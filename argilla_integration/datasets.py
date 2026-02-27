from typing import List, Dict, Any, Optional
import logging

from scrapers.base import ScrapedItem

logger = logging.getLogger(__name__)


class ArgillaManager:
    """Manage Argilla datasets for data curation.

    Falls back gracefully when Argilla is not available.
    """

    def __init__(
        self,
        api_url: str,
        api_key: str,
        workspace: str = "project_recovery",
    ):
        self.api_url = api_url
        self.api_key = api_key
        self.workspace = workspace
        self._available = None
        self._rg = None

    @property
    def available(self) -> bool:
        if self._available is None:
            try:
                import argilla as rg

                rg.init(api_url=self.api_url, api_key=self.api_key)
                self._rg = rg
                self._available = True
                logger.info(f"Connected to Argilla at {self.api_url}")
            except Exception as e:
                logger.warning(f"Argilla not available ({e}), labeling disabled")
                self._available = False
        return self._available

    def create_recovery_dataset(self, name: str = "recovered_data"):
        """Create a dataset for recovered project data."""
        if not self.available:
            logger.info("Argilla unavailable, skipping dataset creation")
            return None

        rg = self._rg
        try:
            settings = rg.Settings(
                fields=[
                    rg.TextField(name="content", title="Content"),
                    rg.TextField(name="source_path", title="Source Path"),
                    rg.TextField(name="filename", title="Filename", required=False),
                ],
                questions=[
                    rg.LabelQuestion(
                        name="relevance",
                        title="Is this relevant to the project?",
                        labels=["relevant", "maybe_relevant", "not_relevant"],
                    ),
                    rg.LabelQuestion(
                        name="content_type",
                        title="Content Type",
                        labels=["core_code", "utility", "configuration", "documentation", "test", "data", "other"],
                    ),
                    rg.LabelQuestion(
                        name="quality",
                        title="Code/Content Quality",
                        labels=["high", "medium", "low", "needs_review"],
                    ),
                    rg.TextQuestion(
                        name="notes",
                        title="Notes / What is this?",
                        required=False,
                    ),
                    rg.LabelQuestion(
                        name="action",
                        title="Recommended Action",
                        labels=["include_as_is", "needs_update", "reference_only", "discard"],
                    ),
                ],
                metadata=[
                    rg.TermsMetadataProperty(name="source_type"),
                    rg.TermsMetadataProperty(name="language"),
                    rg.FloatMetadataProperty(name="confidence_score"),
                    rg.TermsMetadataProperty(name="file_extension"),
                ],
            )

            dataset = rg.Dataset(name=name, workspace=self.workspace, settings=settings)
            try:
                dataset.create()
            except Exception:
                dataset = rg.Dataset.from_argilla(name=name, workspace=self.workspace)

            return dataset

        except Exception as e:
            logger.error(f"Error creating Argilla dataset: {e}")
            return None

    def add_items_to_dataset(self, dataset, items: List[ScrapedItem]) -> int:
        """Add scraped items to Argilla dataset."""
        if dataset is None or not self.available:
            return 0

        rg = self._rg
        records = []

        for item in items:
            record = rg.Record(
                fields={
                    "content": item.content[:10000],
                    "source_path": item.source_path,
                    "filename": item.filename or "",
                },
                metadata={
                    "source_type": item.source_type.value,
                    "language": item.language or "unknown",
                    "confidence_score": item.confidence_score,
                    "file_extension": item.file_extension or "none",
                },
                id=item.id,
            )
            records.append(record)

        if records:
            try:
                dataset.records.log(records)
            except Exception as e:
                logger.error(f"Error adding records to Argilla: {e}")
                return 0

        return len(records)

    def get_labeled_data(self, dataset_name: str, status: str = "completed") -> List[Dict[str, Any]]:
        """Get labeled data from Argilla."""
        if not self.available:
            return []

        rg = self._rg
        try:
            dataset = rg.Dataset.from_argilla(name=dataset_name, workspace=self.workspace)
            labeled_items = []

            for record in dataset.records:
                if record.status == status:
                    responses = {}
                    for response in record.responses:
                        responses.update(response.values)

                    labeled_items.append(
                        {
                            "id": record.id,
                            "content": record.fields.get("content"),
                            "source_path": record.fields.get("source_path"),
                            "filename": record.fields.get("filename"),
                            "metadata": record.metadata,
                            "labels": responses,
                        }
                    )

            return labeled_items
        except Exception as e:
            logger.error(f"Error fetching labeled data: {e}")
            return []

    def export_curated_data(
        self,
        dataset_name: str,
        output_path: str,
        filter_action: Optional[List[str]] = None,
    ) -> int:
        """Export curated data to files."""
        import json
        from pathlib import Path

        filter_action = filter_action or ["include_as_is", "needs_update"]
        labeled = self.get_labeled_data(dataset_name)

        filtered = [item for item in labeled if item.get("labels", {}).get("action") in filter_action]

        output = Path(output_path)
        output.mkdir(parents=True, exist_ok=True)

        with open(output / "curated_data.json", "w") as f:
            json.dump(filtered, f, indent=2, default=str)

        files_dir = output / "files"
        for item in filtered:
            filename = item.get("filename") or f"{item['id']}.txt"
            file_path = files_dir / filename
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "w") as f:
                f.write(item.get("content", ""))

        return len(filtered)

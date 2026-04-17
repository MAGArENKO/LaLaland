import argparse
import asyncio

import uvicorn
from rich.console import Console
from rich.table import Table

console = Console()


def run_api():
    """Run the FastAPI server."""
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)


def run_dashboard():
    """Run the Streamlit dashboard."""
    import subprocess

    subprocess.run(["streamlit", "run", "ui/dashboard.py", "--server.port", "8501", "--server.headless", "true"])


async def run_pipeline_once():
    """Run the pipeline once."""
    from orchestrator.pipeline import RecoveryPipeline

    console.print("[bold blue]Starting Project Recovery Pipeline[/bold blue]")

    pipeline = RecoveryPipeline()
    result = await pipeline.run_full_pipeline()

    table = Table(title="Pipeline Run Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")

    table.add_row("Run ID", result.id)
    table.add_row("Status", result.status.value)
    table.add_row("Items Scraped", str(result.items_scraped))
    table.add_row("Items Processed", str(result.items_processed))
    table.add_row("Items Stored", str(result.items_stored))
    table.add_row("Errors", str(len(result.errors)))

    console.print(table)

    if result.errors:
        console.print("[yellow]Errors:[/yellow]")
        for error in result.errors:
            console.print(f"  - {error}")


def run_worker():
    """Run Celery worker."""
    from orchestrator.tasks import app

    if app:
        app.worker_main(["worker", "--loglevel=info"])
    else:
        console.print("[red]Celery not available[/red]")


def run_beat():
    """Run Celery beat scheduler."""
    from orchestrator.tasks import app

    if app:
        app.worker_main(["beat", "--loglevel=info"])
    else:
        console.print("[red]Celery not available[/red]")


def run_context_help():
    """Show Cursor Cloud-oriented run/test/debug context."""
    console.print("[bold blue]Project Recovery System - Cursor Context Help[/bold blue]")

    services_table = Table(title="Services and Commands")
    services_table.add_column("Service", style="cyan")
    services_table.add_column("Port", style="green")
    services_table.add_column("Command", style="white")
    services_table.add_row("FastAPI API", "8000", "python main.py api")
    services_table.add_row("Streamlit Dashboard", "8501", "python main.py dashboard")
    services_table.add_row("Pipeline (one-shot)", "-", "python main.py pipeline")
    services_table.add_row("Celery Worker", "-", "python main.py worker")
    services_table.add_row("Celery Beat", "-", "python main.py beat")
    console.print(services_table)

    quick_checks_table = Table(title="Quick Checks")
    quick_checks_table.add_column("Goal", style="cyan")
    quick_checks_table.add_column("Command", style="white")
    quick_checks_table.add_row("Run tests", "python -m pytest tests/ -v")
    quick_checks_table.add_row("Run lint", "ruff check .")
    quick_checks_table.add_row("Bring up optional infra", "docker compose up -d qdrant redis postgres")
    quick_checks_table.add_row("API health", "curl -i http://localhost:8000/health")
    quick_checks_table.add_row("Dashboard health", "curl -I http://localhost:8501")
    console.print(quick_checks_table)

    notes_table = Table(title="Operational Notes")
    notes_table.add_column("Topic", style="cyan")
    notes_table.add_column("Details", style="white")
    notes_table.add_row("Source toggles", "Use config/sources.yaml to enable/disable GitHub/filesystem sources.")
    notes_table.add_row("Fallback behavior", "App continues with in-memory fallbacks if external services are unavailable.")
    notes_table.add_row("Model download", "First sentence-transformers run downloads ~90MB into Hugging Face cache.")
    notes_table.add_row("README size", "README.md is a large archive; use focused files for implementation guidance.")
    notes_table.add_row("Tip", "Run `python main.py context` at any time to print this guide.")
    console.print(notes_table)


def main():
    parser = argparse.ArgumentParser(description="Project Recovery System")
    parser.add_argument(
        "command",
        choices=["api", "dashboard", "pipeline", "worker", "beat", "all", "context"],
        help="Command to run",
    )

    args = parser.parse_args()

    if args.command == "api":
        run_api()
    elif args.command == "dashboard":
        run_dashboard()
    elif args.command == "pipeline":
        asyncio.run(run_pipeline_once())
    elif args.command == "worker":
        run_worker()
    elif args.command == "beat":
        run_beat()
    elif args.command == "all":
        console.print("[bold]Use docker-compose to run all services[/bold]")
    elif args.command == "context":
        run_context_help()


if __name__ == "__main__":
    main()

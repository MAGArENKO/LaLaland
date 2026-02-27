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


def main():
    parser = argparse.ArgumentParser(description="Project Recovery System")
    parser.add_argument(
        "command",
        choices=["api", "dashboard", "pipeline", "worker", "beat", "all"],
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


if __name__ == "__main__":
    main()

from . import server
import asyncio
import argparse


def main():
    """Main entry point for the package."""
    parser = argparse.ArgumentParser(description="MotherDuck MCP Server")
    parser.add_argument(
        "--db-path",
        help="Path to local DuckDB database file",
    )

    args = parser.parse_args()
    asyncio.run(server.main(db_path=args.db_path))


if __name__ == "__main__":
    main()

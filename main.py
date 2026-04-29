from pathlib import Path
from agents import ManagerAgent


def main():
    target_path = Path("demo_project")
    output_path = Path("output/codebase_report.md")

    manager = ManagerAgent(target_path=target_path, output_path=output_path)
    result = manager.run()

    print("\n=== SUMMARY ===")
    print(f"Files scanned: {result['summary']['file_count']}")
    print(f"Functions found: {result['summary']['function_count']}")
    print(f"Classes found: {result['summary']['class_count']}")
    print(f"Quality issues: {len(result['quality_issues'])}")
    print(f"Report generated at: {output_path}")


if __name__ == "__main__":
    main()
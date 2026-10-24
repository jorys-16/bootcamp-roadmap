from pathlib import Path

root = Path(__file__).resolve().parent

folders = [
    "curriculum",
    "resources",
    "progress",
    "notes",
    "exercises/javascript",
    "exercises/computer-science",
    "exercises/sql",
    "exercises/python",
    "projects/campus-resource-guide",
    "projects/student-planning-hub/vanilla",
    "projects/data-ml-study/data/raw",
    "docs",
]

files = [
    "README.md",
    "SETUP.md",
    "PROGRESS.md",
    ".gitignore",
    "curriculum/month-01-foundations.md",
    "curriculum/month-02-javascript.md",
    "curriculum/month-03-react-typescript.md",
    "curriculum/month-04-backend-databases.md",
    "curriculum/month-05-testing-deployment.md",
    "curriculum/month-06-python-ai.md",
    "curriculum/month-07-capstone.md",
    "resources/README.md",
    "resources/master-dev.md",
    "notes/README.md",
    "exercises/README.md",
    "projects/campus-resource-guide/README.md",
    "projects/student-planning-hub/README.md",
    "projects/data-ml-study/README.md",
    "docs/architecture.md",
    "docs/decisions.md",
    "docs/code-review.md",
    "docs/demo-checklist.md",
]

files += [
    f"progress/week-{week:02d}.md"
    for week in range(1, 29)
]

for folder in folders:
    (root / folder).mkdir(parents=True, exist_ok=True)

created = 0

for filename in files:
    path = root / filename
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        path.touch()
        created += 1

print(f"Finished! Created {created} new files in {root}")
print("Existing files were left unchanged.")
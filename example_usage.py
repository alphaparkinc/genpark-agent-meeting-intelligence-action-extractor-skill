from client import MeetingActionExtractor

extractor = MeetingActionExtractor()
result = extractor.extract_action_items()
print("=== Meeting Action Extractor Telemetry ===")
print("Total Action Items:", result["items_count"])
print("Overall Feasibility Score:", result["overall_feasibility"])
for item in result["items"]:
    print(f"  [{item['priority']}] {item['assignee']} -> {item['task']} (Due: {item['due_date']})")

import sys
import json
from client import MeetingActionExtractor

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "extract_action_items",
                        "description": "Extracts structured action items, assignees, deadlines, and priorities from meeting transcripts.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "transcript": {"type": "string"}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        args = params.get("arguments", {})
        extractor = MeetingActionExtractor()
        res = extractor.extract_action_items(args.get("transcript"))
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "content": [{"type": "text", "text": json.dumps(res, indent=2)}]
            }
        }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    extractor = MeetingActionExtractor()
    print(json.dumps(extractor.extract_action_items(), indent=2))

if __name__ == "__main__":
    main()

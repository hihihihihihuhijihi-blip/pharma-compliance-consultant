"""Read related knowledge from the fixed public API; never download originals."""
import argparse
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, HTTPRedirectHandler, build_opener

BASE = "https://skills.compliances.cc/kb"

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, new_url):
        return None

DEFAULT_OPENER = build_opener(NoRedirect()).open

def query_kb(action, query=None, document_id=None, limit=5, opener=DEFAULT_OPENER):
    if action not in ("status", "search", "passage"):
        raise ValueError("Unsupported action")
    params = {}
    if action != "status":
        if not isinstance(query, str) or not 2 <= len(query.strip()) <= 200 or not query.strip().isprintable() or len(query.split()) > 8:
            raise ValueError("Use 2–200 printable characters and at most eight generic terms; do not submit private documents")
        params["query"] = query.strip()
    if action == "search":
        if type(limit) is not int or not 1 <= limit <= 10:
            raise ValueError("limit must be 1–10")
        params["limit"] = limit
    if action == "passage":
        if not isinstance(document_id, str) or not 1 <= len(document_id) <= 128:
            raise ValueError("Use the document_id returned by search")
        params["document_id"] = document_id
    url = BASE + "/" + action + ("?" + urlencode(params) if params else "")
    request = Request(url, headers={"Accept": "application/json", "User-Agent": "pharma-compliance-consultant/2.1"})
    with opener(request, timeout=20) as response:
        # Only follow responses that retain the fixed HTTPS API host and path.
        if hasattr(response, "geturl"):
            final = response.geturl()
            if not final.startswith(BASE + "/"):
                raise ValueError("Unexpected API redirect")
        data = response.read(512 * 1024 + 1)
    if len(data) > 512 * 1024:
        raise ValueError("API response too large")
    return json.loads(data.decode("utf-8"))

def main():
    parser = argparse.ArgumentParser(description="Use generic keywords only; no contracts, case data or internal documents")
    sub = parser.add_subparsers(dest="action", required=True)
    sub.add_parser("status")
    search = sub.add_parser("search"); search.add_argument("query")
    search.add_argument("--limit", type=int, default=5)
    passage = sub.add_parser("passage"); passage.add_argument("document_id"); passage.add_argument("query")
    args = parser.parse_args()
    try:
        result = query_kb(args.action, getattr(args, "query", None), getattr(args, "document_id", None), getattr(args, "limit", 5))
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except HTTPError as error:
        parser.exit(1, "API HTTP error: " + str(error.code) + "\n")
    except (URLError, ValueError, TimeoutError, OSError) as error:
        parser.exit(1, "Knowledge query failed: " + type(error).__name__ + "\n")

if __name__ == "__main__":
    main()

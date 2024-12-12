from datetime import datetime, timezone
from typing import Any, Dict
import json
from bson import ObjectId
import re


class JSONEncoder(json.JSONEncoder):
    """Custom JSON encoder for MongoDB documents"""

    def default(self, obj: Any) -> Any:
        if isinstance(obj, ObjectId):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


def format_mongodb_document(doc: Dict[str, Any]) -> Dict[str, Any]:
    """Format MongoDB document for JSON response"""
    return json.loads(json.dumps(doc, cls=JSONEncoder))


def to_camel_case(snake_str: str) -> str:
    """Convert snake_case to camelCase"""
    components = snake_str.split("_")
    return components[0] + "".join(x.title() for x in components[1:])


def to_snake_case(camel_str: str) -> str:
    """Convert camelCase to snake_case"""
    pattern = re.compile(r"(?<!^)(?=[A-Z])")
    return pattern.sub("_", camel_str).lower()


def get_utc_now() -> datetime:
    """Get current UTC datetime"""
    return datetime.now(timezone.utc)


def remove_none_values(d: Dict[str, Any]) -> Dict[str, Any]:
    """Remove None values from dictionary recursively"""
    return {
        k: v if not isinstance(v, dict) else remove_none_values(v)
        for k, v in d.items()
        if v is not None
    }

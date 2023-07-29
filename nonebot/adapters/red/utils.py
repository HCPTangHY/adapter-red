from PIL import Image
from io import BytesIO
from pathlib import Path
from typing import Any

from nonebot.utils import logger_wrapper


log = logger_wrapper("red")


def handle_data(api: str, **data: Any):
    if api == "getSelfProfile":
        return "GET", {}
    if api == "bot/friends":
        return "GET", {}
    if api == "bot/groups":
        return "GET", {}
    if api == "group/muteEveryone":
        return "POST", {"group": data["group"], "enable": data.get("enable", True)}
    if api == "group/kick":
        return "POST", {"uidList": data["uidList"], "group": data["group"], "refuseForever": data.get("refuseForever", False), "reason": data.get("reason", None)}
    if api == "group/getAnnouncements":
        return "POST", {"group": data["group"]}
    if api == "group/getMemberList":
        return "POST", {"group": data["group"], "size": data.get("size", 20)}
    if api == "message/fetchRichMedia":
        return "POST", {
            "msgId": data["msgId"],
            "chatType": data["chatType"],
            "peerUid": data["peerUid"],
            "elementId": data["elementId"],
            "thumbSize": data["thumbSize"],
            "downloadType": data["downloadType"]
        }
    if api == "upload":
        return "POST", data["file"]
    if api == "message/recall":
        return "POST", {"msgIds": data["msgIds"], "peer": data["peer"]}
    if api == "message/getHistory":
        return "POST", {
            "peer": data["peer"],
            "offsetMsgId": data.get("offsetMsgId", 0),
            "count": data.get("count", 100)
        }

def to_bytes(data):
    if isinstance(data, str):
        with open(data, 'rb') as file:
            return file.read()

    elif isinstance(data, Image.Image):
        with BytesIO() as buffer:
            data.save(buffer, format='PNG')
            return buffer.getvalue()

    elif isinstance(data, bytes):
        return data

    elif isinstance(data, BytesIO):
        return data.getvalue()

    elif isinstance(data, Path):
        with data.open('rb') as file:
            return file.read()
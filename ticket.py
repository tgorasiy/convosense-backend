from pydantic import BaseModel
from typing import Optional


class TicketCreate(BaseModel):
title: str
description: str


class TicketOut(BaseModel):
id: str
title: str
description: str
status: str
intent: Optional[str] = None
sentiment: Optional[str] = None
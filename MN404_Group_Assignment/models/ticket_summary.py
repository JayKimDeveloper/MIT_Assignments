from dataclasses import dataclass
from typing import Dict

@dataclass
# Dataclass for Ticket Information
class TicketSummary:
    arena: str
    ticket_counts: Dict[str, int]
    total_price: float
    accompanied: bool

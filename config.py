import os
from dotenv import load_dotenv

load_dotenv()

# =========================
# Discord
# =========================

TOKEN = os.getenv("TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))
SUPPORT_GUILD_ID = int(os.getenv("SUPPORT_GUILD_ID", "0"))

# =========================
# Database
# =========================

DATABASE_URL = os.getenv("DATABASE_URL")

# =========================
# Staff Roles
# =========================

ROLE_OWNER = int(os.getenv("ROLE_OWNER", "0"))
ROLE_DEPUTY = int(os.getenv("ROLE_DEPUTY", "0"))
ROLE_ADMIN = int(os.getenv("ROLE_ADMIN", "0"))  # 運営
ROLE_SENIOR_MOD = int(os.getenv("ROLE_SENIOR_MOD", "0"))
ROLE_MOD = int(os.getenv("ROLE_MOD", "0"))

# =========================
# User Roles
# =========================

ROLE_SERVER_OWNER = int(os.getenv("ROLE_SERVER_OWNER", "0"))
ROLE_PROVIDER = int(os.getenv("ROLE_PROVIDER", "0"))
ROLE_MEMBER = int(os.getenv("ROLE_MEMBER", "0"))

# =========================
# Channels
# =========================

REPORT_CHANNEL = int(os.getenv("REPORT_CHANNEL", "0"))
APPEAL_CHANNEL = int(os.getenv("APPEAL_CHANNEL", "0"))

AUDIT_LOG_CHANNEL = int(os.getenv("AUDIT_LOG_CHANNEL", "0"))
REPORT_LOG_CHANNEL = int(os.getenv("REPORT_LOG_CHANNEL", "0"))
APPEAL_LOG_CHANNEL = int(os.getenv("APPEAL_LOG_CHANNEL", "0"))
ROOM_LOG_CHANNEL = int(os.getenv("ROOM_LOG_CHANNEL", "0"))
ERROR_LOG_CHANNEL = int(os.getenv("ERROR_LOG_CHANNEL", "0"))

# =========================
# GVC Settings
# =========================

MAX_STANDARD_ROOMS = int(
    os.getenv("MAX_STANDARD_ROOMS", "1")
)

MAX_PREMIUM_ROOMS = int(
    os.getenv("MAX_PREMIUM_ROOMS", "3")
)

MAX_VIP_ROOMS = int(
    os.getenv("MAX_VIP_ROOMS", "10")
)

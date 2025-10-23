"""
Die 0711smarthome_fernwartungs_modus-Integration für Home Assistant.

Dieser Code initialisiert die Integration und lädt die Switch-Plattform.
"""
# Datei: custom_components/0711smarthome_fernwartungs_modus/__init__.py
# -----------------------------------------------------------------------------
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

_LOGGER = logging.getLogger(__name__)

# Definiere die Plattform, die diese Integration nutzt.
PLATFORMS = ["switch"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Admin User Toggle from a config entry."""
    # Leite das Setup an die Switch-Plattform weiter.
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    # Entlade die Konfiguration von den Plattformen.
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
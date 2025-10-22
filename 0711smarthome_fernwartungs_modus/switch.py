# switch.py
import logging
from typing import Any # <-- Diese Zeile wurde hinzugefügt

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback) -> None:
    """Set up the 0711smarthome_fernwartungs_modus switch from a config entry."""
    user_id = entry.data["user_id"]
    user_to_control = await hass.auth.async_get_user(user_id)

    if not user_to_control:
        _LOGGER.error(f"User with ID '{user_id}' not found. Cannot create switch.")
        return

    async_add_entities([AdminUserSwitch(hass, entry, user_to_control)])

class AdminUserSwitch(SwitchEntity):
    """Represents a switch to enable/disable an admin user."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry, user_to_control) -> None:
        """Initialize the switch."""
        self.hass = hass
        self._entry = entry
        self._user = user_to_control
        self._attr_name = f"0711smarthome_status {self._user.name}"
        self._attr_unique_id = f"admin_user_toggle_{self._user.id}"
        self._attr_icon = "mdi:account-key"

    @property
    def device_info(self) -> DeviceInfo:
        """Return device information."""
        return DeviceInfo(
            identifiers={(DOMAIN, self._entry.entry_id)},
            name=f"Fernwartungs Modus für {self._user.name}",
            manufacturer="0711 Smart Home",
            model="Fernwartungsmodus",
            sw_version="1.1.1",
            entry_type="service",
        )

    @property
    def is_on(self) -> bool:
        """Return true if the user is active."""
        return self._user.is_active

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Enable the user."""
        _LOGGER.info(f"Enabling admin user: {self._user.name}")
        await self.hass.auth.async_update_user(self._user, is_active=True)
        self.async_schedule_update_ha_state(force_refresh=True)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Disable the user."""
        _LOGGER.info(f"Disabling admin user: {self._user.name}")
        await self.hass.auth.async_update_user(self._user, is_active=False)
        self.async_schedule_update_ha_state(force_refresh=True)

    async def async_update(self) -> None:
        """Fetch latest state of the user."""
        self._user = await self.hass.auth.async_get_user(self._user.id)
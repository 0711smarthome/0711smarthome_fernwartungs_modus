# config_flow.py
import logging
from typing import Any

import voluptuous as vol

from homeassistant import config_entries
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class AdminUserToggleConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Admin User Toggle."""
    VERSION = 1

    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> FlowResult:
        """Handle the initial step."""
        if user_input is not None:
            user = await self.hass.auth.async_get_user(user_input["user_id"])
            if user:
                await self.async_set_unique_id(user.id)
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title=f"Admin: {user.name}",
                    data={"user_id": user.id, "username": user.name},
                )
        
        # In this version, we will not check the current user's ID
        # to avoid the "Could not determine current user" error.
        all_users = await self.hass.auth.async_get_users()
        admin_users = {
            user.id: user.name
            for user in all_users
            if user.is_admin and user.name is not None
        }

        if not admin_users:
            return self.async_abort(reason="no_admin_users")

        schema = vol.Schema({vol.Required("user_id"): vol.In(admin_users)})
        return self.async_show_form(step_id="user", data_schema=schema)
from playwright.sync_api import APIRequestContext


class APIUtils:
    def __init__(self, api_request_context: APIRequestContext):
        self.api_request_context = api_request_context

    def get_system_user_id_by_username(self, username: str) -> int:
        response = self.api_request_context.get(
            "/web/index.php/api/v2/admin/users",
            params={
                "username": username,
                "limit": 50,
                "offset": 0,
            },
        )

        if not response.ok:
            raise RuntimeError(
                f'Failed to search system user "{username}". '
                f"Status: {response.status}. Body: {response.text()}"
            )

        body = response.json()

        for user in body.get("data", []):
            if user.get("userName") == username or user.get("username") == username:
                return user["id"]

        raise RuntimeError(f'System user "{username}" was not found.')

    def delete_system_users(self, user_ids: list[int]) -> None:
        if not user_ids:
            return

        response = self.api_request_context.delete(
            "/web/index.php/api/v2/admin/users",
            data={
                "ids": user_ids,
            },
        )

        if response.status not in [200, 404]:
            raise RuntimeError(
                f"Failed to delete system users {user_ids}. "
                f"Status: {response.status}. Body: {response.text()}"
            )
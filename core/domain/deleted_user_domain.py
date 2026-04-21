"""Domain Object for deleted users."""

from core import utils


class DeletedUser:
    """Domain object for an Oppia's deleted user."""

    def __init__(self, user_id: str) -> None:
        """Initializes a DeletedUser domain object.

        Args:
            user_id: str. The id of the deleted user.
        """
        self.user_id = user_id

    def validate(self) -> None:
        """Validates the properties of DeletedUser.

        Raises:
            ValidationError: if any of the properties are invalid.
        """

        if not isinstance(self.user_id, str):
            raise utils.ValidationError(
                f"Expected user_id to be str, received {(type(self.user_id))}"
            )

        if not self.user_id.strip():
            raise utils.ValidationError(
                "Expected user_id to be a nonempty string"
            )

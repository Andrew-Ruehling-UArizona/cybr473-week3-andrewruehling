"""
ChirpyHub Models - Classes, Objects, and Validation

Two small classes that show why you bundle data with the code that works on it.
A User owns a handle. A Chirp owns its text and a reference to the User who
posted it.

Read this before Assignment 3. Your FileProcessor is built the same way: data
stored on self in __init__, methods that act on that data, and validation that
returns a value instead of crashing.
"""

MAX_CHIRP_LENGTH = 280
MIN_HANDLE_LENGTH = 3
MAX_HANDLE_LENGTH = 15


class User:
    """One ChirpyHub account."""

    def __init__(self, handle: str, display_name: str) -> None:
        # Everything the object needs to know about itself lives on self.
        # Two User objects each keep their own handle and never share one.
        self.handle = handle
        self.display_name = display_name
        self.is_verified = False

    def validate(self) -> bool:
        """Return True if this handle is usable, False if it is not.

        Notice this returns a value rather than printing or crashing. The
        caller decides what to do about a bad handle. A method that prints
        can only ever be used one way; a method that returns can be used
        anywhere, including inside an if statement.
        """
        if len(self.handle) < MIN_HANDLE_LENGTH:
            return False
        if len(self.handle) > MAX_HANDLE_LENGTH:
            return False
        # Underscores are allowed, so strip them before the character check.
        if not self.handle.replace("_", "").isalnum():
            return False
        return True

    def mention(self) -> str:
        """Return the handle in @-form, the way it appears inside a chirp."""
        return "@" + self.handle


class Chirp:
    """One post. Holds a User, not a copy of that user's handle."""

    def __init__(self, author: User, text: str) -> None:
        # author is a whole User object. This is the important line.
        #
        # We could have stored the handle as a plain string instead:
        #     self.author_handle = "sam_r"
        #
        # That copy goes stale the moment Sam renames the account. Every chirp
        # ever posted would still say the old name and you would have to find
        # and rewrite all of them. Holding the User means there is one handle,
        # in one place, and every chirp reads the current value automatically.
        self.author = author
        self.text = text
        self.likes = 0

    def validate(self) -> bool:
        """Return True if this chirp can be posted."""
        if not self.text.strip():
            return False
        if len(self.text) > MAX_CHIRP_LENGTH:
            return False
        # A chirp is only valid if its author is valid. Each class checks its
        # own data, and Chirp asks User rather than re-checking handle rules.
        return self.author.validate()

    def like(self) -> int:
        """Add one like and return the new total."""
        self.likes = self.likes + 1
        return self.likes

    def summary(self) -> str:
        """Return one printable line describing this chirp."""
        return f"{self.author.mention()}: {self.text} ({self.likes} likes)"


# ---------------------------------------------------------------------------
# Using the classes
# ---------------------------------------------------------------------------

sam = User("sam_r", "Sam Rivera")
dana = User("d", "Dana Okonkwo")          # too short, will fail validation

print("sam valid: ", sam.validate())
print("dana valid:", dana.validate())
print()

first = Chirp(sam, "Deployed the new parser. Nothing caught fire.")
second = Chirp(sam, "Spoke too soon.")
empty = Chirp(sam, "   ")                  # whitespace only, will fail

# Both chirps point at the same User object. There is one Sam, not two copies.
print("same author object:", first.author is second.author)
print()

first.like()
first.like()
second.like()

print(first.summary())
print(second.summary())
print()

print("empty chirp valid:", empty.validate())
print()

# Rename the account. Neither Chirp is touched, and both are already correct.
sam.handle = "sam_rivera"
print("after rename:")
print(first.summary())
print(second.summary())

from abc import ABC, abstractmethod


class Device(ABC):
    """Abstract device class representing any controllable device."""
    volume = 0

    @abstractmethod
    def get_name(self) -> str:
        """Return the name of the device."""


class Radio(Device):
    """Concrete Radio device."""
    def get_name(self):
        return f"Radio {self}"


class TV(Device):
    """Concrete TV device."""
    def get_name(self):
        return f"TV {self}"


class Remote(ABC):
    """Abstract Remote class for controlling devices."""
    @abstractmethod
    def volume_up(self):
        """Increase the volume of the device."""

    @abstractmethod
    def volume_down(self):
        """Decrease the volume of the device."""


class BasicRemote(Remote):
    """Concrete Remote that bridges control to a Device."""
    def __init__(self, device: Device):
        self.device = device

    def volume_up(self):
        self.device.volume += 1
        print(f"{self.device.get_name()} volume up: {self.device.volume}")

    def volume_down(self):
        self.device.volume -= 1
        print(f"{self.device.get_name()} volume down: {self.device.volume}")


# Usage
if __name__ == "__main__":
    radio = Radio()
    tv = TV()
    radio_remote = BasicRemote(radio)
    tv_remote = BasicRemote(tv)

    radio_remote.volume_up()
    radio_remote.volume_up()
    radio_remote.volume_down()

    tv_remote.volume_up()
    tv_remote.volume_down()
    tv_remote.volume_up()
    tv_remote.volume_down()

### Disabling the Serial Login in Raspberry Pi
1. Open Raspberry Pi Config.
    ```
    sudo raspi-config
    ```
2. Go to `Interfacing Options`.
3. Go to `Serial Ports`.
4. In the next prompt say **NO** to the `login shell to be accessible over serial`.
5. Enable the `Serial Port Hardware` and press `enter`.
6. You should get the following text.
    ```
    "The serial login shell is disabled
    The serial interface is enabled".
    ```
7. Reboot the Raspberry Pi.
    ```
    sudo reboot
    ```
8. Run the following command after the reboot to check if the serial port is still enabled.
    ```
    dmesg | grep tty
    ```
    The output should be empty.
-------------------------------------------------
### Serial Read on Raspberry Pi
1. Connect your module to the RX and TX pins
    ```
    UART RX -> GPIO14
    UART TX -> GPIO15
    ```
2. Run the following command to check if your module is connected to the Raspberry Pi.
    ```
    dmesg | grep tty
    ```
    The output should show the port which your module is connected to.
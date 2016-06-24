# rpm_device is the name of the ported device
%define rpm_device ham
# rpm_vendor is used in the rpm space
%define rpm_vendor zuk
# Manufacturer and device name to be shown in UI
%define vendor_pretty ZUK
%define device_pretty Z1
# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator 1
%define have_led 1
%include droid-hal-version/droid-hal-version.inc

#!/bin/bash

#read -p "Check for updates? (Y/n): " update

#if [[ "$update" =~ ^[Yy]$ || -z "$update" ]]; then
#    sudo pacman -S --needed pipewire pipewire-audio-client-libraries libspa-0.2-bluetooth libspa-0.2-jack
#    sudo pacman -S --needed pavucontrol ffmpeg
#else
#    echo "Skipping updates..."
#fi

# Enable and start pipewire services
systemctl --user --now enable pipewire pipewire-pulse
systemctl --user --now start pipewire pipewire-pulse

# Load the virtual sink module if not already loaded
if ! pactl list short modules | grep -q module-null-sink; then
    pactl load-module module-null-sink sink_name=Virtual_Sink sink_properties=device.description="Virtual_Sink"
fi

# Get sink and monitor names
VIRTUAL_SINK="Virtual_Sink"
MONITOR_NAME="${VIRTUAL_SINK}.monitor"

# Set virtual sink as default for output
pactl set-default-sink "$VIRTUAL_SINK"
# Set virtual sink's monitor as default source (input)
pactl set-default-source "$MONITOR_NAME"

echo "Recording from virtual sink monitor..."
echo "Press Ctrl+C to stop recording."

# Start recording
ffmpeg -f pulse -i "$MONITOR_NAME" ~/Documents/output.wav

# Prompt to unload the module
read -p "Do you want to unload the virtual sink module? (Y/n): " ans
if [[ "$ans" =~ ^[Yy]$ || -z "$ans" ]]; then
    MODULE_ID=$(pactl list short modules | grep 'module-null-sink' | awk '{print $1}')
    pactl unload-module "$MODULE_ID"
    echo "Virtual sink unloaded."
else
    echo "Virtual sink left loaded."
fi

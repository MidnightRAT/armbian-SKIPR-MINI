# armbian-SKIPR-MINI
Modificated armbian for MKS SKIPR-MINI v1.0 based 3d-printers Flying Bear S1 / Infimech TX.

### Prepare EMMC
- Buy a Makerbase EMMC card whith adapter (https://vi.aliexpress.com/item/1005007552981093.html).
- Download an armbian-mkspi image. Now worked with 1.0.2-25.2.1 bookworm_current_6.12.12 (https://github.com/redrathnure/armbian-mkspi/releases/tag/mkspi%2F1.0.2-25.2.1).
- Burn an armbian-mkspi image to EMMC whith dd/balena-Etcher etc..
- Mount EMMC boot and root partitions.
- Add to `/boot/armbianEnv.txt` next strings (like in this repo https://github.com/MidnightRAT/armbian-SKIPR-MINI/blob/main/BOOT/armbianEnv.txt):
```bash
overlays=rk3328-i2c0 rk3328-i2s1-pcm5102 rk3328-mksklipad50-enable-rtc-end1 rk3328-mkspi-disable-lcd-spi rk3328-opp-1.4ghz rk3328-spi-spidev rk3328-uart1
usbstoragequirks=0x2537:0x1066:u,0x2537:0x1068:u
```
- Replace file `/boot/dtb/rockchip/rk3328-mkspi.dtb` on EMMC with file from this repo (https://github.com/MidnightRAT/armbian-SKIPR-MINI/blob/main/BOOT/dtb/rockchip/rk3328-mkspi.dtb).
- Sync and detach EMMC.

### First start and upgrade armbian
- Install EMMC on printer SKIPR-MINI v1.0 board.
- Connect to ethernet and power on the printer. Your printer must acquire an IP address using DHCP.
- Login to printer via SSH with user: root passwd: 1234

```
home
└── mks
    ├── gcode_files -> printer_data/gcodes
    ├── klipper_config -> printer_data/config
    ├── klipper_logs -> printer_data/logs
    └── printer_data
        ├── config
        │   └── plr.cfg
        ├── gcodes
        └── logs
```

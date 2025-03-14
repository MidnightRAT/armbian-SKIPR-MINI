# armbian-SKIPR-MINI
Modificated armbian for MKS SKIPR-MINI v1.0 based 3d-printers Flying Bear S1 / Infimech TX

### Prepare EMMC
- By a EMMC whith adapter (https://vi.aliexpress.com/item/1005007552981093.html)
- Download latest armbian-mkspi. Now worked with 1.0.2-25.2.1 bookworm_current_6.12.12 (https://github.com/redrathnure/armbian-mkspi/releases/tag/mkspi%2F1.0.2-25.2.1)
- Write armbian-mkspi image to EMMC whith dd/balena-Etcher etc.
- Mount boot partition
- Add strings to `/boot/armbianEnv.txt` 
`overlays=rk3328-i2c0 rk3328-i2s1-pcm5102 rk3328-mksklipad50-enable-rtc-end1 rk3328-mkspi-disable-lcd-spi rk3328-opp-1.4ghz rk3328-spi-spidev rk3328-uart1` 
`usbstoragequirks=0x2537:0x1066:u,0x2537:0x1068:u` 
- Replace file /boot/dtb/rockchip/rk3328-mkspi.dtb


### First start and upgrade armbian
- Install EMMC on printer board

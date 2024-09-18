# QEMU
add bridge network

```bash
nmcli con add type bridge con-name br0 ifname br0
nmcli con add type bridge-slave ifname enx00133b00043c master br0
```

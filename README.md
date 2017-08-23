# Yunohost-partition-plugin
A plugin to manage disks in Yunhost

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)

## Installation

#### Automatic .deb install

Download the latest `yunohost-partition-plugin_x.x.x.deb` on the [Github Release Page](https://github.com/lecler-i/yunohost-partition-plugin/releases/latest)

Open a terminal and go into the directory of the download.

Install the package with the command `dpkg -i FILEYOUJUSTDOWNLOAD.deb`

If the installation fail because of missing dependencies, install them
with `apt-get install -f`

#### Manual Install

Download to your project directory and copy the files into your system :

```sh
git clone https://github.com/lecler-i/yunohost-partition-plugin.git
cd yunohost-partition-plugin
cp data/actionsmap/ynh_part.yml /usr/share/moulinette/actionsmap/
cp -r src/ynh_part /usr/lib/moulinette/
```

## Usage

`yunohost part --help`
`yunohost part_raid --help`


#### List partition for a disk

`yunohost part list /dev/sda`

#### List partitions on All disks

`yunohost part list-all`

#### Create a new partition

>primary (p) NTFS partition at sector 2097152 of a 1Gb size

`yunohost part create /dev/sdb 2097152 p ntfs +1G`

## Support

Please [open an issue](https://github.com/lecler-i/yunohost-partition-plugin/issues) for support.


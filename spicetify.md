# Installing Spicetify on Ubuntu Linux

Spicetify is a multiplatform command-line tool for customizing the official Spotify client. This guide covers the steps to install Spicetify on Ubuntu Linux using the pre-built binary.

## Prerequisites

- **Spotify Client**: Make sure you have installed the Spotify client.
  If you haven't installed Spotify yet, you can install it via the official apt repository. See the [Spotify for Linux](https://www.spotify.com/us/download/linux/) page for more details.
- **Terminal**: Basic familiarity with using a terminal window.

## 1. Install Spicetify CLI

Open your terminal and run the following command to install the Spicetify CLI:

```bash
curl -fsSL https://raw.githubusercontent.com/spicetify/cli/main/install.sh | sh
```

This command downloads and executes the installation script directly, adding Spicetify to your system.

## 2. Install Spicetify Marketplace (Optional)

The Spicetify Marketplace provides a convenient sidebar tab within Spotify for accessing themes, extensions, and snippets. To install it, run:

```bash
curl -fsSL https://raw.githubusercontent.com/spicetify/marketplace/main/resources/install.sh | sh
```

## 3. Set File Permissions

For Spicetify to be able to modify the required Spotify files, you must grant write permissions to the Spotify directories. Assuming Spotify is installed via the apt repo and the installation directory is `/usr/share/spotify`, run:

```bash
sudo chmod a+wr /usr/share/spotify
sudo chmod a+wr -R /usr/share/spotify/Apps
```

> **Note:** If your Spotify installation path differs, adjust the commands accordingly.

## 4. Applying Customizations

After installing and configuring the permissions, back up the original Spotify files and apply the Spicetify customizations with:

```bash
spicetify backup apply
```

This command will create a backup of your original settings and then apply the current customizations from your Spicetify setup.

## 5. Updating Spicetify

When Spotify updates its client, you may need to re-apply Spicetify or update it:

- **Reapply Changes:**
  ```bash
  spicetify backup apply
  ```
- **Upgrade Spicetify (if required):**
  ```bash
  spicetify upgrade
  ```

Check the [Spicetify documentation](https://github.com/spicetify/spicetify-cli) for further details on managing updates and troubleshooting.

## 6. Launch Spotify

Once completed, launch the Spotify client. You should see your custom theme and any enabled Marketplace extensions applied to the interface.

## Conclusion

You now have Spicetify installed on your Ubuntu system! Enjoy customizing your Spotify client. If you run into any issues, please refer to the [Spicetify CLI GitHub page](https://github.com/spicetify/spicetify-cli) for additional support.

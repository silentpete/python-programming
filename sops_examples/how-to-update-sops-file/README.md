# How to use SOPS with age encryption in Python?

While looking into using Mozilla SOPS with Python... I found that the pip module is no longer supported and have to use the Go binary.

## Install `sops` on your System

Download the binary

```none
curl -LO https://github.com/getsops/sops/releases/download/v3.8.1/sops-v3.8.1.linux.amd64
```

Move the binary in to your PATH

```none
mv sops-v3.8.1.linux.amd64 /usr/local/bin/sops
```

Make the binary executable

```none
chmod +x /usr/local/bin/sops
```

Confirm `sops`

```none
sops --version
```

## Install `age` on your System

Get the version from the releases page.

```none
curl -LO https://github.com/FiloSottile/age/releases/download/v1.1.1/age-v1.1.1-linux-amd64.tar.gz
```

extract

```none
tar -xf age-{tab}
```

copy binaries to /usr/local/bin/

```none
cp age/age* /usr/local/bin/.
```

Confirm `age`

```none
age --version
```

## Create age key pair

We can now create a key file. Sops will use this file as the encrytion mechanism.

```none
$ age-keygen -o age.private.key
age-keygen: warning: writing secret key to a world-readable file
Public key: age1fn9xna4ygs90fwdrmq6c7e8vdzx5rclm3zwt2umvq02qfxuqudmqtghj7n
```

## Export public key to SOPS_AGE_RECIPIENTS

```none
$ export SOPS_AGE_RECIPIENTS=$(age-keygen -y age.private.key)
```

## Export age private key

```none
$ export SOPS_AGE_KEY_FILE="$PWD/age.private.key"
```

## Encrypt accounts.yaml

```none
$ sops -e accounts.yaml > accounts.enc.yaml
```

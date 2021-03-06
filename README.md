# Visuelle
Paired with [HAROLD](https://github.com/dyllonrc/HAROLD), Visuelle can play a CSH members chosen audio file in addition to a short gif or webm, on the television in the lobby, and any other screen currently displaying the application. At the tap of a button, the users currently active video will play on repeat for the duration of their audio clip.
This application runs on OKD (formerly Openshift) by Red Hat. All that's needed to set up a new display is a Raspberry Pi set to display the [application's webpage](https://loudnoises-loudnoises.cs.house).

## Installation and Use
The program runs remotely on OKD. It can be run locally as a flask webapp by just running `python wsgi.py`. Feel free to make PRs. All of the relevant code is encased in [wsgi.py](wsgi.py) and [templates/index.html](templates/index.html).

## Auto running a web browser (Kiosk mode)
Very hard. I didn't use this method but [it works fine](https://blog.eq8.eu/til/raspberi-pi-as-kiosk-load-browser-on-startup-fullscreen.html). Alls that's needed to do is configure the display manager to automatically log in, which can be done using `raspi-config`, and then have a web browser run in kiosk mode. I used chromium in fullscreen, with all extensions and notifications turned off.

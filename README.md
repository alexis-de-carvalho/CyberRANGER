# CyberRANGER

This projet is a free, open-source, non-lucrative **CyberRange**.
You will be able to easily deploy Machine Networks and create Cyber Challenges !
If you are interested in CyberSecurity, it is made for you to learn and practice !

It relies on 2 different open-source projects:
*  [CTFd](https://github.com/CTFd/CTFd/) (for the challenges platform, which also manages the network instances)
*  [MI-LXC](https://github.com/flesueur/mi-lxc/) (for networks/machines generation)


Additional features were added, mainly:
* Instances Management (thanks to **VirtualBox**)
* Ability to add Access Tokens (avoiding any player accessing a forbidden machine)


## Challenges

There are currently 2 types of challenges:
* *simple challenges* (only questions, and can involve files to download)
* *infrastructure challenges*, requiring a network of machines (the player can be granted access to a starting machine and try to elevate locally/gain some access to the others...)


The current repository is provided with 5 challenges:

* 4 simple challenges
* 1 infrastructure challenge


Feel free to try them !

## How to use it

**It is highly recommended to run this project within a Virtual Machine.**

If you wish to be able to deploy and run machines for your challenges:

1. You need the [MI-LXC .ova file](https://flesueur.irisa.fr/mi-lxc/images/milxc-debian-amd64-1.4.2.ova)
    
    Rename it `network.ova` and place it in your home directory.

2.  Ensure kernel virtualization is enabled on the machine hosting this CyberRange.

    To ensure you have every tool required, run the script:
    ```
    ./prepare.sh
    ```

3. Run the platform with:

    ```
    python3 serve.py
    ```
    
    You can access it at `localhost:4000`
    

Challenges creation, and flag submission functions as in [CTFd](https://github.com/CTFd/CTFd/).

The current repository is provided with only one user, with credentials **admin:admin**
(change it if needed).

You can add as many users (players) as you like.


## Managing the Instances

*Only if you need to deploy machines for a challenge.*

1. Create a folder in `deploy/networks` with the wanted name. For example, `deploy/networks/challenge01_network`

    It has to follow [MI-LXC](https://github.com/flesueur/mi-lxc/) network structure.
    
    Feel free to duplicate the provided folder **network_example** and change it.
    
    
2. As **admin**, go to the **"Instances"** menu. Click on the "+" button.
    
    a. Enter the **SAME** network name (i.e. the name of the folder you just created).

    b. Choose a value (multi-purpose variable). Enter 0 if you don't need it.
    
    c. Specify the Challenge ID. **(The challenge MUST have been created before you make the network instance).**

3. Finally, click on the newly created instance (in the table). Then press the play button to create the instance. Wait for creation (check terminal logging or wait to be redirected to the instances menu).

    Your instance is ready !
    

>> Be careful, you cannot have more than one running instance per network. If you want to create 2 instances of the same network template, simply duplicate the corresponding folder under "deploy/machines"


## Adding access

For now, access is added manually. To do so, go to the `deploy` folder and enter the following command:

```
./user.sh <ip> <machine_name> <access_token>

```

For example, to add an access token for **machine-home** (from the provided **network_example** folder):
```
./user.sh <ip> machine-home secret
```



Players can now access this machine by typing:

```
ssh machine-home@<ip>
```

And enter **"secret"** when a password is asked (it may ask twice, this is normal behavior).


## User Side

Once you have created (as admin) some challenges and launched network instances (when some challenges need it), users will be able to play.

From the user side, the menu **"Instances"** allows to check IP addresses of instances, so they can access machines if required by the challenge.

If the status is on **RUNNING**, access is possible !

Learn ! Be creative ! Have fun !


## Credits

Thank you to the creators and contributors of [CTFd](https://github.com/CTFd/CTFd/) and [MI-LXC](https://github.com/flesueur/mi-lxc/) for these very useful projects.

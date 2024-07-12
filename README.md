
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Terminal Troll Show</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 80%;
            margin: auto;
            overflow: hidden;
        }
        header {
            background: #333;
            color: #fff;
            padding-top: 30px;
            min-height: 70px;
            border-bottom: #0779e4 3px solid;
        }
        header a {
            color: #fff;
            text-decoration: none;
            text-transform: uppercase;
            font-size: 16px;
        }
        header ul {
            padding: 0;
            list-style: none;
        }
        header li {
            display: inline;
            padding: 0 20px 0 20px;
        }
        header #branding {
            float: left;
        }
        header #branding h1 {
            margin: 0;
        }
        header nav {
            float: right;
            margin-top: 10px;
        }
        section {
            padding: 20px;
            margin: 20px 0;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background: #e4e4e4;
            padding: 5px;
        }
        pre {
            background: #333;
            color: #fff;
            padding: 10px;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div id="branding">
                <h1>Terminal Troll Show</h1>
            </div>
        </div>
    </header>
    <section class="container">
        <h2>Features</h2>
        <ul>
            <li>Displays random numbers in the terminal</li>
            <li>Shows a trolling message</li>
            <li>Reveals your IP information, netmask, and broadcast address</li>
            <li>Animates futuristic bars, rotating slashes, waves, random characters, and a spiral</li>
            <li>Ends with a final message</li>
        </ul>
    </section>
    <section class="container">
        <h2>Installation</h2>
        <p>To run this script, you need to have Python installed on your system. You also need to install the following dependencies:</p>
        <ol>
            <li><code>psutil</code> - A cross-platform library for retrieving information on running processes and system utilization.</li>
            <li><code>windows-curses</code> - A Windows port of the curses library to enable terminal handling.</li>
        </ol>
        <p>You can install these dependencies using <code>pip</code>:</p>
        <pre><code>pip install psutil windows-curses</code></pre>
    </section>
    <section class="container">
        <h2>Usage</h2>
        <ol>
            <li>Save the script to a file named <code>terminal_troll_show.py</code>.</li>
            <li>Open a terminal and navigate to the directory where the script is saved.</li>
            <li>Run the script with Python:</li>
        </ol>
        <pre><code>python terminal_troll_show.py</code></pre>
    </section>
    <section class="container">
        <h2>Code Explanation</h2>
        <p>The script performs the following steps:</p>
        <ol>
            <li>Imports necessary libraries.</li>
            <li>Defines a function to get IP information using the <code>psutil</code> library.</li>
            <li>Defines the <code>main</code> function which contains all the animations and displays.</li>
            <li>Uses the <code>curses</code> library to handle terminal display and animations.</li>
            <li>Displays various animations and information in sequence:
                <ul>
                    <li>Random numbers</li>
                    <li>Trolling message</li>
                    <li>IP information (IP address, netmask, broadcast address)</li>
                    <li>Futuristic bars</li>
                    <li>Rotating slashes</li>
                    <li>Wave pattern</li>
                    <li>Random characters</li>
                    <li>Spiral pattern</li>
                    <li>Final message</li>
                </ul>
            </li>
        </ol>
    </section>
    <section class="container">
        <h2>Dependencies</h2>
        <ul>
            <li>Python 3.x</li>
            <li><code>psutil</code></li>
            <li><code>windows-curses</code> (only for Windows users)</li>
        </ul>
    </section>
    <section class="container">
        <h2>Example Output</h2>
        <p>Here's an example of what you might see when you run the script:</p>
        <pre><code>Random numbers displayed in the terminal...
You've been trolled!
Your IP: 192.168.1.2
Netmask: 255.255.255.0
Broadcast: 192.168.1.255
Futuristic bars animation...
Rotating slashes animation...
Wave animation...
Random characters animation...
Spiral animation...
End of the Show!</code></pre>
    </section>
    <section class="container">
        <h2>License</h2>
        <p>This project is licensed under the MIT License. See the LICENSE file for details.</p>
    </section>
    <section class="container">
        <h2>Acknowledgements</h2>
        <ul>
            <li><code>curses</code> library for handling terminal display and animations</li>
            <li><code>psutil</code> library for retrieving IP information</li>
            <li><code>windows-curses</code> for enabling <code>curses</code> on Windows</li>
        </ul>
    </section>
    <footer>
        <div class="container">
            <p>Enjoy it!</p>
        </div>
    </footer>
</body>
</html>

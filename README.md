<h1 align=center> Biome Fest</h1>
<p align=center>
<img src="bf_low_res.png" alt="Application Image" class=center></img>
<h2>What does Biome Fest do?</h2>
<b>Biome Fest is meant to be a GUI version of minecraft-pi-server. This program communicates with the terminal and displays it in an easy to understand interface.</p>
<p>Biome fest is meant to be an easy to understand server software for MCPI users who want something that works right out of the box.</p>
</b>
<h2>How to install Biome Fest</h2>
<p>Before installing Biome Fest, make sure to have installed</p>
<ul>
  <li>Python 3.6 or higher</li>
  <li><a href="https://jenkins.thebrokenrail.com/job/minecraft-pi-reborn/job/master/lastSuccessfulBuild/artifact/out/deb/">minecraft-pi-server</a></li>
</ul>
<p>Clone this project into an empty directory using</p>
<code>
  git clone https://github.com/MrBrasilMan/Biome-Fest.git
 </code>
<p>To run Biome Fest, execute the bash script run.sh</p>
<code>
      bash run.sh
</code>
<p>This will configure everything to boot up!</p>
<h2>Why Biome Fest?</h2>
Biome Fest is a front-end using a somewhat tolerable back-end of minecraft-pi-server.<br>While getting the player count is a little slow due to some unoptimised code I must work on in the newer releases, the rest of the server runs as smooth as butter.<br>Instead of being a command tool, Biome Fest uses a simple WYSIWYG GUI approch. This is great for newbies trying to get into Minecraft Pi: Reborn</h2>
<h2>What is not implemented?</h2>
A few things I want to implement in 2.0 are (but not limited by)<br>
<ul>
  <li>Chat functionaility with front-end</li>
  <li>Installer to install minecraft-pi-server.deb natively</li>
  <li>Possibly implement a tab system to simplify things similar to MCPIL</li>
 </ul>

"""Fix guides: one page per common cause of a slow Windows PC, served at /fix/<slug>/.

Each guide answers the search question first, then says whether the culprit is
safe to stop, then the free manual fix. Know My PC gets one short mention at the
end (build.py adds it). Edit or add guides here, then run:  python build.py
"""

GUIDES = [
    {
        "slug": "vmmem-high-memory",
        "title": "Vmmem or VmmemWSL Using Too Much Memory: How to Fix It",
        "h1": "Vmmem using too much memory",
        "description": "Vmmem and VmmemWSL are the WSL 2 and Docker virtual machine. Why they hold on to RAM, how to free it with wsl --shutdown, and how to cap it in .wslconfig.",
        "lede": "Vmmem is the virtual machine behind WSL 2 and Docker Desktop. It's not a virus, and you can free its memory in seconds.",
        "summary": "The WSL 2 and Docker virtual machine, and how to cap its RAM",
        "sections": [
            ("what", "What Vmmem is", r"""
<p><strong>Vmmem</strong> (called <strong>VmmemWSL</strong> on newer versions of Windows) is how Task Manager shows the memory and CPU used by a virtual machine. On most PCs that machine runs WSL 2, the Windows Subsystem for Linux. Docker Desktop runs on WSL 2 too, so starting Docker starts Vmmem.</p>
<p>It uses so much memory because Linux treats spare RAM as file cache, and WSL 2 gives that memory back to Windows slowly. By default WSL 2 can use up to half of your PC's RAM, and it holds on to it after builds or containers have finished.</p>"""),
            ("safe", "Is it safe to end?", r"""
<p>Don't end it from Task Manager; Windows usually refuses anyway. Shut WSL down properly instead (below). That stops every Linux distro and Docker container, so save your work in them first.</p>"""),
            ("free", "Free the memory now", r"""
<p>Open PowerShell or Command Prompt and run:</p>
<pre><code>wsl --shutdown</code></pre>
<p>Vmmem disappears within a few seconds. WSL starts again next time you open a Linux terminal. If you use Docker Desktop, quit it from its icon in the taskbar first.</p>"""),
            ("cap", "Cap how much memory WSL can use", r"""
<p>Create or edit the file <code>%UserProfile%\.wslconfig</code> (for example <code>C:\Users\you\.wslconfig</code>) and add:</p>
<pre><code>[wsl2]
memory=6GB</code></pre>
<p>Pick a number that leaves room for Windows: 4 to 6 GB on a 16 GB PC, 8 to 12 GB on a 32 GB PC. Then run <code>wsl --shutdown</code> so the setting takes effect. Docker Desktop with the WSL 2 backend follows the same limit.</p>
<p>Recent versions of WSL can also hand unused memory back to Windows on their own. Run <code>wsl --update</code>, then add this to the same file:</p>
<pre><code>[experimental]
autoMemoryReclaim=gradual</code></pre>"""),
        ],
        "app": "Know My PC labels Vmmem as the WSL or Docker virtual machine, shows how much memory it's holding, and lists your WSL distros and Docker containers next to it.",
    },
    {
        "slug": "antimalware-service-executable-high-cpu",
        "title": "Antimalware Service Executable High CPU: How to Fix It",
        "h1": "Antimalware Service Executable using high CPU",
        "description": "Antimalware Service Executable (MsMpEng.exe) is Microsoft Defender scanning files. Why it spikes, when it stops on its own, and how to make it scan less.",
        "lede": "This is Microsoft Defender, the antivirus built into Windows. A spike is usually a scan that finishes on its own.",
        "summary": "Microsoft Defender scanning, and how to make it scan less",
        "sections": [
            ("what", "What it is", r"""
<p><strong>Antimalware Service Executable</strong> is the name Task Manager gives <code>MsMpEng.exe</code>, the engine of Microsoft Defender Antivirus. It checks files as they're opened and written, and runs a regular quick scan.</p>
<p>It gets busy when lots of files change at once: right after a download or an install, while a game updates, while you unzip something big, or when developer tools write thousands of small files (<code>node_modules</code>, build folders). It also runs its regular scan during Windows' automatic maintenance.</p>"""),
            ("safe", "Is it safe to end?", r"""
<p>No. Windows protects it, and it's your antivirus, so turning it off isn't a good fix. Making it do less work is.</p>"""),
            ("wait", "If it just started", r"""
<p>Let it finish. A spike after a download or update usually settles within a few minutes. If you just installed another antivirus, make sure only one is doing real-time protection: Windows Security turns Defender's off automatically when another one is active.</p>"""),
            ("schedule", "Move the regular scan to when you're away", r"""
<p>Defender's regular scan runs during automatic maintenance, which Windows starts when the PC is idle at a set time. If your PC is never idle then, it runs while you're using it. To change the time:</p>
<ol><li>Open Control Panel → System and Security → Security and Maintenance.</li><li>Expand <strong>Maintenance</strong> and click <strong>Change maintenance settings</strong>.</li><li>Pick a time when the PC is usually on but you're not using it.</li></ol>"""),
            ("exclude", "Exclude folders you trust", r"""
<p>If it's busy every time you build code or update games, exclude those folders from real-time scanning:</p>
<ol><li>Open Windows Security → Virus &amp; threat protection.</li><li>Under Virus &amp; threat protection settings, click <strong>Manage settings</strong>.</li><li>Scroll to Exclusions, click <strong>Add or remove exclusions</strong>, and add the folder.</li></ol>
<p>Only exclude folders whose contents you trust, such as your own code projects. Never exclude Downloads or a whole drive. On Windows 11, a <strong>Dev Drive</strong> is a safer option for code: Defender scans it in a faster performance mode instead of not at all.</p>"""),
        ],
        "app": "Know My PC recognises a Defender scan when it's the cause, says it'll finish on its own, and shows how long it's been running so you can tell a normal scan from one that never stops.",
    },
    {
        "slug": "windows-modules-installer-worker-high-cpu",
        "title": "Windows Modules Installer Worker High CPU: How to Fix It",
        "h1": "Windows Modules Installer Worker using high CPU",
        "description": "Windows Modules Installer Worker (TiWorker.exe) is Windows Update installing updates. Why it's busy, how long it takes, and what to do if it never stops.",
        "lede": "This is Windows Update installing or cleaning up updates. Let it finish, restart, and it goes quiet.",
        "summary": "Windows Update installing, and what to do if it never stops",
        "sections": [
            ("what", "What it is", r"""
<p><strong>Windows Modules Installer Worker</strong> is <code>TiWorker.exe</code>, the part of Windows Update that installs updates and Windows features and removes old versions of system files afterwards. It's busiest right after updates download, before and after a restart, and during automatic maintenance.</p>
<p>On a PC with a hard drive instead of an SSD it can keep the disk at 100% for half an hour or more.</p>"""),
            ("safe", "Is it safe to end?", r"""
<p>Don't. Stopping it in the middle can leave an update half-installed, and Windows starts it again anyway.</p>"""),
            ("finish", "Let it finish, then restart", r"""
<ol><li>Open Settings → Windows Update and see whether an update is installing or waiting for a restart.</li><li>Leave the PC on until it's done, then restart if asked.</li></ol>
<p>To stop updates from restarting your PC while you work, set <strong>Active hours</strong> in Settings → Windows Update → Advanced options.</p>"""),
            ("stuck", "If it's busy for hours, every day", r"""
<p>An update that keeps failing will reinstall over and over. First run the troubleshooter: on Windows 11, Settings → System → Troubleshoot → Other troubleshooters → <strong>Windows Update</strong>. If that doesn't help, repair Windows' system files. Open Terminal as administrator and run these one after the other:</p>
<pre><code>DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow</code></pre>
<p>Both take a while. Restart afterwards and check Windows Update again.</p>"""),
        ],
        "app": "Know My PC recognises Windows Update when it's the cause and tells you it will finish on its own, so you don't end it by mistake.",
    },
    {
        "slug": "searchindexer-high-cpu",
        "title": "SearchIndexer.exe High CPU or Disk Usage: How to Fix It",
        "h1": "Windows Search indexer using high CPU or disk",
        "description": "SearchIndexer.exe builds the index for Windows search. Why it gets busy, how to index fewer folders, and how to rebuild an index that's stuck.",
        "lede": "Windows is building its search index. It's busy after big file changes and settles down by itself, but you can make it do less.",
        "summary": "Windows Search indexing, and how to index fewer folders",
        "sections": [
            ("what", "What it is", r"""
<p><strong>SearchIndexer.exe</strong> (Microsoft Windows Search Indexer) keeps a list of your files and their contents so Start, File Explorer and Outlook can search quickly. <code>SearchProtocolHost.exe</code> and <code>SearchFilterHost.exe</code> are its helpers that read inside files.</p>
<p>It's busy after you copy lots of files, add a drive, sync a big mailbox, or after a Windows update. With <strong>Enhanced</strong> search on, it indexes your whole PC instead of just your user folders.</p>"""),
            ("safe", "Is it safe to end?", r"""
<p>Ending it does no harm, but Windows starts it again. Usually it settles within an hour. If it's busy every day, give it less to index.</p>"""),
            ("less", "Index fewer folders", r"""
<ol><li>Windows 11: open Settings → Privacy &amp; security → <strong>Searching Windows</strong>. Windows 10: Settings → Search → Searching Windows.</li><li>Choose <strong>Classic</strong> instead of Enhanced. Classic indexes only your libraries and desktop.</li><li>Under <strong>Exclude folders from enhanced search</strong>, add folders full of files you never search: code projects, game libraries, virtual machine disks, backups.</li></ol>"""),
            ("rebuild", "If it never finishes", r"""
<p>A damaged index can make it work forever. Search Start for <strong>Indexing Options</strong>, click <strong>Advanced</strong>, then <strong>Rebuild</strong>. Search results are incomplete until the rebuild finishes.</p>
<p>If you never use Windows search, you can turn indexing off: open Services, double-click <strong>Windows Search</strong>, set Startup type to Disabled and click Stop. Searching in Start, File Explorer and Outlook becomes much slower.</p>"""),
        ],
        "app": "Know My PC recognises search indexing when it's the cause and tells you it will settle on its own, so you know whether to wait or act.",
    },
    {
        "slug": "c-drive-full",
        "title": "C: Drive Full? What's Taking Up Space and How to Free It",
        "h1": "What's taking up space on your C: drive",
        "description": "Where space hides on a full C: drive in Windows 11 and 10: Windows Update leftovers, temp files, hibernation, games, developer caches, WSL disks and AI models.",
        "lede": "A full C: drive slows Windows down. Here's where space usually piles up, and how to get it back safely.",
        "summary": "Where space hides on Windows, and how to get it back",
        "sections": [
            ("start", "Start with Windows' own view", r"""
<p>Open Settings → System → <strong>Storage</strong>. It shows what's using space by category, and <strong>Cleanup recommendations</strong> lists big files, unused apps and files already in the cloud. Turn on <strong>Storage Sense</strong> on the same page to clean temporary files and the Recycle Bin automatically.</p>"""),
            ("windows", "Windows leftovers", r"""
<ul>
<li><strong>Windows Update files and old Windows versions.</strong> Search Start for Disk Cleanup, click <strong>Clean up system files</strong>, and tick Windows Update Cleanup and Previous Windows installation(s). This can free several gigabytes.</li>
<li><strong>Temporary files.</strong> Settings → System → Storage → Temporary files.</li>
<li><strong>Recycle Bin.</strong> Files you deleted still count until it's emptied.</li>
<li><strong>Hibernation file.</strong> <code>hiberfil.sys</code> can be as large as several gigabytes. If you never hibernate, run <code>powercfg /hibernate off</code> in an administrator Terminal to remove it. This also turns off Fast startup.</li>
</ul>
<p>Leave <code>pagefile.sys</code> alone. Windows needs it.</p>"""),
            ("yours", "Your own files and apps", r"""
<ul>
<li><strong>Downloads.</strong> Installers and zip files you've already used.</li>
<li><strong>Installed apps.</strong> Settings → Apps → Installed apps, sorted by size.</li>
<li><strong>Games.</strong> Steam, Epic and Xbox can move a game to another drive from their own settings instead of reinstalling it.</li>
</ul>"""),
            ("dev", "Developer caches, WSL disks and AI models", r"""
<ul>
<li><strong>Package caches.</strong> <code>npm cache clean --force</code>, <code>pip cache purge</code>, <code>dotnet nuget locals all --clear</code>. Cargo keeps downloads in <code>%UserProfile%\.cargo\registry</code>.</li>
<li><strong>Docker.</strong> <code>docker system prune</code> removes stopped containers and unused images.</li>
<li><strong>WSL disks.</strong> Each Linux distro lives in an <code>ext4.vhdx</code> file that grows but doesn't shrink on its own, so deleting files inside Linux doesn't give Windows the space back. Recent WSL versions can fix that with <code>wsl --manage &lt;distro&gt; --set-sparse true</code>.</li>
<li><strong>Ollama models.</strong> Stored in <code>%UserProfile%\.ollama\models</code>. Run <code>ollama list</code> to see them and <code>ollama rm &lt;model&gt;</code> to delete one.</li>
</ul>"""),
        ],
        "app": "Know My PC's Storage view maps your folders, checks all of these places for you, and moves anything you clear to the Recycle Bin, never deleting outright.",
    },
    {
        "slug": "port-in-use",
        "title": "Port Already in Use on Windows: Find What's Using It",
        "h1": "Find what's using a port on Windows",
        "description": "Port 3000 or 8080 already in use on Windows? Find the process with PowerShell or netstat, stop it, and fix ports Windows has reserved for Hyper-V and WSL.",
        "lede": "“Port already in use” means another process is listening on it. Two commands find it, and a third frees it.",
        "summary": "Find and free a port that's already in use",
        "sections": [
            ("find", "Find the process", r"""
<p>In PowerShell, replace 3000 with your port:</p>
<pre><code>Get-NetTCPConnection -LocalPort 3000 -State Listen |
  Select-Object LocalAddress, OwningProcess
Get-Process -Id &lt;OwningProcess&gt;</code></pre>
<p>Or in Command Prompt, where the last column is the process ID:</p>
<pre><code>netstat -ano | findstr :3000
tasklist /FI "PID eq &lt;PID&gt;"</code></pre>"""),
            ("stop", "Stop it", r"""
<pre><code>Stop-Process -Id &lt;PID&gt;</code></pre>
<p>Or <code>taskkill /PID &lt;PID&gt; /F</code> in Command Prompt. Usually it's a dev server left running after its terminal closed, often <code>node.exe</code> or <code>python.exe</code>.</p>"""),
            ("special", "When the owner looks strange", r"""
<ul>
<li><strong>wslrelay.exe</strong> or <strong>com.docker.backend.exe</strong>: the port belongs to something running inside WSL or a Docker container. Stop it there (<code>docker ps</code>, then <code>docker stop</code>).</li>
<li><strong>System (PID 4)</strong>: a Windows service such as IIS is using it.</li>
<li><strong>Nothing is listening but you still get “access denied”</strong>: Hyper-V, WSL or Docker reserved a range of ports. List them with <code>netsh interface ipv4 show excludedportrange protocol=tcp</code> and pick a port outside those ranges.</li>
</ul>"""),
            ("network", "Is it reachable from your network?", r"""
<p>Check the LocalAddress. <code>127.0.0.1</code> or <code>::1</code> means only your PC can connect. <code>0.0.0.0</code> or <code>::</code> means other devices on your network can reach it too, which you may not want on public Wi-Fi.</p>"""),
        ],
        "app": "Know My PC's Developer view lists every dev server with its port and project folder, warns when one is reachable from your network, and flags processes left running after their terminal closed.",
    },
]

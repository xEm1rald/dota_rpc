# 🧩 Dota RPC

Display your **Dota 2 in-game stats** as a rich presence in Discord — powered by Game State Integration (GSI).

---

## ⚙️ How to Use

1. **Download & Install**
   - Get the latest `.exe` from the [Releases](#) page *(or clone this repository)*.  
   - Run the application.

2. **Configure Game State Integration**
   - Open the **Config** tab in the app.  
   - In **Config GSI Data**, select:
     - `provider`
     - `player`
     - `hero`
     - `map`
     - `abilities`  
   - Press **“Update ConfigGSI”** to apply settings.

3. **Enable GSI in Dota 2**
   - Add the following to your Dota 2 **Launch Options**:  
     ```bash
     -gamestateintegration
     ```

4. **Start the Server**
   - Go to the **Info** tab.  
   - Click **“Run Server”**.  
   - Once Dota 2 is running, your Discord Rich Presence will update automatically.

---

## 🖼️ Preview

![Preview](https://i.ibb.co/gMXgDNkY/image.png)

---

## 💡 Tips

- Make sure **Dota 2** and **Discord** are both running before starting the server.  
- If RPC doesn’t update, check that your **GSI config file** is correctly generated in your Dota 2 `cfg` directory.  
- Works best with **AioPresence (async)** for smooth, non-blocking updates.


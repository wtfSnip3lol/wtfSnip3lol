<style>
  .container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
  }
  
  .header {
    text-align: center;
    padding: 40px 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 20px;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
  }
  
  .header h1 {
    margin: 0;
    font-size: 2.5em;
    font-weight: 800;
  }
  
  .header p {
    margin: 10px 0 0 0;
    font-size: 1.1em;
    opacity: 0.9;
  }
  
  .button-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 15px;
    margin: 30px 0;
  }
  
  .btn {
    padding: 20px;
    border: none;
    border-radius: 15px;
    font-size: 1.1em;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    transition: all 0.3s ease;
    color: white;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  }
  
  .btn:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
  }
  
  .btn-twitter {
    background: linear-gradient(135deg, #1DA1F2 0%, #1a8cd8 100%);
  }
  
  .btn-twitch {
    background: linear-gradient(135deg, #9147FF 0%, #7828e8 100%);
  }
  
  .btn-discord {
    background: linear-gradient(135deg, #5865F2 0%, #4752d9 100%);
  }
  
  .footer {
    text-align: center;
    padding: 20px;
    color: #666;
    font-size: 0.9em;
  }
</style>

<div class="container">
  <div class="header">
    <h1>👋 hey</h1>
    <p>i'm <strong>Snip3</strong></p>
    <p style="margin-top: 15px; font-size: 0.95em;">just a random guy yk</p>
  </div>
  
  <div class="button-grid">
    <a href="https://twitter.com/Snip3_lol" class="btn btn-twitter">
      <span>𝕏 Twitter</span>
    </a>
    <a href="https://twitch.tv/snip3lol" class="btn btn-twitch">
      <span>📺 Twitch</span>
    </a>
    <a href="https://discord.com/users/1085805846094675988" class="btn btn-discord">
      <span>💬 Discord</span>
    </a>
  </div>
  
  <div class="footer">
    <p>✨ let's connect!</p>
  </div>
</div>

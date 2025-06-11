
  <h1>CraftWise</h1>

  <p>
    CraftWise is a Streamlit-based application that provides tailored writing suggestions by leveraging OpenAI’s GPT-4o model. Users can choose to supply their own OpenAI API key (with no usage limit) or opt to use a default API key (limited to 5 suggestions per session). CraftWise allows writers to specify an audience level, desired formality, domain context, and intent, then automatically rewrites any input text according to those parameters.
  </p>

  <hr />

  <h2>Table of Contents</h2>
  <ol>
    <li><a href="#features">Features</a></li>
    <li><a href="#requirements">Requirements</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#configuration">Configuration</a>
      <ul>
        <li><a href="#option-1-use-your-own-api-key">Option 1: Use Your Own API Key</a></li>
        <li><a href="#option-2-use-the-default-api-key">Option 2: Use the Default API Key</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#streamlit-app-walkthrough">Streamlit App Walkthrough</a></li>
    <li><a href="#project-structure">Project Structure</a></li>
    <li><a href="#license">License</a></li>
  </ol>

  <hr />

  <h2 id="features">Features</h2>
  <ul>
    <li>
      <strong>GPT-4o-Powered Rewriting</strong><br />
      Sends one chat completion request to the GPT-4o model, leveraging OpenAI’s state-of-the-art language understanding.
    </li>
    <li>
      <strong>Customizable Options</strong>
      <ul>
        <li><strong>Audience</strong>: <code>general</code> / <code>knowledgeable</code> / <code>expert</code></li>
        <li><strong>Formality</strong>: <code>informal</code> / <code>neutral</code> / <code>formal</code></li>
        <li><strong>Domain</strong>: <code>academic</code> / <code>business</code> / <code>general</code> / <code>email</code> / <code>casual</code> / <code>creative</code></li>
        <li><strong>Intent</strong>: <code>inform</code> / <code>describe</code> / <code>convince</code> / <code>tell a story</code></li>
      </ul>
    </li>
    <li>
      <strong>API Key Flexibility</strong><br />
      Use your own OpenAI API key with no request limit. Alternatively, use a shared “default” API key, limited to <strong>5 suggestions per session</strong>.
    </li>
    <li>
      <strong>Session-Based Rate Limiting (Default Key Only)</strong><br />
      If the default key is selected, the app counts requests in <code>st.session_state</code> and disables further calls after 5.
    </li>
    <li>
      <strong>Error Handling &amp; Safeguards</strong><br />
      <ul>
        <li>Checks for missing or invalid API key.</li>
        <li>Ensures “Text to Rewrite” is not empty before calling OpenAI.</li>
        <li>Catches and displays any API-call errors (network issues, rate-limit, invalid model, etc.).</li>
      </ul>
    </li>
  </ul>

  <hr />

  <h2 id="requirements">Requirements</h2>
  <ul>
    <li>Python 3.8+</li>
    <li>Streamlit</li>
    <li>OpenAI Python SDK</li>
  </ul>
  <p>Install the required packages via:</p>
  <pre><code>pip install streamlit openai</code></pre>

  <hr />

  <h2 id="installation">Installation</h2>
  <ol>
    <li>
      <p><strong>Clone this repository</strong></p>
      <pre><code>git clone https://github.com/othnielObasi/craftwise.git
cd craftwise</code></pre>
    </li>
    <li>
      <p><strong>Create &amp; activate a virtual environment</strong> (optional, but recommended)</p>
      <pre><code>python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.\.venv\Scripts\activate    # Windows PowerShell</code></pre>
    </li>
    <li>
      <p><strong>Install dependencies</strong></p>
      <pre><code>pip install streamlit openai</code></pre>
    </li>
  </ol>

  <hr />

  <h2 id="configuration">Configuration</h2>

  <h3 id="option-1-use-your-own-api-key">Option 1: Use Your Own API Key</h3>
  <ol>
    <li>At runtime, the app will prompt you for an OpenAI API key in a password-protected text box.</li>
    <li>Copy &amp; paste your key (e.g. <code>sk-abc123...</code>) when prompted.</li>
    <li>There is no usage limit when you supply your own key.</li>
  </ol>

  <h3 id="option-2-use-the-default-api-key">Option 2: Use the Default API Key</h3>
  <ol>
    <li>
      <p>Set the environment variable <code>DEFAULT_OPENAI_API_KEY</code> to a valid OpenAI key that you (or your organization) share.</p>
      <pre><code>export DEFAULT_OPENAI_API_KEY="sk-DEFAULT_KEY_HERE"</code></pre>
      <p>On Windows Command Prompt or PowerShell:</p>
      <pre><code>setx DEFAULT_OPENAI_API_KEY "sk-DEFAULT_KEY_HERE"</code></pre>
    </li>
    <li>Restart your terminal/session so that <code>os.getenv("DEFAULT_OPENAI_API_KEY")</code> can detect it.</li>
    <li>
      <p>When you launch the app, check “Use default API key (max 5 suggestions)” to enable rate-limited access.</p>
      <ul>
        <li>You will see an info banner telling you: <em>You are using the default API key. Limited to 5 suggestions this session.</em></li>
        <li>After 5 rewrite requests, the “Generate Suggestions” button becomes disabled. A warning banner will instruct you to refresh or enter your own API key.</li>
      </ul>
    </li>
  </ol>

  <hr />

  <h2 id="usage">Usage</h2>
  <ol>
    <li>
      <p>From the project root, launch Streamlit:</p>
      <pre><code>streamlit run streamlit_app.py</code></pre>
    </li>
    <li>In your browser, navigate to the local URL shown in the terminal (e.g., <code>http://localhost:8501</code>).</li>
    <li>
      <p><strong>Choose an API Key</strong></p>
      <ul>
        <li>If you want unlimited access, leave “Use default API key” unchecked, then paste your personal key in the box.</li>
        <li>If you prefer to use the shared default key (and are okay with 5 requests per session), check “Use default API key (max 5 suggestions).”</li>
      </ul>
    </li>
    <li>
      <p><strong>Enter the Text to Rewrite</strong></p>
      <p>Type or paste any paragraph or block of text into the “Enter Text to Rewrite” field.</p>
    </li>
    <li>
      <p><strong>Select Your Options</strong></p>
      <ul>
        <li><strong>Audience</strong>: Choose between <code>general</code>, <code>knowledgeable</code>, or <code>expert</code>.</li>
        <li><strong>Formality</strong>: Choose <code>informal</code>, <code>neutral</code>, or <code>formal</code>.</li>
        <li><strong>Domain</strong>: Choose from <code>academic</code>, <code>business</code>, <code>general</code>, <code>email</code>, <code>casual</code>, or <code>creative</code>.</li>
        <li><strong>Intent</strong>: Choose to <code>inform</code>, <code>describe</code>, <code>convince</code>, or <code>tell a story</code>.</li>
      </ul>
    </li>
    <li>
      <p><strong>Generate Suggestions</strong></p>
      <ul>
        <li>Click the <strong>Generate Suggestions</strong> button.</li>
        <li>If you are using the default key, the app will display a spinner with the current request count (e.g., “Generating tailored suggestions (Request 2/5)…”).</li>
        <li>After GPT-4o processes your request, scroll down to see the “Tailored Suggestions” text area populate with the rewritten output.</li>
      </ul>
    </li>
    <li>
      <p><strong>Rate Limiting (Default Key Only)</strong></p>
      <ul>
        <li>If you selected the default key, each click increments a counter in <code>st.session_state</code>.</li>
        <li>Once you reach 5 total requests, the app disables the button and shows:
          <pre><code>Request limit reached (5 suggestions). To continue, enter your own API key.</code></pre>
        </li>
      </ul>
    </li>
  </ol>

  <hr />

  <h2 id="streamlit-app-walkthrough">Streamlit App Walkthrough</h2>
  <ol>
    <li>
      <h3>API Key Selection Pane</h3>
      <ul>
        <li>Checkbox to toggle “Use default API key (max 5 suggestions)”.</li>
        <li>If unchecked: a password field appears, prompting the user to paste their personal key.</li>
        <li>If checked: the default key is automatically loaded from <code>os.getenv("DEFAULT_OPENAI_API_KEY")</code>.</li>
      </ul>
    </li>
    <li>
      <h3>Input Section</h3>
      <ul>
        <li><strong>Text to Rewrite</strong>: Multi-line text area.</li>
        <li><strong>Audience</strong>: <code>radio</code> widget with options [<code>general</code>, <code>knowledgeable</code>, <code>expert</code>].</li>
        <li><strong>Formality</strong>: <code>radio</code> widget with options [<code>informal</code>, <code>neutral</code>, <code>formal</code>].</li>
        <li><strong>Domain</strong>: <code>selectbox</code> widget with choices [<code>academic</code>, <code>business</code>, <code>general</code>, <code>email</code>, <code>casual</code>, <code>creative</code>].</li>
        <li><strong>Intent</strong>: <code>radio</code> widget with options [<code>inform</code>, <code>describe</code>, <code>convince</code>, <code>tell a story</code>].</li>
      </ul>
    </li>
    <li>
      <h3>Generate Button</h3>
      <ul>
        <li>Disabled if the default key has reached 5 requests.</li>
        <li>When clicked:
          <ul>
            <li>Checks that “Text to Rewrite” is non-empty.</li>
            <li>If using the default key, increments <code>st.session_state.default_request_count</code>.</li>
            <li>Calls <code>assistant.get_suggestions(...)</code>, sending a single GPT-4o chat completion request.</li>
            <li>Displays the rewritten output in a read-only text area labeled “Tailored Suggestions.”</li>
          </ul>
        </li>
        <li>After 5 requests with the default key, a warning appears:
          <pre><code>You have reached the 5-suggestion limit using the default API key. Refresh or enter your own key to continue.</code></pre>
        </li>
      </ul>
    </li>
    <li>
      <h3>TailoredWritingAssistant Class</h3>
      <p>
        Holds four options in <code>self.options</code> and constructs a prompt like:
      </p>
      <pre><code>Considering the audience is knowledgeable, the formality is formal, the domain is business, and the intent is to inform, rewrite the text:

&lt;User’s input text&gt;</code></pre>
      <p>
        Sends that prompt (with a “system” role message) to <code>client.chat.completions.create(...)</code> using model <code>gpt-4o</code>. Returns the assistant’s generated content or an error message if the call fails.
      </p>
    </li>
  </ol>

  <hr />

  <h2 id="project-structure">Project Structure</h2>
  <pre><code>craftwise/
├── streamlit_app.py         # Main Streamlit application
├── README.md                # This README file
├── requirements.txt         # (optional) List of Python dependencies
└── .streamlit/
    └── secrets.toml         # (optional) For storing DEFAULT_OPENAI_API_KEY if using Streamlit Secrets</code></pre>

  <p>
    <strong>streamlit_app.py</strong>: The primary script to launch CraftWise. Implements API key selection/validation, rate limiting logic, Streamlit widgets, and the TailoredWritingAssistant class.
  </p>
  <p>
    <strong>README.md</strong>: Project overview, installation &amp; usage instructions (this file).
  </p>
  <p>
    <strong>requirements.txt</strong> (optional but recommended): Lists required Python packages. Example contents:
  </p>
  <pre><code>streamlit&gt;=1.20.0
openai&gt;=0.27.0</code></pre>
  <p>
    <strong>.streamlit/secrets.toml</strong> (optional): If you prefer to store <code>DEFAULT_OPENAI_API_KEY</code> in Streamlit’s built-in secrets, place this file with:
  </p>
  <pre><code>DEFAULT_OPENAI_API_KEY = "sk-DEFAULT_KEY_HERE"</code></pre>

  <hr />

  <h2 id="license">License</h2>
  <p>
    This project is released under the MIT License. Feel free to fork, modify, and use it for your own writing-assistant needs.
  </p>

</body>
</html>

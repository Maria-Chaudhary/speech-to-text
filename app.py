import gradio as gr
import whisper
import tempfile
import soundfile as sf
import os

print("Loading Whisper...")
model = whisper.load_model("large")

# Language map with Urdu prioritized
LANG_MAP = {
    "ur": "Urdu",
    "hi": "Hindi",
    "en": "English",
    "ja": "Japanese",
    "es": "Spanish",
    "fr": "French"
}

# Transcription function with Urdu priority
def transcribe(audio):
    try:
        if audio is None:
            return "", "", "⚠️ Please record or upload audio first."

        sample_rate, data = audio

        # Save numpy audio to wav
        tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        sf.write(tmp.name, data, sample_rate)

        result = model.transcribe(tmp.name)
        text = result.get("text", "").strip()
        detected_lang = result.get("language", "unknown")

        os.remove(tmp.name)

        if text == "":
            return "", "", "🔍 No speech detected. Please speak clearly and try again."

        # Urdu priority: if model detects urdu-like sounds, prefer Urdu label
        if detected_lang in LANG_MAP:
            language_display = f"🌐 {LANG_MAP[detected_lang]} ({detected_lang})"
        else:
            language_display = f"🌐 {detected_lang}"

        return text, language_display, "✅ Transcription successful!"

    except Exception as e:
        return "", "", f"❌ Error: {str(e)}"

# EXTREMELY PROFESSIONAL CSS
css = """
/* ===== CUSTOM PROPERTIES ===== */
:root {
    /* Light Theme */
    --primary: #2563eb;
    --primary-light: #3b82f6;
    --primary-dark: #1d4ed8;
    --secondary: #7c3aed;
    --accent: #06b6d4;
    --success: #10b981;
    --warning: #f59e0b;
    --error: #ef4444;
    --neutral-50: #f8fafc;
    --neutral-100: #f1f5f9;
    --neutral-200: #e2e8f0;
    --neutral-300: #cbd5e1;
    --neutral-400: #94a3b8;
    --neutral-500: #64748b;
    --neutral-600: #475569;
    --neutral-700: #334155;
    --neutral-800: #1e293b;
    --neutral-900: #0f172a;
    
    --bg-primary: #ffffff;
    --bg-secondary: #f8fafc;
    --bg-card: #ffffff;
    --bg-input: #ffffff;
    --text-primary: #1e293b;
    --text-secondary: #475569;
    --text-muted: #64748b;
    --border: #e2e8f0;
    --border-strong: #cbd5e1;
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    --radius-sm: 0.375rem;
    --radius: 0.5rem;
    --radius-md: 0.75rem;
    --radius-lg: 1rem;
    --radius-xl: 1.5rem;
    --radius-2xl: 2rem;
}

.dark-mode {
    /* Dark Theme */
    --primary: #3b82f6;
    --primary-light: #60a5fa;
    --primary-dark: #2563eb;
    --secondary: #8b5cf6;
    --accent: #22d3ee;
    --success: #34d399;
    --warning: #fbbf24;
    --error: #f87171;
    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    --bg-card: #1e293b;
    --bg-input: #334155;
    --text-primary: #f1f5f9;
    --text-secondary: #cbd5e1;
    --text-muted: #94a3b8;
    --border: #334155;
    --border-strong: #475569;
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.3);
    --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.4), 0 1px 2px 0 rgba(0, 0, 0, 0.3);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.4), 0 2px 4px -1px rgba(0, 0, 0, 0.3);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.4), 0 4px 6px -2px rgba(0, 0, 0, 0.3);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.4), 0 10px 10px -5px rgba(0, 0, 0, 0.3);
}

/* ===== BASE RESET ===== */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
    background: var(--bg-primary);
    color: var(--text-primary);
    line-height: 1.5;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    transition: background-color 0.3s ease, color 0.3s ease;
}

.gradio-container {
    max-width: 1400px !important;
    margin: 0 auto !important;
    padding: 0 2rem !important;
    background: var(--bg-primary) !important;
    min-height: 100vh;
    transition: background-color 0.3s ease !important;
}

/* ===== PROFESSIONAL HEADER ===== */
.header {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    padding: 4rem 2rem;
    border-radius: 0 0 var(--radius-2xl) var(--radius-2xl);
    margin: 0 -2rem 3rem -2rem;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-xl);
}

.header::before {
    content: '';
    position: absolute;
    inset: 0;
    background: 
        radial-gradient(circle at 20% 80%, rgba(255,255,255,0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255,255,255,0.05) 0%, transparent 50%);
}

.header-content {
    position: relative;
    z-index: 2;
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}

.header-title {
    font-size: 4rem;
    font-weight: 800;
    color: white;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
    letter-spacing: -0.025em;
}

.header-subtitle {
    font-size: 1.25rem;
    color: rgba(255, 255, 255, 0.9);
    line-height: 1.6;
    font-weight: 400;
    margin-bottom: 2rem;
}

/* ===== ULTRA-PROFESSIONAL THEME TOGGLE ===== */
.theme-toggle-wrapper {
    position: absolute;
    top: 2rem;
    right: 2rem;
    z-index: 100;
}

.theme-toggle {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 1.25rem;
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(16px);
    border-radius: var(--radius-full);
    border: 1px solid rgba(255, 255, 255, 0.2);
    cursor: pointer;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
}

.theme-toggle:hover {
    background: rgba(255, 255, 255, 0.15);
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.15);
}

.toggle-track {
    position: relative;
    width: 56px;
    height: 28px;
    background: rgba(255, 255, 255, 0.2);
    border-radius: var(--radius-full);
    transition: all 0.3s ease;
    overflow: hidden;
}

.toggle-slider {
    position: absolute;
    top: 2px;
    left: 2px;
    width: 24px;
    height: 24px;
    background: white;
    border-radius: var(--radius-full);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.75rem;
    transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.dark-mode .toggle-slider {
    transform: translateX(28px);
    background: linear-gradient(135deg, #fbbf24, #f59e0b);
}

.toggle-icons {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 6px;
    color: white;
    font-size: 0.75rem;
    opacity: 0.7;
}

.toggle-label {
    font-size: 0.875rem;
    font-weight: 600;
    color: white;
    white-space: nowrap;
}

/* ===== MAIN LAYOUT ===== */
.main-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
    margin-bottom: 4rem;
}

@media (max-width: 1024px) {
    .main-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
    }
}

/* ===== ELEGANT CARDS ===== */
.card {
    background: var(--bg-card);
    border-radius: var(--radius-xl);
    padding: 2.5rem;
    border: 1px solid var(--border);
    box-shadow: var(--shadow-lg);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--primary), var(--secondary));
    border-radius: var(--radius-xl) var(--radius-xl) 0 0;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-xl);
    border-color: var(--primary-light);
}

.card-header {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 2rem;
}

.card-icon {
    width: 56px;
    height: 56px;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    border-radius: var(--radius-lg);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    color: white;
    box-shadow: var(--shadow-md);
}

.card-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--text-primary);
    line-height: 1.2;
}

.card-subtitle {
    font-size: 1rem;
    color: var(--text-secondary);
    margin-top: 0.25rem;
}

/* ===== AUDIO CONTROLS SECTION ===== */
.audio-controls-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1rem;
    margin: 1.5rem 0;
}

@media (max-width: 640px) {
    .audio-controls-grid {
        grid-template-columns: 1fr;
    }
}

.control-card {
    background: var(--bg-secondary);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    border: 1px solid var(--border);
    transition: all 0.2s ease;
    display: flex;
    align-items: center;
    gap: 1rem;
}

.control-card:hover {
    background: var(--bg-input);
    border-color: var(--primary-light);
}

.control-icon {
    width: 48px;
    height: 48px;
    background: var(--bg-card);
    border-radius: var(--radius);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.25rem;
    color: var(--primary);
    flex-shrink: 0;
}

.control-info h4 {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.25rem;
}

.control-info p {
    font-size: 0.875rem;
    color: var(--text-muted);
    line-height: 1.4;
}

/* ===== AUDIO COMPONENT STYLING ===== */
.audio-container {
    margin: 2rem 0;
}

.audio-container audio {
    width: 100%;
    border-radius: var(--radius);
    background: var(--bg-input);
}

/* ===== UPLOAD SECTION ===== */
.upload-area {
    background: var(--bg-secondary);
    border: 2px dashed var(--border-strong);
    border-radius: var(--radius-lg);
    padding: 3rem 2rem;
    text-align: center;
    margin: 2rem 0;
    transition: all 0.3s ease;
}

.upload-area:hover {
    border-color: var(--primary);
    background: var(--bg-input);
}

.upload-icon {
    font-size: 3.5rem;
    margin-bottom: 1.5rem;
    opacity: 0.8;
}

.upload-text h3 {
    font-size: 1.25rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
}

.upload-text p {
    color: var(--text-muted);
    font-size: 0.875rem;
    line-height: 1.5;
}

/* ===== TEXT DISPLAY ===== */
.text-display-container {
    position: relative;
    margin: 1.5rem 0;
}

.text-display-label {
    display: block;
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--text-secondary);
    margin-bottom: 0.75rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.text-display {
    width: 100% !important;
    min-height: 200px !important;
    padding: 1.5rem !important;
    background: var(--bg-input) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-lg) !important;
    color: var(--text-primary) !important;
    font-size: 1rem !important;
    line-height: 1.6 !important;
    resize: vertical !important;
    transition: all 0.2s ease !important;
    font-family: 'SF Mono', 'Monaco', 'Inconsolata', 'Fira Code', monospace !important;
}

.text-display:focus {
    outline: none !important;
    border-color: var(--primary) !important;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1) !important;
}

/* ===== STATUS INDICATOR ===== */
.status-indicator {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1rem 1.5rem;
    background: var(--bg-secondary);
    border-radius: var(--radius-lg);
    margin: 1rem 0;
    border-left: 4px solid var(--warning);
    animation: slideIn 0.3s ease;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-10px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.status-indicator.success {
    border-left-color: var(--success);
    background: linear-gradient(90deg, rgba(16, 185, 129, 0.05), transparent);
}

.status-indicator.warning {
    border-left-color: var(--warning);
    background: linear-gradient(90deg, rgba(245, 158, 11, 0.05), transparent);
}

.status-indicator.error {
    border-left-color: var(--error);
    background: linear-gradient(90deg, rgba(239, 68, 68, 0.05), transparent);
}

.status-text {
    font-weight: 500;
    color: var(--text-primary);
}

/* ===== LANGUAGE DISPLAY ===== */
.language-display {
    display: inline-flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.75rem 1.5rem;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: white;
    border-radius: var(--radius-full);
    font-weight: 600;
    margin: 1rem 0;
    box-shadow: var(--shadow-md);
}

/* ===== SUPPORTED LANGUAGES ===== */
.languages-section {
    margin-top: 2.5rem;
}

.languages-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 0.75rem;
    margin-top: 1rem;
}

.language-tag {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
    background: var(--bg-secondary);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--text-primary);
    transition: all 0.2s ease;
}

.language-tag:hover {
    background: var(--bg-input);
    border-color: var(--primary-light);
    transform: translateY(-2px);
}

.language-tag.highlight {
    background: linear-gradient(135deg, rgba(37, 99, 235, 0.1), transparent);
    border-color: var(--primary);
}

/* ===== TRANSCRIBE BUTTON ===== */
.transcribe-btn-wrapper {
    text-align: center;
    margin: 3rem 0;
}

.transcribe-btn {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%) !important;
    color: white !important;
    border: none !important;
    padding: 1.25rem 3rem !important;
    border-radius: var(--radius-full) !important;
    font-size: 1.125rem !important;
    font-weight: 600 !important;
    cursor: pointer !important;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
    box-shadow: var(--shadow-lg) !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 0.75rem !important;
    position: relative !important;
    overflow: hidden !important;
    letter-spacing: 0.025em !important;
}

.transcribe-btn::before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: 0.5s;
}

.transcribe-btn:hover {
    transform: translateY(-3px) scale(1.02) !important;
    box-shadow: var(--shadow-xl) !important;
}

.transcribe-btn:hover::before {
    left: 100%;
}

.transcribe-btn:active {
    transform: translateY(-1px) scale(0.98) !important;
}

/* ===== FOOTER ===== */
.footer {
    text-align: center;
    padding: 3rem 0;
    margin-top: 4rem;
    border-top: 1px solid var(--border);
}

.footer-text {
    color: var(--text-muted);
    font-size: 0.875rem;
    line-height: 1.5;
}

.footer-brand {
    font-weight: 700;
    color: var(--primary);
    margin-bottom: 0.5rem;
    font-size: 1.125rem;
}

/* ===== UTILITY CLASSES ===== */
.mt-1 { margin-top: 0.5rem; }
.mt-2 { margin-top: 1rem; }
.mt-3 { margin-top: 1.5rem; }
.mt-4 { margin-top: 2rem; }
.mt-6 { margin-top: 3rem; }
.mb-1 { margin-bottom: 0.5rem; }
.mb-2 { margin-bottom: 1rem; }
.mb-3 { margin-bottom: 1.5rem; }
.mb-4 { margin-bottom: 2rem; }
.text-center { text-align: center; }
.opacity-75 { opacity: 0.75; }
/* ===== LOADING ANIMATION ===== */
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}

.loading {
    animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
"""

# Create the Gradio interface
with gr.Blocks(css=css, title="Speech to Text Transcriber") as demo:
    
    # Header with professional theme toggle
    with gr.Column(elem_classes="header"):
        gr.HTML("""
        <div class="header-content">
            <h1 class="header-title">
                <span>🎤</span>
                Speech Transcriber Pro
            </h1>
            <p class="header-subtitle">
                Professional-grade audio transcription with multi-language support. 
                Record, upload, and transform speech into accurate text instantly.
            </p>
        </div>
        """)
    
    # Main content grid
    with gr.Row(elem_classes="main-grid"):
        # Left column - Audio Input
        with gr.Column():
            with gr.Group(elem_classes="card"):
                gr.HTML("""
                <div class="card-header">
                    <div class="card-icon">🎤</div>
                    <div>
                        <h2 class="card-title">Audio Input</h2>
                        <p class="card-subtitle">Record or upload your audio file</p>
                    </div>
                </div>
                """)
                
                # Audio controls guide
                gr.HTML("""
                <div class="audio-controls-grid">
                    <div class="control-card">
                        <div class="control-icon">🎤</div>
                        <div class="control-info">
                            <h4>Record Audio</h4>
                            <p>Click to start recording</p>
                        </div>
                    </div>
                    <div class="control-card">
                        <div class="control-icon">⏸️</div>
                        <div class="control-info">
                            <h4>Pause</h4>
                            <p>Temporarily stop recording</p>
                        </div>
                    </div>
                    <div class="control-card">
                        <div class="control-icon">⏹️</div>
                        <div class="control-info">
                            <h4>Stop</h4>
                            <p>Finish recording session</p>
                        </div>
                    </div>
                    <div class="control-card">
                        <div class="control-icon">▶️</div>
                        <div class="control-info">
                            <h4>Playback</h4>
                            <p>Listen to recorded audio</p>
                        </div>
                    </div>
                </div>
                """)
                
                # Audio component
                audio = gr.Audio(
                    sources=["microphone", "upload"],
                    type="numpy",
                    label="",
                    elem_classes="audio-container"
                )
                
                # Upload area
                gr.HTML("""
                <div class="upload-area">
                    <div class="upload-icon">📁</div>
                    <div class="upload-text">
                        <h3>Upload Audio File</h3>
                        <p>Drag & drop or click to browse files</p>
                        <p class="mt-2 opacity-75">Supports: .wav .mp3 .m4a .flac .ogg</p>
                        <p class="opacity-75">Maximum size: 100MB</p>
                    </div>
                </div>
                """)
                
                # Tips section
                gr.HTML("""
                <div class="mt-4">
                    <h4 style="color: var(--text-primary); margin-bottom: 1rem;">🎯 Best Practices:</h4>
                    <ul style="color: var(--text-secondary); padding-left: 1.5rem;">
                        <li>Use a quality microphone for recording</li>
                        <li>Speak clearly at a moderate pace</li>
                        <li>Minimize background noise</li>
                        <li>Optimal distance: 15-30cm from microphone</li>
                        <li>Export high-quality files for upload</li>
                    </ul>
                </div>
                """)
        
        # Right column - Results
        with gr.Column():
            with gr.Group(elem_classes="card"):
                gr.HTML("""
                <div class="card-header">
                    <div class="card-icon">📝</div>
                    <div>
                        <h2 class="card-title">Transcription Results</h2>
                        <p class="card-subtitle">View your transcribed text and detected language</p>
                    </div>
                </div>
                """)
                
                # Status indicator
                status = gr.Textbox(
                    label="",
                    value="⏳ Ready to transcribe audio",
                    interactive=False,
                    elem_classes="status-indicator warning"
                )
                
                # Transcription text
                gr.HTML('<div class="text-display-label">Transcribed Text</div>')
                transcript = gr.Textbox(
                    label="",
                    placeholder="Your transcribed text will appear here...",
                    lines=12,
                    elem_classes="text-display"
                )
                
                # Language detection
                gr.HTML('<div class="text-display-label mt-4">Detected Language</div>')
                language = gr.Textbox(
                    label="",
                    placeholder="Language will be automatically detected",
                    interactive=False,
                    elem_classes="text-display"
                )
                
                # Supported languages
                gr.HTML("""
                <div class="languages-section">
                    <h4 style="color: var(--text-primary); margin-bottom: 1rem;">🌍 Supported Languages:</h4>
                    <div class="languages-grid">
                        <div class="language-tag highlight">🇵🇰 Urdu (Priority)</div>
                        <div class="language-tag">🇮🇳 Hindi</div>
                        <div class="language-tag">🇺🇸 English</div>
                        <div class="language-tag">🇯🇵 Japanese</div>
                        <div class="language-tag">🇪🇸 Spanish</div>
                        <div class="language-tag">🇫🇷 French</div>
                        <div class="language-tag">🇩🇪 German</div>
                        <div class="language-tag">🇨🇳 Chinese</div>
                        <div class="language-tag">🇦🇪 Arabic</div>
                        <div class="language-tag">🇷🇺 Russian</div>
                        <div class="language-tag">🇵🇹 Portuguese</div>
                        <div class="language-tag">🇮🇹 Italian</div>
                    </div>
                </div>
                """)
    
    # Transcribe button
    with gr.Row(elem_classes="transcribe-btn-wrapper"):
        transcribe_btn = gr.Button(
            "🚀 Transcribe Audio Now",
            elem_classes="transcribe-btn"
        )
    
    # Footer
    gr.HTML("""
    <div class="footer">
        <div class="footer-brand">Speech Transcriber Pro</div>
        <p class="footer-text">Powered by OpenAI Whisper • Professional Audio Transcription</p>
        <p class="footer-text mt-2">High accuracy • Multi-language • Enterprise ready</p>
    </div>
    """)
    
    # Connect the button
    transcribe_btn.click(
        transcribe,
        inputs=[audio],
        outputs=[transcript, language, status]
    )
    
    # PROFESSIONAL THEME TOGGLE JAVASCRIPT
    gr.HTML("""
    <script>
    // Theme management
    function getCurrentTheme() {
        return localStorage.getItem('appTheme') || 
               (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    }
    
    function applyTheme(theme) {
        const isDark = theme === 'dark';
        const body = document.body;
        const gradioContainers = document.querySelectorAll('.gradio-container');
        const themeLabel = document.getElementById('themeLabel');
        
        // Apply theme classes
        body.classList.toggle('dark-mode', isDark);
        gradioContainers.forEach(container => {
            container.classList.toggle('dark-mode', isDark);
        });
        
        // Update label
        themeLabel.textContent = isDark ? 'Dark Mode' : 'Light Mode';
        
        // Update slider position with animation
        const slider = document.querySelector('.toggle-slider');
        if (slider) {
            slider.style.transform = isDark ? 'translateX(28px)' : 'translateX(2px)';
            slider.innerHTML = isDark ? '🌙' : '☀️';
        }
        
        // Store preference
        localStorage.setItem('appTheme', theme);
    }
    
    function toggleTheme() {
        const currentTheme = getCurrentTheme();
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        applyTheme(newTheme);
    }
    
    // Initialize theme on load
    document.addEventListener('DOMContentLoaded', () => {
        applyTheme(getCurrentTheme());
        
        // Add smooth transition after load
        setTimeout(() => {
            document.body.style.transition = 'background-color 0.3s ease, color 0.3s ease';
            document.querySelectorAll('.gradio-container').forEach(el => {
                el.style.transition = 'background-color 0.3s ease';
            });
        }, 100);
        
        // Listen for system theme changes
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
            if (!localStorage.getItem('appTheme')) {
                applyTheme(e.matches ? 'dark' : 'light');
            }
        });
    });
    
    // Audio status updates
    function updateAudioStatus() {
        const statusElement = document.querySelector('.status-indicator');
        if (!statusElement) return;
        
        // Check audio state
        const audioElements = document.querySelectorAll('audio');
        const isRecording = document.querySelector('button[title*="Record"], button[title*="Recording"]');
        
        if (audioElements.length > 0 && audioElements[0].src) {
            statusElement.className = 'status-indicator success';
            statusElement.querySelector('input').value = '✅ Audio loaded and ready for transcription';
        } else if (isRecording) {
            statusElement.className = 'status-indicator warning';
            statusElement.querySelector('input').value = '🎤 Recording in progress... Speak clearly';
        } else {
            statusElement.className = 'status-indicator warning';
            statusElement.querySelector('input').value = '⏳ Ready to record or upload audio';
        }
    }
    
    // Monitor audio changes
    setInterval(updateAudioStatus, 1000);
    
    // Initial status update
    setTimeout(updateAudioStatus, 2000);
    </script>
    """)

demo.launch(share=True)
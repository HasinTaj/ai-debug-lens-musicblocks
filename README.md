# 🎵 AI Debug Lens for Music Blocks

An **AI-powered debugger** that analyzes block-based compositions created with [Music Blocks](https://musicblocks.sugarlabs.org/) and detects potential bugs, logical issues, and musical inconsistencies in real-time.

> 🎯 Proposed for GSoC 2025 with Sugar Labs

## 💡 Idea

Music Blocks is a creative platform for learning music and programming. However, beginners may unintentionally create problematic logic such as:
- Infinite loops (e.g., `repeat 0`)
- Out-of-scale pitches
- Extremely low/high tempos
- Redundant or unreachable blocks

**AI Debug Lens** is designed to:
- Analyze the JSON representation of Music Blocks
- Flag common logic errors
- (Future) Use ML to detect musical pattern anomalies and suggest improvements

## ⚙️ Features (Prototype)

- ✅ Rule-based debugging of block logic
- ✅ JSON-based Music Block analysis
- 🔜 Transformer model to detect patterns and recommend enhancements

## 📦 Files

| File | Purpose |
|------|---------|
| `ai_debug_lens_prototype.py` | Core analysis script |
| `block_examples/sample_block.json` | Sample Music Block composition |
| `images/ai_debug_architecture.png` | Architecture overview |

## 🧪 Run It

```bash
python ai_debug_lens_prototype.py
```

## 🧠 Sample Output

```
Issue in Block 1: Warning: Infinite loop detected
Issue in Block 2: Warning: Tempo too low, may result in inaudible playback
Issue in Block 3: Note outside musical scale
```

## 🖼️ Architecture

![AI Debug Lens Architecture](images/ai_debug_architecture.png)

## 🙋‍♂️ Author

- 👨‍💻 Hasintaj
- 🏷️ GSoC 2025 Aspirant @ Sugar Labs
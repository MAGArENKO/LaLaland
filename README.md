lets add blender complete documentation, community, add-ons, extensions,source code,everything needs to be igdesred  to but before that naurokuros repositories in github , eguidebg@gmail.com v arrena lm, gemini, chatgpt i localnite mi hardowe  аз ще дам на срейпърите пълен достъп https://cursor.com/docs/cli/headless
https://openusd.org/release/index.html#https://huggingface.co/dataset 

https://huggingface.co/datasets
https://huggingface.co/datasets/nvidia/PhysicalAI-Robotics-NuRec
https://github.com/PixarAnimationStudios/OpenUSD/blob/release/BUILDING.md
https://lmarena.ai/c/019b6f86-867a-7332-8a9e-e389e540c282
Stay updated on frontier AI capabilities

New Chat
Leaderboard
Today

https://openusd.org/release/intro.html#what-is-usd
https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://cursor.com/docs/cli/overvi
CAN AGENT WORK DIREECTLY WIYH https://openusd.org/release/intro.html#what-is-usd OR NEEDS TOOLS
https://openusd.org/release/intro.html#what-is-usd WHAT IDE CAN MY AGENTS USE TO CREATE
Define USD concept
Since you are applying for a Startup Grant, the visuals need to look innovative, expensive, and func
INKSCAPE BLENDER ADOBE
датайлно проучване за възможностите за оидобрчване комуникацията с агента на жисуал студио и генерир
Yesterday

Argilla data curation platform
Компетентностен модел, иновации и информационна среда в агенция за пручвания и анализ на данни СЪДЪР
ДОКЛАД: Компетентностен модел, иновации и информационна среда в съвременната маркетинг агенция (дета
КАКВИ СА пълните и РЕАЛНИТЕ ОИЗНАНИЯ КОИТО ТРЯБВА ДА ПИТЕЖАВАТ СЛУЖИТЕЛИТЕ В В ПЪЛНОЦЕННА РАБОТЕЩА с
examine and wrire for visual studio . devide in grouts
--- cagent installed - See the installation guide API key configured - Set ANTHROPIC_API_KEY or OPEN
i need to make a use https://github.com/namurokuro/argilla-cookbook to make a self sustaining scrapi
STOP
Older

i did a cloning disk process and was attacked by hackers i stooped the process traing to prevent at
what format are restore points and backup files in cursor
can you help to cofigure container for my drive cBind-mounting over existing data If you bind mount
i want to analize my project communication architecture infrastructure simply fay and enhance it my

Terms of Use
Privacy Policy

claude-opus-4-5-20251101-thinking-32k
Expanding the AI Creative Pipeline

Based on the playlist you're sharing, it looks like you're building a comprehensive AI-driven content creation system.
What's the video covering?

Could be one of these topics:
Possible Topic	Integration Point
ComfyUI Workflows	Texture/concept generation
Krita AI Plugins	AI-assisted painting
Blender Automation	Scripted rendering
Stable Diffusion	Image generation backend
Current Pipeline Summary

text

┌─────────────────────────────────────────────────────────────────┐
│                        CURSOR IDE                               │
│                   (AI Agent / Orchestrator)                     │
└─────────────────────────────┬───────────────────────────────────┘
                              │
         ┌────────────────────┼────────────────────┐
         ▼                    ▼                    ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│    COMFYUI      │  │     KRITA       │  │    OpenUSD      │
│                 │  │                 │  │                 │
│ • Textures      │  │ • Paint-overs   │  │ • Scenes        │
│ • Concepts      │  │ • Touch-ups     │  │ • Materials     │
│ • ControlNet    │  │ • AI Plugins    │  │ • VFX Elements  │
│ • Upscaling     │  │ • Batch Export  │  │ • Lighting      │
└────────┬────────┘  └────────┬────────┘  └────────┬────────┘
         │                    │                    │
         └────────────────────┴────────────────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │      BLENDER CLI       │
                 │                        │
                 │  • USD Import          │
                 │  • Apply Textures      │
                 │  • Render (Cycles)     │
                 │  • Compositing         │
                 └────────────────────────┘
                              │
                              ▼
                       Final Output

Tell Me More

What does the video cover? I can help integrate:

    Specific ComfyUI nodes/workflows
    Krita plugin automation
    Advanced USD schemas
    Blender compositor scripting

Just let me know what you're aiming to add! 🎬

https://www.youtube.com/watch?v=vNryKL0POng&list=PLzw3YtsHipodetyJ9NQatDsFRaGo8FHbN&index=52
claude-opus-4-5-20251101-thinking-32k
Complete AI Creative Pipeline
Full Stack Integration

text

┌────────────────────────────────────────────────────────────────┐
│                      CURSOR IDE                                │
│                 (AI Code/Script Generation)                    │
└───────────────────────────┬────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   COMFYUI    │    │    KRITA     │    │   OpenUSD    │
│  Textures    │    │   Painting   │    │   Scenes     │
│  Concepts    │    │   Textures   │    │   Shaders    │
└──────┬───────┘    └──────┬───────┘    └──────┬───────┘
       │                   │                   │
       └───────────────────┴───────────────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │    BLENDER CLI        │
               │   Final Compositing   │
               │      & Render         │
               └───────────────────────┘

ComfyUI Setup

Bash

# Clone ComfyUI
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# Install dependencies
pip install -r requirements.txt

# Run headless (API mode)
python main.py --listen --port 8188

ComfyUI API for Texture Generation

Python

import requests
import json

workflow = {
    "prompt": {
        "3": {
            "class_type": "KSampler",
            "inputs": {
                "seed": 42,
                "steps": 20,
                "cfg": 7,
                "sampler_name": "euler",
                "scheduler": "normal",
                "denoise": 1,
                "model": ["4", 0],
                "positive": ["6", 0],
                "negative": ["7", 0],
                "latent_image": ["5", 0]
            }
        },
        # ... workflow nodes
    }
}

# Generate texture via API
response = requests.post(
    "http://127.0.0.1:8188/prompt",
    json={"prompt": workflow}
)

Krita Setup

Bash

# Install Krita
sudo apt install krita

# Krita CLI for batch processing
krita --export input.kra --export-filename output.png

Krita Scripting (Python)

Python

# krita_texture_script.py
from krita import *

def create_material_texture():
    doc = Krita.instance().createDocument(
        2048, 2048, "AI_Texture", "RGBA", "U8", "", 300
    )
    
    # Add layers
    root = doc.rootNode()
    paint_layer = doc.createNode("Diffuse", "paintlayer")
    root.addChildNode(paint_layer, None)
    
    # Export
    doc.exportImage("/textures/diffuse.png", InfoObject())
    
create_material_texture()

Run Krita Script

Bash

krita --script krita_texture_script.py

Integrated Pipeline Script

Python

#!/usr/bin/env python3
# ai_vfx_full_pipeline.py

import subprocess
import requests
from pxr import Usd, UsdShade, Sdf

# ═══════════════════════════════════════════
# STEP 1: Generate Textures with ComfyUI
# ═══════════════════════════════════════════
def generate_texture(prompt, output_path):
    workflow = {
        "prompt": prompt,
        "output": output_path
    }
    requests.post("http://127.0.0.1:8188/prompt", json=workflow)
    print(f"Generated: {output_path}")

generate_texture(
    "seamless metal rust texture, 4k, PBR",
    "/textures/rust_diffuse.png"
)

# ═══════════════════════════════════════════
# STEP 2: Process in Krita (optional touch-up)
# ═══════════════════════════════════════════
subprocess.run([
    "krita",
    "--export", "/textures/rust_diffuse.png",
    "--export-filename", "/textures/rust_processed.png"
])

# ═══════════════════════════════════════════
# STEP 3: Create USD Material with Texture
# ═══════════════════════════════════════════
stage = Usd.Stage.CreateNew("textured_asset.usda")

material = UsdShade.Material.Define(stage, "/Materials/RustMetal")
shader = UsdShade.Shader.Define(stage, "/Materials/RustMetal/PBR")
shader.CreateIdAttr("UsdPreviewSurface")

# Connect texture
texture = UsdShade.Shader.Define(stage, "/Materials/RustMetal/DiffuseTex")
texture.CreateIdAttr("UsdUVTexture")
texture.CreateInput("file", Sdf.ValueTypeNames.Asset).Set("/textures/rust_processed.png")

# Link texture to shader
shader.CreateInput("diffuseColor", Sdf.ValueTypeNames.Color3f).ConnectToSource(
    texture.ConnectableAPI(), "rgb"
)

stage.Save()

# ═══════════════════════════════════════════
# STEP 4: Render in Blender
# ═══════════════════════════════════════════
subprocess.run([
    "blender", "-b",
    "--python", "render_usd.py",
    "--", "textured_asset.usda"
])

print("Pipeline complete!")

Example Use Cases
Task	Tool Chain
Generate PBR Texture	ComfyUI → Krita → USD Material → Blender
AI Concept Art	ComfyUI → Krita touchup → Reference in Blender
Procedural VFX	Cursor → USD PointInstancer → Blender render
HDRI Generation	ComfyUI Panorama → USD DomeLight → Blender
Matte Painting	ComfyUI + Krita → Blender compositor
Directory Structure

text

project/
├── scripts/
│   ├── generate_textures.py
│   ├── create_usd_scene.py
│   └── render_blender.py
├── textures/
│   ├── diffuse.png
│   ├── roughness.png
│   └── normal.png
├── usd/
│   ├── assets.usda
│   └── materials.usda
├── output/
│   └── renders/
└── comfyui_workflows/
    └── texture_workflow.json

Want me to detail:

    ComfyUI workflow JSON for specific textures?
    Krita AI plugins integration?
    Blender compositing with AI-generated elements?

and cmfi ui andd krita
claude-opus-4-5-20251101-thinking-32k
Building OpenUSD for AI Agent Pipeline
Quick Build (Recommended)

Bash

# Clone OpenUSD
git clone https://github.com/PixarAnimationStudios/OpenUSD.git
cd OpenUSD

# Install dependencies (Ubuntu/Debian)
sudo apt-get install -y \
    build-essential \
    cmake \
    python3-dev \
    libgl1-mesa-dev \
    libglu1-mesa-dev

# Build with Python support
python3 build_scripts/build_usd.py /opt/USD \
    --python \
    --tools \
    --usd-imaging

Environment Setup

Bash

# Add to ~/.bashrc
export USD_INSTALL_ROOT=/opt/USD
export PATH=$USD_INSTALL_ROOT/bin:$PATH
export PYTHONPATH=$USD_INSTALL_ROOT/lib/python:$PYTHONPATH
export LD_LIBRARY_PATH=$USD_INSTALL_ROOT/lib:$LD_LIBRARY_PATH

Verify Installation

Bash

# Test USD tools
usdcat --help
usdview --help

# Test Python bindings
python3 -c "from pxr import Usd; print('USD OK')"

Full AI Agent Architecture

text

┌─────────────────────────────────────────────────────┐
│                   CURSOR IDE                        │
│              (AI Code Generation)                   │
└───────────────────┬─────────────────────────────────┘
                    │ generates
                    ▼
┌─────────────────────────────────────────────────────┐
│              USD Python Scripts                     │
│         (Shaders, VFX, Scene Assembly)              │
└───────────────────┬─────────────────────────────────┘
                    │ processes
                    ▼
┌─────────────────────────────────────────────────────┐
│              OpenUSD (Built)                        │
│         usdcat | usdchecker | usdzip               │
└───────────────────┬─────────────────────────────────┘
                    │ exports
                    ▼
┌─────────────────────────────────────────────────────┐
│              BLENDER CLI                            │
│         --background --python render.py            │
└───────────────────┬─────────────────────────────────┘
                    │ outputs
                    ▼
              Final Renders/Assets

Example: Complete Pipeline Script

Python

#!/usr/bin/env python3
# ai_vfx_pipeline.py

from pxr import Usd, UsdGeom, UsdShade, UsdLux
import subprocess

# 1. Create USD Scene
stage = Usd.Stage.CreateNew("ai_scene.usda")
UsdGeom.SetStageUpAxis(stage, UsdGeom.Tokens.z)

# Add geometry
sphere = UsdGeom.Sphere.Define(stage, "/World/VFXElement")
sphere.GetRadiusAttr().Set(1.0)

# Add material
material = UsdShade.Material.Define(stage, "/World/EmissiveMat")
shader = UsdShade.Shader.Define(stage, "/World/EmissiveMat/Shader")
shader.CreateIdAttr("UsdPreviewSurface")
shader.CreateInput("emissiveColor", Sdf.ValueTypeNames.Color3f).Set((1, 0.5, 0))

# Add light
light = UsdLux.DomeLight.Define(stage, "/World/HDRI")

stage.Save()

# 2. Validate with USD tools
subprocess.run(["usdchecker", "ai_scene.usda"])

# 3. Send to Blender
subprocess.run([
    "blender", "-b",
    "--python", "render_usd.py",
    "--", "ai_scene.usda"
])

Want me to detail a specific part of this pipeline?

https://github.com/PixarAnimationStudios/OpenUSD/blob/release/BUILDING.md

https://www.youtube.com/watch?v=-R_JtWnI3Ds

https://github.com/PixarAnimationStudios/OpenUSD/blob/release/BUILDING.md
claude-opus-4-5-20251101-thinking-32k
AI-Powered Blender Pipeline with Cursor

You're building an AI agent workflow for automated 3D content creation!
The Stack
Component	Purpose
Cursor IDE	AI-assisted code generation
USD/Python Scripts	Scene/shader/VFX definitions
Blender CLI	Headless rendering & processing
Blender Command Line Basics

Bash

# Run a Python script in Blender
blender --background --python my_script.py

# Render a scene headlessly
blender -b scene.blend -o //output_ -f 1

# Import USD and render
blender -b --python import_usd_render.py

Example Workflow Script

Python

# import_usd_render.py
import bpy

# Clear scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Import USD generated by AI
bpy.ops.wm.usd_import(filepath="/path/to/ai_generated.usda")

# Set render settings
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.render.filepath = "/output/render.png"

# Render
bpy.ops.render.render(write_still=True)

Full Pipeline

text

Cursor AI → Generates USD/Python → Blender CLI → Rendered Output
     ↑                                              ↓
     └──────── Feedback Loop (optional) ───────────┘

Want me to create a complete example script that Cursor could generate for a specific VFX task?

curl https://cursor.com/install -fsS | bash curl https://cursor.com/install -fsS | bash https://www.youtube.com/watch?v=J_dOXs2cwys https://www.youtube.com/watch?v=pbBLFKZL080&t=101s https://docs.blender.org/manual/en/latest/advanced/command_line/index.html
claude-opus-4-5-20251101-thinking-32k
Yes! USD for Shading & VFX in Blender
Shading with USD

An AI agent can generate UsdShade material networks:

Python

#usda 1.0

def Material "MetalMaterial" {
    token outputs:surface.connect = </MetalMaterial/PBRShader.outputs:surface>
    
    def Shader "PBRShader" {
        uniform token info:id = "UsdPreviewSurface"
        color3f inputs:diffuseColor = (0.8, 0.2, 0.1)
        float inputs:metallic = 1.0
        float inputs:roughness = 0.3
        token outputs:surface
    }
}

VFX Elements Possible
Element	USD Feature	Blender Support
Materials/Shaders	UsdShade	✅ Yes
Volumes (fog, smoke)	OpenVDB fields	✅ Yes
Particles/Instances	PointInstancer	✅ Yes
Lights	UsdLux	✅ Yes
Cameras	UsdGeom Camera	✅ Yes
Animated transforms	TimeSamples	✅ Yes
Example: Point Instancer for Particles

Python

def PointInstancer "Sparks" {
    point3f[] positions = [(0,0,0), (1,2,0), (2,1,1)]
    int[] protoIndices = [0, 0, 0]
    rel prototypes = </Sparks/SparkGeo>
    
    def Sphere "SparkGeo" {
        double radius = 0.05
    }
}

Workflow

text

AI Agent → Generates USDA → Import to Blender → Render/Simulate

Want me to show a specific VFX element example (fire, debris, lights, materials)?

BUT IT CAN VE USED FOR SHADING AND CREATING VFX ELEMENTS FOR BLENDER
claude-opus-4-5-20251101-thinking-32k
Yes! AI Agents Can Use USD to Generate 3D Content
How It Works:
1. Direct Text Generation (USDA)

Since .usda files are human-readable text, an AI agent can generate valid USD code:

Python

#usda 1.0

def Xform "Room" {
    def Cube "Table" {
        double3 xformOp:translate = (0, 0.5, 0)
        double3 xformOp:scale = (2, 0.1, 1)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:scale"]
    }
}

2. Using USD Python API

Agents can programmatically build scenes:

Python

from pxr import Usd, UsdGeom

stage = Usd.Stage.CreateNew("scene.usda")
UsdGeom.Cube.Define(stage, "/MyCube")
stage.Save()

3. Integration Platforms
Platform	AI Capability
NVIDIA Omniverse	AI-assisted scene generation
Blender + USD	Scripted generation via Python
Custom Pipelines	LLM-driven procedural content
Current Limitations:

    Complex geometry still requires traditional 3D modeling or procedural methods
    AI-generated meshes (from text-to-3D models) can be exported to USD

Would you like an example of an AI agent workflow for USD generation?

CABN A TRAINED AGENT USE IT TO GENERATE CONTENT
claude-opus-4-5-20251101-thinking-32k
Universal Scene Description (USD)

You've shared a link to the OpenUSD documentation. USD (Universal Scene Description) is an open-source framework originally developed by Pixar Animation Studios for describing, composing, and exchanging 3D scene data.
Key Features of USD:
Feature	Description
Scene Composition	Layer and combine assets from multiple sources non-destructively
Collaboration	Multiple artists can work on the same scene simultaneously
Scalability	Handles massive, complex scenes efficiently
Interoperability	Industry-standard format supported by major DCC tools
Common File Extensions:

    .usda – Human-readable ASCII format
    .usdc – Binary (crate) format for performance
    .usdz – Packaged/zipped archive (used in AR/Apple ecosystem)

Industry Adoption:

USD is now supported in Maya, Houdini, Blender, Unreal Engine, Unity, NVIDIA Omniverse, Apple's Reality ecosystem, and more.

Is there something specific about USD you'd like to explore — such as:

    Composition arcs (references, payloads, variants)?
    Working with USD in a specific application?
    USD schemas or pipeline integration?

    https://openusd.org/release/intro.html#what-is-usd

Something went wrong while generating the response. Please try again.

Inputs are processed by third-party AI and responses may be inaccurate.

https://cursor.com/cli  Stay updated on frontier AI capabilities

Terms of Use
Privacy Policy

claude-opus-4-5-20251101-thinking-32k
Complete Cursor Projects Recovery System

Let me create a comprehensive system to recover ALL your old Cursor projects, including workspace data, chat history, and AI conversations.
1. Cursor Data Locations

Python

# recovery/scrapers/cursor_scraper.py
"""
COMPLETE CURSOR PROJECTS RECOVERY
Recovers all Cursor IDE projects, workspaces, chat history, and AI conversations

Cursor stores data in:
- AppData/Roaming/Cursor/
- AppData/Local/Cursor/
- .cursor/ folders in projects
- .cursor-tutor files
- Workspace storage
- Extension data
"""

import asyncio
import aiofiles
import json
import os
import sqlite3
import shutil
import tempfile
from pathlib import Path
from datetime import datetime
from typing import AsyncIterator, Dict, Any, List, Optional, Set
from dataclasses import dataclass, field
import re

from loguru import logger


@dataclass
class CursorProject:
    """Represents a Cursor project"""
    path: str
    name: str
    last_opened: Optional[datetime] = None
    workspace_file: Optional[str] = None
    has_cursor_folder: bool = False
    files: List[str] = field(default_factory=list)
    chat_history: List[Dict] = field(default_factory=list)
    ai_conversations: List[Dict] = field(default_factory=list)
    settings: Dict[str, Any] = field(default_factory=dict)


@dataclass
class CursorChat:
    """Represents a Cursor AI chat/conversation"""
    id: str
    title: Optional[str] = None
    messages: List[Dict] = field(default_factory=list)
    model: Optional[str] = None
    created_at: Optional[str] = None
    project_path: Optional[str] = None
    workspace: Optional[str] = None


@dataclass
class ScrapedItem:
    id: str
    source_type: str
    source_path: str
    content: str
    content_type: str
    filename: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    language: Optional[str] = None
    confidence_score: float = 1.0


class CursorProjectsScraper:
    """
    Comprehensive scraper for ALL Cursor IDE data.
    
    Recovers:
    1. All Cursor projects and workspaces
    2. Cursor chat/AI conversation history
    3. Cursor settings and configurations
    4. Extension data
    5. Workspace storage
    6. Recent files and folders
    7. .cursor folders in all projects
    """
    
    def __init__(self, username: str = "eguid"):
        self.username = username
        self.cursor_paths = self._get_cursor_paths()
        
        # Storage
        self.projects: List[CursorProject] = []
        self.chats: List[CursorChat] = []
        self.processed_paths: Set[str] = set()
        
    def _get_cursor_paths(self) -> Dict[str, List[Path]]:
        """Get all Cursor data locations"""
        
        appdata_roaming = Path(f"C:/Users/{self.username}/AppData/Roaming")
        appdata_local = Path(f"C:/Users/{self.username}/AppData/Local")
        
        return {
            # Main Cursor directories
            "cursor_roaming": [
                appdata_roaming / "Cursor",
                appdata_roaming / "cursor",
            ],
            "cursor_local": [
                appdata_local / "Cursor",
                appdata_local / "cursor",
            ],
            
            # User data directories
            "user_data": [
                appdata_roaming / "Cursor" / "User",
                appdata_local / "Cursor" / "User Data",
                appdata_local / "Cursor" / "User Data" / "Default",
            ],
            
            # Workspace storage
            "workspace_storage": [
                appdata_roaming / "Cursor" / "User" / "workspaceStorage",
                appdata_local / "Cursor" / "User Data" / "Default" / "Workspaces",
            ],
            
            # Global storage (chat history, settings)
            "global_storage": [
                appdata_roaming / "Cursor" / "User" / "globalStorage",
                appdata_local / "Cursor" / "User Data" / "Default" / "Local Storage",
            ],
            
            # State and history
            "state": [
                appdata_roaming / "Cursor" / "User" / "History",
                appdata_roaming / "Cursor" / "User" / "Backups",
                appdata_roaming / "Cursor" / "User" / "sync",
            ],
            
            # Extension data
            "extensions": [
                appdata_roaming / "Cursor" / "User" / "extensions",
                appdata_local / "Cursor" / "extensions",
            ],
            
            # Cache and logs (may contain useful data)
            "cache": [
                appdata_local / "Cursor" / "Cache",
                appdata_local / "Cursor" / "Code Cache",
                appdata_local / "Cursor" / "GPUCache",
            ],
            
            # Logs
            "logs": [
                appdata_roaming / "Cursor" / "logs",
                appdata_local / "Cursor" / "logs",
            ],
            
            # Possible project locations to scan
            "project_locations": [
                Path(f"C:/Users/{self.username}/Documents"),
                Path(f"C:/Users/{self.username}/Desktop"),
                Path(f"C:/Users/{self.username}/Projects"),
                Path(f"C:/Users/{self.username}/Code"),
                Path(f"C:/Users/{self.username}/dev"),
                Path(f"C:/Users/{self.username}/workspace"),
                Path(f"C:/Users/{self.username}/repos"),
                Path(f"C:/Users/{self.username}/git"),
                Path(f"C:/Users/{self.username}/OneDrive/Desktop"),
                Path(f"C:/Users/{self.username}/OneDrive/Documents"),
                Path("G:/restored"),
                Path("G:/"),
                Path("D:/"),
                Path("E:/"),
            ],
            
            # WSL paths
            "wsl_paths": [
                Path(f"\\\\wsl.localhost\\Ubuntu\\home\\{self.username}"),
                Path(f"\\\\wsl$\\Ubuntu\\home\\{self.username}"),
            ],
        }
    
    async def scrape_all(self) -> AsyncIterator[ScrapedItem]:
        """Scrape ALL Cursor data"""
        
        logger.info("=" * 60)
        logger.info("CURSOR PROJECTS COMPLETE RECOVERY")
        logger.info("=" * 60)
        
        # 1. Extract recent projects from Cursor state
        logger.info("\n[1/7] Extracting recent projects list...")
        async for item in self._extract_recent_projects():
            yield item
        
        # 2. Extract chat/AI conversation history
        logger.info("\n[2/7] Extracting Cursor AI chat history...")
        async for item in self._extract_chat_history():
            yield item
        
        # 3. Extract workspace storage
        logger.info("\n[3/7] Extracting workspace storage...")
        async for item in self._extract_workspace_storage():
            yield item
        
        # 4. Extract global storage (settings, state)
        logger.info("\n[4/7] Extracting global storage...")
        async for item in self._extract_global_storage():
            yield item
        
        # 5. Scan for .cursor folders in all project locations
        logger.info("\n[5/7] Scanning for .cursor folders in projects...")
        async for item in self._scan_cursor_folders():
            yield item
        
        # 6. Extract from SQLite databases
        logger.info("\n[6/7] Extracting from SQLite databases...")
        async for item in self._extract_sqlite_data():
            yield item
        
        # 7. Extract extension data
        logger.info("\n[7/7] Extracting extension data...")
        async for item in self._extract_extension_data():
            yield item
        
        # Summary
        logger.info(f"\nTotal projects found: {len(self.projects)}")
        logger.info(f"Total chats found: {len(self.chats)}")
    
    async def _extract_recent_projects(self) -> AsyncIterator[ScrapedItem]:
        """Extract list of recent projects from Cursor state files"""
        
        state_files = [
            "storage.json",
            "state.vscdb",
            "state.json",
            "recentlyOpened.json",
            "workspaces.json",
        ]
        
        for category, paths in self.cursor_paths.items():
            if category not in ["cursor_roaming", "cursor_local", "user_data", "state"]:
                continue
                
            for base_path in paths:
                if not base_path.exists():
                    continue
                
                # Search for state files
                for state_file in state_files:
                    for filepath in base_path.rglob(state_file):
                        try:
                            content = filepath.read_text(encoding='utf-8', errors='ignore')
                            
                            # Try to parse as JSON
                            try:
                                data = json.loads(content)
                                projects = self._extract_projects_from_state(data, str(filepath))
                                
                                for project in projects:
                                    if project.path not in self.processed_paths:
                                        self.processed_paths.add(project.path)
                                        self.projects.append(project)
                                        
                                        yield ScrapedItem(
                                            id=f"cursor:project:{project.name}",
                                            source_type="cursor_project",
                                            source_path=project.path,
                                            content=self._format_project_info(project),
                                            content_type="project_info",
                                            filename=f"cursor_project_{project.name}.md",
                                            metadata={
                                                "project_name": project.name,
                                                "project_path": project.path,
                                                "last_opened": str(project.last_opened) if project.last_opened else None,
                                                "has_cursor_folder": project.has_cursor_folder,
                                                "source_file": str(filepath),
                                            },
                                            confidence_score=0.95
                                        )
                            except json.JSONDecodeError:
                                # Try as vscdb (SQLite)
                                if filepath.suffix == '.vscdb':
                                    async for item in self._parse_vscdb(filepath):
                                        yield item
                                        
                        except Exception as e:
                            logger.debug(f"Error reading {filepath}: {e}")
    
    def _extract_projects_from_state(self, data: Dict, source: str) -> List[CursorProject]:
        """Extract project paths from state data"""
        projects = []
        
        # Common keys that contain project paths
        keys_to_check = [
            'openedPathsList',
            'lastKnownMenubarData',
            'windowsState',
            'recentlyOpened',
            'workspaces',
            'folders',
            'files',
            'entries',
        ]
        
        def extract_paths(obj, depth=0):
            if depth > 10:
                return
            
            if isinstance(obj, dict):
                for key, value in obj.items():
                    if key in keys_to_check or 'path' in key.lower() or 'folder' in key.lower():
                        if isinstance(value, str) and (os.path.isabs(value) or value.startswith('file://')):
                            path = value.replace('file:///', '').replace('file://', '')
                            path = path.replace('/', '\\') if '\\' not in path else path
                            
                            if os.path.exists(path) or os.path.exists(path.rstrip('\\')):
                                name = os.path.basename(path.rstrip('\\/'))
                                if name and not name.startswith('.'):
                                    projects.append(CursorProject(
                                        path=path,
                                        name=name,
                                        has_cursor_folder=os.path.exists(os.path.join(path, '.cursor'))
                                    ))
                        elif isinstance(value, list):
                            for item in value:
                                extract_paths(item, depth + 1)
                        elif isinstance(value, dict):
                            extract_paths(value, depth + 1)
                    else:
                        extract_paths(value, depth + 1)
                        
            elif isinstance(obj, list):
                for item in obj:
                    extract_paths(item, depth + 1)
        
        extract_paths(data)
        return projects
    
    async def _parse_vscdb(self, db_path: Path) -> AsyncIterator[ScrapedItem]:
        """Parse VSCode/Cursor state database"""
        
        try:
            # Copy to temp (might be locked)
            with tempfile.NamedTemporaryFile(delete=False, suffix='.db') as tmp:
                tmp_path = tmp.name
            
            shutil.copy2(db_path, tmp_path)
            
            conn = sqlite3.connect(tmp_path)
            cursor = conn.cursor()
            
            # Get all tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cursor.fetchall()]
            
            for table in tables:
                try:
                    cursor.execute(f"SELECT * FROM {table}")
                    rows = cursor.fetchall()
                    
                    # Get column names
                    cursor.execute(f"PRAGMA table_info({table})")
                    columns = [col[1] for col in cursor.fetchall()]
                    
                    for row in rows:
                        row_dict = dict(zip(columns, row))
                        
                        # Check for value column (common in key-value stores)
                        value = row_dict.get('value', '')
                        if isinstance(value, bytes):
                            value = value.decode('utf-8', errors='ignore')
                        
                        # Try to parse as JSON
                        try:
                            data = json.loads(value)
                            
                            # Check if it's chat/conversation data
                            if self._is_chat_data(data):
                                chat = self._parse_chat(data, str(db_path))
                                if chat:
                                    self.chats.append(chat)
                                    
                                    yield ScrapedItem(
                                        id=f"cursor:chat:{chat.id}",
                                        source_type="cursor_chat",
                                        source_path=str(db_path),
                                        content=self._format_chat(chat),
                                        content_type="ai_conversation",
                                        filename=f"cursor_chat_{chat.id[:16]}.md",
                                        metadata={
                                            "chat_id": chat.id,
                                            "model": chat.model,
                                            "message_count": len(chat.messages),
                                        },
                                        confidence_score=0.95
                                    )
                            
                            # Check for project data
                            projects = self._extract_projects_from_state(data, str(db_path))
                            for project in projects:
                                if project.path not in self.processed_paths:
                                    self.processed_paths.add(project.path)
                                    self.projects.append(project)
                                    
                        except json.JSONDecodeError:
                            pass
                            
                except Exception as e:
                    continue
            
            conn.close()
            os.unlink(tmp_path)
            
        except Exception as e:
            logger.debug(f"Error parsing vscdb {db_path}: {e}")
    
    async def _extract_chat_history(self) -> AsyncIterator[ScrapedItem]:
        """Extract Cursor AI chat history"""
        
        # Chat history locations
        chat_locations = [
            "globalStorage",
            "workspaceStorage",
            "User/History",
        ]
        
        for category, paths in self.cursor_paths.items():
            for base_path in paths:
                if not base_path.exists():
                    continue
                
                # Look for chat-related files
                chat_patterns = [
                    "**/*chat*.json",
                    "**/*conversation*.json",
                    "**/*history*.json",
                    "**/*ai*.json",
                    "**/*composer*.json",
                    "**/state.vscdb",
                    "**/*.sqlite",
                    "**/*.db",
                ]
                
                for pattern in chat_patterns:
                    for filepath in base_path.rglob(pattern.replace("**", "*")):
                        try:
                            if filepath.suffix in ['.json']:
                                content = filepath.read_text(encoding='utf-8', errors='ignore')
                                try:
                                    data = json.loads(content)
                                    if self._is_chat_data(data):
                                        chat = self._parse_chat(data, str(filepath))
                                        if chat and chat.id not in {c.id for c in self.chats}:
                                            self.chats.append(chat)
                                            
                                            yield ScrapedItem(
                                                id=f"cursor:chat:{chat.id}",
                                                source_type="cursor_chat",
                                                source_path=str(filepath),
                                                content=self._format_chat(chat),
                                                content_type="ai_conversation",
                                                filename=f"cursor_chat_{chat.id[:16]}.md",
                                                metadata={
                                                    "chat_id": chat.id,
                                                    "model": chat.model,
                                                    "message_count": len(chat.messages),
                                                    "source_file": str(filepath),
                                                },
                                                confidence_score=0.95
                                            )
                                except json.JSONDecodeError:
                                    pass
                                    
                            elif filepath.suffix in ['.sqlite', '.db', '.vscdb']:
                                async for item in self._parse_vscdb(filepath):
                                    yield item
                                    
                        except Exception as e:
                            logger.debug(f"Error processing {filepath}: {e}")
    
    async def _extract_workspace_storage(self) -> AsyncIterator[ScrapedItem]:
        """Extract data from workspace storage"""
        
        for base_path in self.cursor_paths.get("workspace_storage", []):
            if not base_path.exists():
                continue
            
            logger.info(f"  Scanning workspace storage: {base_path}")
            
            # Each subfolder is a workspace
            for workspace_dir in base_path.iterdir():
                if not workspace_dir.is_dir():
                    continue
                
                workspace_id = workspace_dir.name
                
                # Look for workspace.json
                workspace_json = workspace_dir / "workspace.json"
                if workspace_json.exists():
                    try:
                        data = json.loads(workspace_json.read_text())
                        folder = data.get('folder', data.get('workspace', ''))
                        
                        if folder:
                            folder_path = folder.replace('file:///', '').replace('file://', '')
                            folder_path = folder_path.replace('/', '\\')
                            
                            name = os.path.basename(folder_path.rstrip('\\/'))
                            
                            if folder_path not in self.processed_paths:
                                self.processed_paths.add(folder_path)
                                
                                project = CursorProject(
                                    path=folder_path,
                                    name=name,
                                    workspace_file=str(workspace_json),
                                    has_cursor_folder=os.path.exists(os.path.join(folder_path, '.cursor'))
                                )
                                self.projects.append(project)
                                
                                yield ScrapedItem(
                                    id=f"cursor:workspace:{workspace_id}",
                                    source_type="cursor_workspace",
                                    source_path=folder_path,
                                    content=self._format_project_info(project),
                                    content_type="workspace_info",
                                    filename=f"workspace_{name}.md",
                                    metadata={
                                        "workspace_id": workspace_id,
                                        "folder": folder_path,
                                    },
                                    confidence_score=0.9
                                )
                    except Exception as e:
                        pass
                
                # Look for state.vscdb in workspace
                state_db = workspace_dir / "state.vscdb"
                if state_db.exists():
                    async for item in self._parse_vscdb(state_db):
                        yield item
                
                # Look for other data files
                for data_file in workspace_dir.rglob("*.json"):
                    try:
                        content = data_file.read_text(encoding='utf-8', errors='ignore')
                        data = json.loads(content)
                        
                        if self._is_chat_data(data):
                            chat = self._parse_chat(data, str(data_file))
                            if chat:
                                self.chats.append(chat)
                                
                                yield ScrapedItem(
                                    id=f"cursor:workspace_chat:{chat.id}",
                                    source_type="cursor_chat",
                                    source_path=str(data_file),
                                    content=self._format_chat(chat),
                                    content_type="ai_conversation",
                                    filename=f"workspace_chat_{chat.id[:16]}.md",
                                    metadata={
                                        "workspace_id": workspace_id,
                                        "chat_id": chat.id,
                                    },
                                    confidence_score=0.9
                                )
                    except:
                        pass
    
    async def _extract_global_storage(self) -> AsyncIterator[ScrapedItem]:
        """Extract from global storage"""
        
        for base_path in self.cursor_paths.get("global_storage", []):
            if not base_path.exists():
                continue
            
            logger.info(f"  Scanning global storage: {base_path}")
            
            # Scan all files
            for filepath in base_path.rglob("*"):
                if not filepath.is_file():
                    continue
                
                try:
                    if filepath.suffix in ['.json']:
                        content = filepath.read_text(encoding='utf-8', errors='ignore')
                        
                        # Look for chat data
                        if any(term in content.lower() for term in ['message', 'chat', 'conversation', 'prompt', 'response']):
                            try:
                                data = json.loads(content)
                                
                                if self._is_chat_data(data):
                                    chat = self._parse_chat(data, str(filepath))
                                    if chat:
                                        self.chats.append(chat)
                                        
                                        yield ScrapedItem(
                                            id=f"cursor:global:{chat.id}",
                                            source_type="cursor_chat",
                                            source_path=str(filepath),
                                            content=self._format_chat(chat),
                                            content_type="ai_conversation",
                                            filename=f"global_chat_{chat.id[:16]}.md",
                                            metadata={"source_file": str(filepath)},
                                            confidence_score=0.85
                                        )
                            except json.JSONDecodeError:
                                pass
                                
                    elif filepath.suffix in ['.vscdb', '.sqlite', '.db']:
                        async for item in self._parse_vscdb(filepath):
                            yield item
                            
                    # LevelDB storage
                    elif filepath.suffix in ['.ldb', '.log']:
                        async for item in self._parse_leveldb_file(filepath):
                            yield item
                            
                except Exception as e:
                    continue
    
    async def _parse_leveldb_file(self, filepath: Path) -> AsyncIterator[ScrapedItem]:
        """Parse LevelDB file for chat data"""
        
        try:
            content = filepath.read_bytes()
            content_str = content.decode('utf-8', errors='ignore')
            
            # Look for JSON objects
            json_pattern = r'\{[^{}]*(?:"messages"|"conversation"|"chat"|"prompt")[^{}]*\}'
            
            for match in re.finditer(json_pattern, content_str, re.DOTALL):
                try:
                    data = json.loads(match.group())
                    if self._is_chat_data(data):
                        chat = self._parse_chat(data, str(filepath))
                        if chat:
                            yield ScrapedItem(
                                id=f"cursor:leveldb:{chat.id}",
                                source_type="cursor_chat",
                                source_path=str(filepath),
                                content=self._format_chat(chat),
                                content_type="ai_conversation",
                                filename=f"leveldb_chat_{chat.id[:16]}.md",
                                metadata={"source": "leveldb"},
                                confidence_score=0.75
                            )
                except:
                    continue
                    
        except Exception as e:
            pass
    
    async def _scan_cursor_folders(self) -> AsyncIterator[ScrapedItem]:
        """Scan for .cursor folders in project directories"""
        
        for category in ["project_locations", "wsl_paths"]:
            for base_path in self.cursor_paths.get(category, []):
                if not base_path.exists():
                    continue
                
                logger.info(f"  Scanning for .cursor folders: {base_path}")
                
                try:
                    # Find all .cursor folders
                    for cursor_folder in base_path.rglob(".cursor"):
                        if not cursor_folder.is_dir():
                            continue
                        
                        project_path = cursor_folder.parent
                        project_name = project_path.name
                        
                        if str(project_path) in self.processed_paths:
                            continue
                        
                        self.processed_paths.add(str(project_path))
                        
                        # Extract data from .cursor folder
                        cursor_data = await self._extract_cursor_folder_data(cursor_folder)
                        
                        project = CursorProject(
                            path=str(project_path),
                            name=project_name,
                            has_cursor_folder=True,
                            chat_history=cursor_data.get('chats', []),
                            settings=cursor_data.get('settings', {}),
                        )
                        self.projects.append(project)
                        
                        # Yield project info
                        yield ScrapedItem(
                            id=f"cursor:dotfolder:{project_name}",
                            source_type="cursor_project",
                            source_path=str(project_path),
                            content=self._format_project_info(project),
                            content_type="project_info",
                            filename=f"project_{project_name}.md",
                            metadata={
                                "project_path": str(project_path),
                                "cursor_folder": str(cursor_folder),
                            },
                            confidence_score=1.0
                        )
                        
                        # Yield any chats found
                        for chat_data in cursor_data.get('chats', []):
                            yield ScrapedItem(
                                id=f"cursor:project_chat:{project_name}:{chat_data.get('id', 'unknown')}",
                                source_type="cursor_chat",
                                source_path=str(cursor_folder),
                                content=json.dumps(chat_data, indent=2),
                                content_type="ai_conversation",
                                filename=f"project_{project_name}_chat.json",
                                metadata={"project": project_name},
                                confidence_score=1.0
                            )
                        
                        # Also scan project files for code
                        async for item in self._scan_project_files(project_path):
                            yield item
                            
                except PermissionError:
                    continue
                except Exception as e:
                    logger.debug(f"Error scanning {base_path}: {e}")
    
    async def _extract_cursor_folder_data(self, cursor_folder: Path) -> Dict[str, Any]:
        """Extract data from a .cursor folder"""
        
        data = {
            "chats": [],
            "settings": {},
            "rules": [],
        }
        
        try:
            # Check for common files
            files_to_check = [
                "chat.json",
                "chats.json",
                "history.json",
                "state.json",
                "settings.json",
                "rules",
                ".cursorrules",
            ]
            
            for filename in files_to_check:
                filepath = cursor_folder / filename
                if filepath.exists():
                    try:
                        content = filepath.read_text(encoding='utf-8', errors='ignore')
                        
                        if filename in ["rules", ".cursorrules"]:
                            data["rules"].append(content)
                        else:
                            try:
                                json_data = json.loads(content)
                                if "chat" in filename or "history" in filename:
                                    if isinstance(json_data, list):
                                        data["chats"].extend(json_data)
                                    else:
                                        data["chats"].append(json_data)
                                else:
                                    data["settings"].update(json_data)
                            except json.JSONDecodeError:
                                pass
                    except:
                        pass
            
            # Scan all JSON files in .cursor
            for json_file in cursor_folder.rglob("*.json"):
                try:
                    content = json.loads(json_file.read_text(encoding='utf-8', errors='ignore'))
                    if self._is_chat_data(content):
                        data["chats"].append(content)
                except:
                    pass
                    
        except Exception as e:
            logger.debug(f"Error extracting .cursor data: {e}")
        
        return data
    
    async def _scan_project_files(self, project_path: Path) -> AsyncIterator[ScrapedItem]:
        """Scan project files for source code"""
        
        code_extensions = {
            '.py', '.js', '.ts', '.jsx', '.tsx', '.java', '.cpp', '.c', '.h',
            '.go', '.rs', '.rb', '.php', '.swift', '.kt', '.scala',
            '.sql', '.html', '.css', '.scss', '.vue', '.svelte',
            '.json', '.yaml', '.yml', '.toml', '.md', '.sh', '.bash',
        }
        
        exclude_dirs = {
            'node_modules', '__pycache__', '.git', 'venv', '.venv',
            'dist', 'build', 'target', '.next', '.nuxt'
        }
        
        try:
            for root, dirs, files in os.walk(project_path):
                # Filter directories
                dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.')]
                
                for filename in files:
                    filepath = Path(root) / filename
                    
                    if filepath.suffix.lower() not in code_extensions:
                        continue
                    
                    try:
                        if filepath.stat().st_size > 1024 * 1024:  # Skip files > 1MB
                            continue
                        
                        content = filepath.read_text(encoding='utf-8', errors='ignore')
                        
                        # Check if it's interesting code (agents, schemas, etc.)
                        if self._is_interesting_code(content):
                            yield ScrapedItem(
                                id=f"cursor:file:{filepath.as_posix()}",
                                source_type="cursor_file",
                                source_path=str(filepath),
                                content=content,
                                content_type="source_code",
                                filename=filepath.name,
                                language=self._detect_language(filepath.suffix),
                                metadata={
                                    "project": project_path.name,
                                    "relative_path": str(filepath.relative_to(project_path)),
                                },
                                confidence_score=0.8
                            )
                    except:
                        continue
                        
        except Exception as e:
            pass
    
    def _is_interesting_code(self, content: str) -> bool:
        """Check if code contains interesting patterns"""
        patterns = [
            'class.*Agent',
            'BaseAgent',
            'execute_task',
            'get_tools',
            'CREATE TABLE',
            'async def',
            'SYSTEM_PROMPT',
            'mcp_server',
            'bpy.ops',
            'workflow',
        ]
        
        return any(re.search(pattern, content, re.IGNORECASE) for pattern in patterns)
    
    async def _extract_sqlite_data(self) -> AsyncIterator[ScrapedItem]:
        """Extract from all SQLite databases"""
        
        for category, paths in self.cursor_paths.items():
            for base_path in paths:
                if not base_path.exists():
                    continue
                
                for db_file in base_path.rglob("*.sqlite"):
                    async for item in self._parse_vscdb(db_file):
                        yield item
                
                for db_file in base_path.rglob("*.db"):
                    async for item in self._parse_vscdb(db_file):
                        yield item
                
                for db_file in base_path.rglob("*.vscdb"):
                    async for item in self._parse_vscdb(db_file):
                        yield item
    
    async def _extract_extension_data(self) -> AsyncIterator[ScrapedItem]:
        """Extract data from Cursor extensions"""
        
        for base_path in self.cursor_paths.get("extensions", []):
            if not base_path.exists():
                continue
            
            # Look for extension data that might contain chat history
            for ext_dir in base_path.iterdir():
                if not ext_dir.is_dir():
                    continue
                
                # Check for relevant extensions
                ext_name = ext_dir.name.lower()
                if any(term in ext_name for term in ['chat', 'ai', 'copilot', 'gpt', 'claude']):
                    for json_file in ext_dir.rglob("*.json"):
                        try:
                            content = json_file.read_text(encoding='utf-8', errors='ignore')
                            data = json.loads(content)
                            
                            if self._is_chat_data(data):
                                chat = self._parse_chat(data, str(json_file))
                                if chat:
                                    yield ScrapedItem(
                                        id=f"cursor:ext:{ext_name}:{chat.id}",
                                        source_type="cursor_extension",
                                        source_path=str(json_file),
                                        content=self._format_chat(chat),
                                        content_type="ai_conversation",
                                        filename=f"ext_{ext_name}_chat.md",
                                        metadata={"extension": ext_name},
                                        confidence_score=0.8
                                    )
                        except:
                            continue
    
    # =========================================================================
    # Helper Methods
    # =========================================================================
    
    def _is_chat_data(self, data: Any) -> bool:
        """Check if data looks like chat data"""
        if not isinstance(data, dict):
            if isinstance(data, list) and len(data) > 0:
                return self._is_chat_data(data[0])
            return False
        
        indicators = [
            'messages' in data,
            'conversation' in data,
            'chat' in data,
            'prompt' in data and 'response' in data,
            'role' in data and 'content' in data,
            'user' in data and 'assistant' in data,
        ]
        
        return any(indicators)
    
    def _parse_chat(self, data: Dict, source: str) -> Optional[CursorChat]:
        """Parse chat data into CursorChat object"""
        try:
            # Generate ID
            chat_id = data.get('id', data.get('chatId', self._generate_id(str(data))))
            
            # Extract messages
            messages = []
            msg_data = data.get('messages', data.get('conversation', data.get('chat', [])))
            
            if isinstance(msg_data, list):
                for msg in msg_data:
                    if isinstance(msg, dict):
                        messages.append({
                            'role': msg.get('role', msg.get('sender', 'unknown')),
                            'content': msg.get('content', msg.get('message', msg.get('text', ''))),
                            'model': msg.get('model'),
                        })
            
            if not messages:
                # Try single message format
                if 'prompt' in data and 'response' in data:
                    messages = [
                        {'role': 'user', 'content': data['prompt']},
                        {'role': 'assistant', 'content': data['response']},
                    ]
            
            if not messages:
                return None
            
            return CursorChat(
                id=str(chat_id),
                messages=messages,
                model=data.get('model'),
                created_at=data.get('createdAt', data.get('timestamp')),
            )
            
        except Exception as e:
            return None
    
    def _format_project_info(self, project: CursorProject) -> str:
        """Format project info as markdown"""
        lines = [
            f"# Cursor Project: {project.name}",
            "",
            f"**Path:** `{project.path}`",
            f"**Has .cursor folder:** {project.has_cursor_folder}",
        ]
        
        if project.last_opened:
            lines.append(f"**Last opened:** {project.last_opened}")
        
        if project.workspace_file:
            lines.append(f"**Workspace file:** `{project.workspace_file}`")
        
        if project.chat_history:
            lines.append(f"\n## Chat History\n")
            lines.append(f"Found {len(project.chat_history)} conversations")
        
        return "\n".join(lines)
    
    def _format_chat(self, chat: CursorChat) -> str:
        """Format chat as markdown"""
        lines = [
            f"# Cursor AI Conversation",
            "",
            f"**ID:** `{chat.id}`",
        ]
        
        if chat.model:
            lines.append(f"**Model:** {chat.model}")
        
        if chat.created_at:
            lines.append(f"**Created:** {chat.created_at}")
        
        lines.append(f"**Messages:** {len(chat.messages)}")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        for msg in chat.messages:
            role = msg.get('role', 'unknown').upper()
            content = msg.get('content', '')
            model = msg.get('model', '')
            
            model_info = f" ({model})" if model else ""
            lines.append(f"## {role}{model_info}")
            lines.append("")
            lines.append(content)
            lines.append("")
        
        return "\n".join(lines)
    
    def _detect_language(self, extension: str) -> str:
        """Detect language from extension"""
        ext_map = {
            '.py': 'python',
            '.js': 'javascript',
            '.ts': 'typescript',
            '.jsx': 'javascript',
            '.tsx': 'typescript',
            '.java': 'java',
            '.cpp': 'cpp',
            '.c': 'c',
            '.go': 'go',
            '.rs': 'rust',
            '.rb': 'ruby',
            '.sql': 'sql',
            '.html': 'html',
            '.css': 'css',
            '.json': 'json',
            '.yaml': 'yaml',
            '.yml': 'yaml',
            '.md': 'markdown',
            '.sh': 'bash',
        }
        return ext_map.get(extension.lower(), 'text')
    
    def _generate_id(self, content: str) -> str:
        """Generate unique ID from content"""
        import hashlib
        return hashlib.sha256(content.encode()).hexdigest()[:24]
    
    def get_summary(self) -> Dict[str, Any]:
        """Get summary of all found data"""
        return {
            "total_projects": len(self.projects),
            "total_chats": len(self.chats),
            "projects": [
                {
                    "name": p.name,
                    "path": p.path,
                    "has_cursor": p.has_cursor_folder,
                }
                for p in self.projects
            ],
            "chat_count_by_model": self._count_by_model(),
        }
    
    def _count_by_model(self) -> Dict[str, int]:
        """Count chats by model"""
        counts = {}
        for chat in self.chats:
            model = chat.model or 'unknown'
            counts[model] = counts.get(model, 0) + 1
        return counts

2. Complete Recovery Script

Python

# scripts/recover_cursor_projects.py
"""
COMPLETE CURSOR PROJECTS RECOVERY

Recovers ALL Cursor IDE data including:
- All projects and workspaces
- All AI chat history
- All .cursor folder data
- All code from projects
"""

import asyncio
import sys
import json
from pathlib import Path
from datetime import datetime

# Add project root
sys.path.insert(0, str(Path(__file__).parent.parent))

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.table import Table
from rich.panel import Panel
from rich.tree import Tree

from recovery.scrapers.cursor_scraper import CursorProjectsScraper, ScrapedItem

console = Console()


class CursorRecovery:
    """Complete Cursor projects recovery"""
    
    def __init__(self, username: str = "eguid"):
        self.username = username
        self.output_dir = Path(f"C:/Users/{username}/Desktop/CLAUDE RECOMENDATIONS/recovered/cursor")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.scraper = CursorProjectsScraper(username)
        
        # Storage
        self.items: list = []
        self.projects_found = 0
        self.chats_found = 0
        self.code_files_found = 0
    
    async def run(self):
        """Run complete recovery"""
        
        console.print(Panel.fit(
            "[bold magenta]🔮 CURSOR PROJECTS COMPLETE RECOVERY[/bold magenta]\n\n"
            "Scanning for:\n"
            "  • All Cursor projects & workspaces\n"
            "  • All AI chat history\n"
            "  • All .cursor folder data\n"
            "  • All source code from projects\n\n"
            f"Output: {self.output_dir}",
            border_style="magenta"
        ))
        
        # Create output directories
        (self.output_dir / "projects").mkdir(exist_ok=True)
        (self.output_dir / "chats").mkdir(exist_ok=True)
        (self.output_dir / "code").mkdir(exist_ok=True)
        (self.output_dir / "workspaces").mkdir(exist_ok=True)
        
        console.print()
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console,
        ) as progress:
            task = progress.add_task("[cyan]Recovering Cursor data...", total=None)
            
            async for item in self.scraper.scrape_all():
                self.items.append(item)
                self._save_item(item)
                
                if item.source_type == "cursor_project":
                    self.projects_found += 1
                elif item.source_type == "cursor_chat":
                    self.chats_found += 1
                elif item.source_type == "cursor_file":
                    self.code_files_found += 1
                
                progress.update(
                    task, 
                    description=f"[cyan]Projects: {self.projects_found} | Chats: {self.chats_found} | Files: {self.code_files_found}"
                )
        
        # Save summary
        self._save_summary()
        
        # Display results
        self._display_results()
    
    def _save_item(self, item: ScrapedItem):
        """Save an item to appropriate location"""
        
        try:
            if item.source_type == "cursor_project":
                filepath = self.output_dir / "projects" / item.filename
                filepath.write_text(item.content, encoding='utf-8')
                
                # Save metadata
                meta_path = filepath.with_suffix('.json')
                meta_path.write_text(json.dumps(item.metadata, indent=2), encoding='utf-8')
                
            elif item.source_type == "cursor_chat":
                filepath = self.output_dir / "chats" / item.filename
                filepath.write_text(item.content, encoding='utf-8')
                
            elif item.source_type == "cursor_workspace":
                filepath = self.output_dir / "workspaces" / item.filename
                filepath.write_text(item.content, encoding='utf-8')
                
            elif item.source_type == "cursor_file":
                # Organize by project
                project = item.metadata.get('project', 'unknown')
                project_dir = self.output_dir / "code" / project
                project_dir.mkdir(parents=True, exist_ok=True)
                
                filepath = project_dir / item.filename
                filepath.write_text(item.content, encoding='utf-8')
                
        except Exception as e:
            pass
    
    def _save_summary(self):
        """Save recovery summary"""
        
        summary = {
            "recovered_at": datetime.now().isoformat(),
            "username": self.username,
            "statistics": {
                "total_items": len(self.items),
                "projects_found": self.projects_found,
                "chats_found": self.chats_found,
                "code_files_found": self.code_files_found,
            },
            "scraper_summary": self.scraper.get_summary(),
        }
        
        summary_path = self.output_dir / "recovery_summary.json"
        summary_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
        
        # Also create a markdown summary
        md_summary = self._create_markdown_summary(summary)
        md_path = self.output_dir / "README.md"
        md_path.write_text(md_summary, encoding='utf-8')
    
    def _create_markdown_summary(self, summary: dict) -> str:
        """Create markdown summary"""
        
        lines = [
            "# Cursor Projects Recovery Summary",
            "",
            f"**Recovered:** {summary['recovered_at']}",
            f"**User:** {summary['username']}",
            "",
            "## Statistics",
            "",
            f"- **Total Items:** {summary['statistics']['total_items']}",
            f"- **Projects Found:** {summary['statistics']['projects_found']}",
            f"- **AI Chats Found:** {summary['statistics']['chats_found']}",
            f"- **Code Files Found:** {summary['statistics']['code_files_found']}",
            "",
            "## Projects",
            "",
        ]
        
        for project in summary['scraper_summary'].get('projects', []):
            lines.append(f"### {project['name']}")
            lines.append(f"- Path: `{project['path']}`")
            lines.append(f"- Has .cursor: {project['has_cursor']}")
            lines.append("")
        
        lines.extend([
            "## Directory Structure",
            "",
            "```",
            "recovered/cursor/",
            "├── projects/      # Project info and metadata",
            "├── chats/         # AI conversation history",
            "├── code/          # Source code by project",
            "├── workspaces/    # Workspace configurations",
            "└── README.md      # This file",
            "```",
        ])
        
        return "\n".join(lines)
    
    def _display_results(self):
        """Display recovery results"""
        
        console.print()
        console.print(Panel.fit(
            "[bold green]✅ RECOVERY COMPLETE[/bold green]",
            border_style="green"
        ))
        
        # Statistics table
        table = Table(title="Recovery Statistics")
        table.add_column("Category", style="cyan")
        table.add_column("Count", style="green")
        
        table.add_row("Projects Found", str(self.projects_found))
        table.add_row("AI Chats Found", str(self.chats_found))
        table.add_row("Code Files Found", str(self.code_files_found))
        table.add_row("Total Items", str(len(self.items)))
        
        console.print(table)
        
        # Projects tree
        if self.scraper.projects:
            console.print()
            tree = Tree("[bold]📁 Recovered Projects[/bold]")
            
            for project in self.scraper.projects[:20]:  # Show first 20
                branch = tree.add(f"[cyan]{project.name}[/cyan]")
                branch.add(f"[dim]{project.path}[/dim]")
                if project.has_cursor_folder:
                    branch.add("[green]✓ Has .cursor folder[/green]")
            
            if len(self.scraper.projects) > 20:
                tree.add(f"[dim]... and {len(self.scraper.projects) - 20} more[/dim]")
            
            console.print(tree)
        
        # Output location
        console.print()
        console.print(f"[bold]Output saved to:[/bold] {self.output_dir}")


async def main():
    """Main entry point"""
    
    print("=" * 60)
    print("CURSOR PROJECTS COMPLETE RECOVERY")
    print("=" * 60)
    print()
    
    recovery = CursorRecovery(username="eguid")
    await recovery.run()


if __name__ == "__main__":
    asyncio.run(main())

3. Also Check VSCode Data (Cursor is based on VSCode)

Python

# recovery/scrapers/vscode_scraper.py
"""
VSCode/Cursor Shared Data Recovery

Both Cursor and VSCode share similar data structures.
This scraper handles both.
"""

import asyncio
import os
import json
import sqlite3
import shutil
import tempfile
from pathlib import Path
from typing import AsyncIterator, Dict, Any, List, Set
from dataclasses import dataclass

from loguru import logger


@dataclass
class ScrapedItem:
    id: str
    source_type: str
    source_path: str
    content: str
    content_type: str
    filename: str = None
    metadata: Dict[str, Any] = None
    language: str = None
    confidence_score: float = 1.0


class VSCodeDataScraper:
    """
    Scrapes VSCode AND Cursor data together.
    
    Both editors share:
    - Similar folder structure
    - Similar database formats
    - Similar extension APIs
    """
    
    def __init__(self, username: str = "eguid"):
        self.username = username
        
        # All possible data locations
        self.data_paths = {
            "cursor_roaming": Path(f"C:/Users/{username}/AppData/Roaming/Cursor"),
            "cursor_local": Path(f"C:/Users/{username}/AppData/Local/Cursor"),
            "vscode_roaming": Path(f"C:/Users/{username}/AppData/Roaming/Code"),
            "vscode_local": Path(f"C:/Users/{username}/AppData/Local/Programs/Microsoft VS Code"),
            "code_oss": Path(f"C:/Users/{username}/AppData/Roaming/Code - OSS"),
            "code_insiders": Path(f"C:/Users/{username}/AppData/Roaming/Code - Insiders"),
        }
        
        self.processed: Set[str] = set()
    
    async def scrape_all(self) -> AsyncIterator[ScrapedItem]:
        """Scrape all VSCode/Cursor data"""
        
        for name, base_path in self.data_paths.items():
            if not base_path.exists():
                continue
            
            logger.info(f"Scanning {name}: {base_path}")
            
            # Recent files/folders
            async for item in self._extract_recent(base_path, name):
                yield item
            
            # Workspace storage
            async for item in self._extract_workspaces(base_path, name):
                yield item
            
            # Global state
            async for item in self._extract_global_state(base_path, name):
                yield item
            
            # History
            async for item in self._extract_history(base_path, name):
                yield item
    
    async def _extract_recent(self, base_path: Path, source: str) -> AsyncIterator[ScrapedItem]:
        """Extract recently opened files/folders"""
        
        storage_path = base_path / "User" / "globalStorage" / "storage.json"
        if storage_path.exists():
            try:
                data = json.loads(storage_path.read_text())
                
                # Extract paths
                paths = []
                self._extract_paths_recursive(data, paths)
                
                if paths:
                    content = f"# Recently Opened in {source}\n\n"
                    for p in paths:
                        content += f"- `{p}`\n"
                    
                    yield ScrapedItem(
                        id=f"{source}:recent",
                        source_type=f"{source}_recent",
                        source_path=str(storage_path),
                        content=content,
                        content_type="file_list",
                        filename=f"{source}_recent_files.md",
                        metadata={"paths": paths},
                    )
            except Exception as e:
                pass
    
    def _extract_paths_recursive(self, obj: Any, paths: List[str], depth: int = 0):
        """Recursively extract file paths"""
        if depth > 10:
            return
        
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, str) and self._looks_like_path(value):
                    paths.append(value)
                else:
                    self._extract_paths_recursive(value, paths, depth + 1)
        elif isinstance(obj, list):
            for item in obj:
                self._extract_paths_recursive(item, paths, depth + 1)
    
    def _looks_like_path(self, s: str) -> bool:
        """Check if string looks like a file path"""
        if not s:
            return False
        
        # Check for path indicators
        if s.startswith('file:///'):
            return True
        if s.startswith('/') or (len(s) > 2 and s[1] == ':'):
            return True
        if '\\' in s and ('Users' in s or 'home' in s):
            return True
        
        return False
    
    async def _extract_workspaces(self, base_path: Path, source: str) -> AsyncIterator[ScrapedItem]:
        """Extract workspace data"""
        
        ws_storage = base_path / "User" / "workspaceStorage"
        if not ws_storage.exists():
            return
        
        for ws_dir in ws_storage.iterdir():
            if not ws_dir.is_dir():
                continue
            
            # workspace.json
            ws_json = ws_dir / "workspace.json"
            if ws_json.exists():
                try:
                    data = json.loads(ws_json.read_text())
                    folder = data.get('folder', '')
                    
                    if folder:
                        yield ScrapedItem(
                            id=f"{source}:workspace:{ws_dir.name}",
                            source_type=f"{source}_workspace",
                            source_path=str(ws_json),
                            content=json.dumps(data, indent=2),
                            content_type="workspace",
                            filename=f"workspace_{ws_dir.name[:16]}.json",
                            metadata={"folder": folder},
                        )
                except:
                    pass
            
            # state.vscdb
            state_db = ws_dir / "state.vscdb"
            if state_db.exists():
                async for item in self._parse_vscdb(state_db, source):
                    yield item
    
    async def _extract_global_state(self, base_path: Path, source: str) -> AsyncIterator[ScrapedItem]:
        """Extract global state"""
        
        global_storage = base_path / "User" / "globalStorage"
        if not global_storage.exists():
            return
        
        # Check each extension's storage
        for ext_dir in global_storage.iterdir():
            if not ext_dir.is_dir():
                continue
            
            # Look for interesting data
            for json_file in ext_dir.glob("*.json"):
                try:
                    content = json_file.read_text()
                    
                    # Check if it's chat/AI related
                    if any(term in content.lower() for term in ['chat', 'message', 'conversation', 'prompt']):
                        yield ScrapedItem(
                            id=f"{source}:global:{ext_dir.name}:{json_file.name}",
                            source_type=f"{source}_extension",
                            source_path=str(json_file),
                            content=content,
                            content_type="extension_data",
                            filename=f"{ext_dir.name}_{json_file.name}",
                            metadata={"extension": ext_dir.name},
                        )
                except:
                    pass
    
    async def _extract_history(self, base_path: Path, source: str) -> AsyncIterator[ScrapedItem]:
        """Extract edit history"""
        
        history_path = base_path / "User" / "History"
        if not history_path.exists():
            return
        
        for history_dir in history_path.iterdir():
            if not history_dir.is_dir():
                continue
            
            # entries.json contains file history
            entries = history_dir / "entries.json"
            if entries.exists():
                try:
                    data = json.loads(entries.read_text())
                    
                    for entry in data.get('entries', []):
                        # Each entry has a timestamp and content reference
                        entry_id = entry.get('id', '')
                        entry_file = history_dir / entry_id
                        
                        if entry_file.exists():
                            content = entry_file.read_text(encoding='utf-8', errors='ignore')
                            
                            yield ScrapedItem(
                                id=f"{source}:history:{history_dir.name}:{entry_id}",
                                source_type=f"{source}_history",
                                source_path=str(entry_file),
                                content=content,
                                content_type="history_entry",
                                filename=f"history_{entry_id[:16]}.txt",
                                metadata={
                                    "timestamp": entry.get('timestamp'),
                                    "source": entry.get('source'),
                                },
                            )
                except:
                    pass
    
    async def _parse_vscdb(self, db_path: Path, source: str) -> AsyncIterator[ScrapedItem]:
        """Parse VSCode database"""
        
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.db') as tmp:
                tmp_path = tmp.name
            
            shutil.copy2(db_path, tmp_path)
            
            conn = sqlite3.connect(tmp_path)
            cursor = conn.cursor()
            
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cursor.fetchall()]
            
            for table in tables:
                try:
                    cursor.execute(f"SELECT key, value FROM {table}")
                    rows = cursor.fetchall()
                    
                    for key, value in rows:
                        if isinstance(value, bytes):
                            value = value.decode('utf-8', errors='ignore')
                        
                        if not value:
                            continue
                        
                        # Check if interesting
                        if any(term in str(value).lower() for term in ['chat', 'message', 'conversation', 'assistant', 'prompt']):
                            yield ScrapedItem(
                                id=f"{source}:db:{table}:{key}",
                                source_type=f"{source}_database",
                                source_path=str(db_path),
                                content=value[:50000] if isinstance(value, str) else str(value)[:50000],
                                content_type="database_entry",
                                filename=f"db_{table}_{key[:20]}.txt",
                                metadata={"table": table, "key": key},
                            )
                except:
                    continue
            
            conn.close()
            os.unlink(tmp_path)
            
        except Exception as e:
            pass

4. Updated Main Recovery Script

Python

# scripts/recover_all.py
"""
COMPLETE RECOVERY - Everything

Recovers:
1. All LM Arena chat history
2. All Cursor projects
3. All VSCode data
4. All code from specified locations
"""

import asyncio
import sys
from pathlib import Path
from datetime import datetime
import json

sys.path.insert(0, str(Path(__file__).parent.parent))

from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table

# Import scrapers
from recovery.scrapers.lmarena_full_history import LMArenaFullHistoryScraper
from recovery.scrapers.cursor_scraper import CursorProjectsScraper
from recovery.scrapers.vscode_scraper import VSCodeDataScraper
from recovery.processors.agent_processor import AgentProcessor
from recovery.processors.database_processor import DatabaseProcessor
from recovery.processors.prompt_processor import PromptProcessor

console = Console()


class CompleteRecovery:
    """Complete recovery of all data"""
    
    def __init__(self, username: str = "eguid"):
        self.username = username
        self.output_dir = Path(f"C:/Users/{username}/Desktop/CLAUDE RECOMENDATIONS/recovered")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize scrapers
        self.lmarena_scraper = LMArenaFullHistoryScraper(username)
        self.cursor_scraper = CursorProjectsScraper(username)
        self.vscode_scraper = VSCodeDataScraper(username)
        
        # Initialize processors
        self.agent_processor = AgentProcessor({})
        self.db_processor = DatabaseProcessor({})
        self.prompt_processor = PromptProcessor({})
        
        # Stats
        self.stats = {
            "lmarena_items": 0,
            "cursor_projects": 0,
            "cursor_chats": 0,
            "vscode_items": 0,
            "agents_found": 0,
            "schemas_found": 0,
            "prompts_found": 0,
            "code_files": 0,
        }
    
    async def run(self):
        """Run complete recovery"""
        
        console.print(Panel.fit(
            "[bold cyan]🔮 COMPLETE DATA RECOVERY[/bold cyan]\n\n"
            "Recovering ALL your data:\n"
            "  • LM Arena chat history (all browsers)\n"
            "  • Cursor projects & AI chats\n"
            "  • VSCode workspaces & history\n"
            "  • Agent code\n"
            "  • Database schemas\n"
            "  • Prompt templates\n\n"
            f"Locations:\n"
            f"  • WSL filesystem\n"
            f"  • G:\\restored\n"
            f"  • OneDrive folders\n"
            f"  • Browser data\n\n"
            f"Output: {self.output_dir}",
            border_style="cyan"
        ))
        
        # Create directory structure
        self._create_directories()
        
        # Phase 1: LM Arena
        console.print("\n[bold magenta]━━━ Phase 1: LM Arena History ━━━[/bold magenta]")
        await self._recover_lmarena()
        
        # Phase 2: Cursor
        console.print("\n[bold magenta]━━━ Phase 2: Cursor Projects ━━━[/bold magenta]")
        await self._recover_cursor()
        
        # Phase 3: VSCode
        console.print("\n[bold magenta]━━━ Phase 3: VSCode Data ━━━[/bold magenta]")
        await self._recover_vscode()
        
        # Phase 4: Process for Agents/Schemas/Prompts
        console.print("\n[bold magenta]━━━ Phase 4: Extract Agents/Schemas/Prompts ━━━[/bold magenta]")
        await self._process_extracted()
        
        # Save summary
        self._save_summary()
        
        # Display results
        self._display_results()
    
    def _create_directories(self):
        """Create output directory structure"""
        dirs = [
            "lmarena/chats",
            "lmarena/code",
            "cursor/projects",
            "cursor/chats",
            "cursor/code",
            "vscode/workspaces",
            "vscode/history",
            "agents",
            "schemas",
            "prompts",
            "workflows",
        ]
        
        for d in dirs:
            (self.output_dir / d).mkdir(parents=True, exist_ok=True)
    
    async def _recover_lmarena(self):
        """Recover LM Arena data"""
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("[cyan]Scanning browser data...", total=None)
            
            async for item in self.lmarena_scraper.scrape_all():
                self.stats["lmarena_items"] += 1
                
                # Save item
                if item.content_type == "ai_conversation":
                    filepath = self.output_dir / "lmarena/chats" / item.filename
                    filepath.write_text(item.content, encoding='utf-8')
                elif item.content_type == "source_code":
                    filepath = self.output_dir / "lmarena/code" / item.filename
                    filepath.write_text(item.content, encoding='utf-8')
                    self.stats["code_files"] += 1
                
                progress.update(task, description=f"[cyan]LM Arena items: {self.stats['lmarena_items']}")
    
    async def _recover_cursor(self):
        """Recover Cursor data"""
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("[cyan]Scanning Cursor data...", total=None)
            
            async for item in self.cursor_scraper.scrape_all():
                if item.source_type == "cursor_project":
                    self.stats["cursor_projects"] += 1
                    filepath = self.output_dir / "cursor/projects" / item.filename
                    filepath.write_text(item.content, encoding='utf-8')
                    
                elif item.source_type == "cursor_chat":
                    self.stats["cursor_chats"] += 1
                    filepath = self.output_dir / "cursor/chats" / item.filename
                    filepath.write_text(item.content, encoding='utf-8')
                    
                elif item.source_type == "cursor_file":
                    self.stats["code_files"] += 1
                    project = item.metadata.get('project', 'unknown')
                    project_dir = self.output_dir / "cursor/code" / project
                    project_dir.mkdir(parents=True, exist_ok=True)
                    filepath = project_dir / item.filename
                    filepath.write_text(item.content, encoding='utf-8')
                
                progress.update(
                    task, 
                    description=f"[cyan]Projects: {self.stats['cursor_projects']} | Chats: {self.stats['cursor_chats']}"
                )
    
    async def _recover_vscode(self):
        """Recover VSCode data"""
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("[cyan]Scanning VSCode data...", total=None)
            
            async for item in self.vscode_scraper.scrape_all():
                self.stats["vscode_items"] += 1
                
                if item.content_type == "workspace":
                    filepath = self.output_dir / "vscode/workspaces" / item.filename
                    filepath.write_text(item.content, encoding='utf-8')
                elif item.content_type == "history_entry":
                    filepath = self.output_dir / "vscode/history" / item.filename
                    filepath.write_text(item.content, encoding='utf-8')
                
                progress.update(task, description=f"[cyan]VSCode items: {self.stats['vscode_items']}")
    
    async def _process_extracted(self):
        """Process extracted content for agents/schemas/prompts"""
        
        # Scan all extracted code
        code_dirs = [
            self.output_dir / "lmarena/code",
            self.output_dir / "cursor/code",
            self.output_dir / "vscode/history",
        ]
        
        for code_dir in code_dirs:
            if not code_dir.exists():
                continue
            
            for filepath in code_dir.rglob("*"):
                if not filepath.is_file():
                    continue
                
                try:
                    content = filepath.read_text(encoding='utf-8', errors='ignore')
                    
                    # Check for agents
                    if self.agent_processor._is_agent_code(content):
                        agent = self.agent_processor.process(content, {"path": str(filepath)})
                        if agent:
                            self.stats["agents_found"] += 1
                            agent_path = self.output_dir / "agents" / f"{agent.class_name}.py"
                            agent_path.write_text(content, encoding='utf-8')
                    
                    # Check for schemas
                    if self.db_processor._is_sql_schema(content):
                        schema = self.db_processor.process(content, {"path": str(filepath)})
                        if schema:
                            self.stats["schemas_found"] += 1
                            schema_path = self.output_dir / "schemas" / filepath.name
                            schema_path.write_text(content, encoding='utf-8')
                    
                    # Check for prompts
                    prompts = self.prompt_processor.process(content, {"path": str(filepath)})
                    if prompts:
                        self.stats["prompts_found"] += len(prompts)
                        for prompt in prompts:
                            prompt_path = self.output_dir / "prompts" / f"{prompt.name}.txt"
                            prompt_path.write_text(prompt.content, encoding='utf-8')
                            
                except Exception as e:
                    continue
    
    def _save_summary(self):
        """Save recovery summary"""
        
        summary = {
            "recovered_at": datetime.now().isoformat(),
            "username": self.username,
            "statistics": self.stats,
            "output_directory": str(self.output_dir),
            "agents": self.agent_processor.get_agent_summary(),
            "schemas": self.db_processor.get_schema_summary(),
            "prompts": self.prompt_processor.get_prompt_summary(),
        }
        
        # JSON summary
        summary_path = self.output_dir / "recovery_summary.json"
        summary_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
        
        # Markdown summary
        md_path = self.output_dir / "README.md"
        md_path.write_text(self._create_readme(summary), encoding='utf-8')
    
    def _create_readme(self, summary: dict) -> str:
        """Create README.md"""
        
        return f"""# Complete Data Recovery Summary

**Recovered:** {summary['recovered_at']}
**User:** {summary['username']}

## Statistics

| Category | Count |
|----------|-------|
| LM Arena Items | {self.stats['lmarena_items']} |
| Cursor Projects | {self.stats['cursor_projects']} |
| Cursor Chats | {self.stats['cursor_chats']} |
| VSCode Items | {self.stats['vscode_items']} |
| Agents Found | {self.stats['agents_found']} |
| Schemas Found | {self.stats['schemas_found']} |
| Prompts Found | {self.stats['prompts_found']} |
| Code Files | {self.stats['code_files']} |

## Directory Structure

recovered/
├── lmarena/
│ ├── chats/ # LM Arena AI conversations
│ └── code/ # Code blocks from chats
├── cursor/
│ ├── projects/ # Cursor project info
│ ├── chats/ # Cursor AI conversations
│ └── code/ # Code from projects
├── vscode/
│ ├── workspaces/ # VSCode workspaces
│ └── history/ # Edit history
├── agents/ # Extracted agent code
├── schemas/ # Extracted SQL schemas
├── prompts/ # Extracted prompt templates
├── workflows/ # Extracted workflows
└── README.md # This file

text


## Recovered Agents

{self._list_agents(summary)}

## Recovered Schemas

{self._list_schemas(summary)}
"""
    
    def _list_agents(self, summary: dict) -> str:
        agents = summary.get('agents', {}).get('agents', [])
        if not agents:
            return "No agents found."
        
        lines = []
        for a in agents:
            lines.append(f"- **{a['class']}** ({a['agency']}) - {a['methods']} methods, {a['tools']} tools")
        return "\n".join(lines)
    
    def _list_schemas(self, summary: dict) -> str:
        tables = summary.get('schemas', {}).get('tables', [])
        if not tables:
            return "No schemas found."
        
        lines = []
        for t in tables:
            lines.append(f"- **{t['name']}** - {t['columns']} columns")
        return "\n".join(lines)
    
    def _display_results(self):
        """Display results"""
        
        console.print()
        console.print(Panel.fit(
            "[bold green]✅ COMPLETE RECOVERY FINISHED[/bold green]",
            border_style="green"
        ))
        
        table = Table(title="Recovery Statistics")
        table.add_column("Category", style="cyan")
        table.add_column("Count", style="green")
        
        for key, value in self.stats.items():
            table.add_row(key.replace('_', ' ').title(), str(value))
        
        console.print(table)
        console.print()
        console.print(f"[bold]Output:[/bold] {self.output_dir}")


async def main():
    recovery = CompleteRecovery(username="eguid")
    await recovery.run()


if __name__ == "__main__":
    asyncio.run(main())

Run It

PowerShell

# PowerShell - Run complete recovery

cd "C:\Users\eguid\Desktop\CLAUDE RECOMENDATIONS"

# Activate venv
.\venv\Scripts\Activate

# Run COMPLETE recovery (LM Arena + Cursor + VSCode + Everything)
python scripts/recover_all.py

# Or run just Cursor projects
python scripts/recover_cursor_projects.py

This will recover:

    ALL LM Arena chat history from all browsers
    ALL Cursor projects ever opened
    ALL Cursor AI conversations
    ALL VSCode workspaces and history
    ALL code files from those projects
    Extract and organize:
        Agent class definitions
        Database schemas
        Prompt templates
        Workflows

Output structure:

text

recovered/
├── lmarena/
│   ├── chats/          # All LM Arena conversations
│   └── code/           # Code extracted from chats
├── cursor/
│   ├── projects/       # All Cursor projects found
│   ├── chats/          # All Cursor AI chats
│   └── code/           # All code from projects
├── vscode/
│   ├── workspaces/     # All workspaces
│   └── history/        # Edit history
├── agents/             # Extracted agent code
├── schemas/            # Extracted SQL schemas
├── prompts/            # Extracted prompts
├── workflows/          # Extracted workflows
└── README.md           # Summary

Would you like me to add any additional recovery sources or processing?

ALL OLD CURSOR PRJECTS
claude-opus-4-5-20251101-thinking-32k
Complete LM Arena History Scraper + Agent/Database/Prompt Recovery

Let me create a focused system to recover your entire LM Arena history and specifically target agents, databases, prompts, and code snippets.
1. Complete LM Arena History Scraper

Python

# recovery/scrapers/lmarena_full_history.py
"""
LM Arena FULL History Scraper
Extracts ALL chat history from browser storage, cache, and any available source
"""

import asyncio
import aiofiles
import json
import os
import re
import sqlite3
import shutil
import tempfile
import struct
from pathlib import Path
from datetime import datetime
from typing import AsyncIterator, Dict, Any, List, Optional, Set, Tuple
from dataclasses import dataclass, field
import subprocess

from loguru import logger


@dataclass
class ChatMessage:
    role: str
    content: str
    model: Optional[str] = None
    timestamp: Optional[str] = None


@dataclass
class ChatConversation:
    id: str
    title: Optional[str] = None
    messages: List[ChatMessage] = field(default_factory=list)
    models: List[str] = field(default_factory=list)
    created_at: Optional[str] = None
    url: Optional[str] = None
    source: str = "unknown"
    raw_data: Optional[Dict] = None


@dataclass 
class ScrapedItem:
    id: str
    source_type: str
    source_path: str
    content: str
    content_type: str
    filename: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    language: Optional[str] = None
    confidence_score: float = 1.0


class LMArenaFullHistoryScraper:
    """
    Comprehensive scraper for ALL LM Arena chat history.
    
    Sources:
    1. Chrome Local Storage (LevelDB)
    2. Chrome IndexedDB
    3. Chrome Session Storage
    4. Chrome Cache
    5. Edge (same as Chrome)
    6. Firefox (different format)
    7. Browser History (for URL discovery)
    8. Any exported JSON/MD files
    9. Clipboard history (if available)
    """
    
    # Known LM Arena domains
    LMARENA_DOMAINS = [
        'lmarena.ai',
        'chat.lmsys.org', 
        'arena.lmsys.org',
        'lmsys.org',
        'chatbot-arena',
    ]
    
    def __init__(self, username: str = "eguid"):
        self.username = username
        self.processed_ids: Set[str] = set()
        self.conversations: List[ChatConversation] = []
        
        # Browser paths
        self.browser_paths = self._get_browser_paths()
        
    def _get_browser_paths(self) -> Dict[str, List[Path]]:
        """Get all browser data paths"""
        base = Path(f"C:/Users/{self.username}/AppData")
        
        return {
            "chrome": [
                base / "Local/Google/Chrome/User Data/Default",
                base / "Local/Google/Chrome/User Data/Profile 1",
                base / "Local/Google/Chrome/User Data/Profile 2",
            ],
            "edge": [
                base / "Local/Microsoft/Edge/User Data/Default",
                base / "Local/Microsoft/Edge/User Data/Profile 1",
            ],
            "firefox": [
                base / "Roaming/Mozilla/Firefox/Profiles",
            ],
            "brave": [
                base / "Local/BraveSoftware/Brave-Browser/User Data/Default",
            ],
            "vivaldi": [
                base / "Local/Vivaldi/User Data/Default",
            ],
        }
    
    async def scrape_all(self) -> AsyncIterator[ScrapedItem]:
        """Scrape ALL available LM Arena history"""
        logger.info("=" * 60)
        logger.info("STARTING FULL LM ARENA HISTORY EXTRACTION")
        logger.info("=" * 60)
        
        # 1. Scan all Chromium-based browsers
        for browser_name, paths in self.browser_paths.items():
            if browser_name == "firefox":
                continue  # Handle separately
                
            for profile_path in paths:
                if profile_path.exists():
                    logger.info(f"Scanning {browser_name}: {profile_path}")
                    async for item in self._scrape_chromium_browser(profile_path, browser_name):
                        yield item
        
        # 2. Scan Firefox
        for firefox_path in self.browser_paths.get("firefox", []):
            if firefox_path.exists():
                async for item in self._scrape_firefox(firefox_path):
                    yield item
        
        # 3. Scan for exported files
        export_paths = [
            Path(f"C:/Users/{self.username}/Downloads"),
            Path(f"C:/Users/{self.username}/Documents"),
            Path(f"C:/Users/{self.username}/Desktop"),
            Path(f"C:/Users/{self.username}/OneDrive/Desktop"),
            Path(f"C:/Users/{self.username}/OneDrive/Documents"),
            Path("G:/restored"),
        ]
        
        for export_path in export_paths:
            if export_path.exists():
                logger.info(f"Scanning exports: {export_path}")
                async for item in self._scan_exported_files(export_path):
                    yield item
        
        # 4. Extract code blocks from all conversations
        logger.info(f"Extracting code blocks from {len(self.conversations)} conversations")
        async for item in self._extract_all_code_blocks():
            yield item
        
        logger.info(f"Total conversations found: {len(self.conversations)}")
        logger.info(f"Total unique chat IDs: {len(self.processed_ids)}")
    
    async def _scrape_chromium_browser(
        self, 
        profile_path: Path, 
        browser_name: str
    ) -> AsyncIterator[ScrapedItem]:
        """Scrape a Chromium-based browser profile"""
        
        # 1. Local Storage (LevelDB)
        local_storage = profile_path / "Local Storage" / "leveldb"
        if local_storage.exists():
            async for item in self._parse_leveldb(local_storage, browser_name, "local_storage"):
                yield item
        
        # 2. Session Storage
        session_storage = profile_path / "Session Storage"
        if session_storage.exists():
            async for item in self._parse_leveldb(session_storage, browser_name, "session_storage"):
                yield item
        
        # 3. IndexedDB
        indexeddb = profile_path / "IndexedDB"
        if indexeddb.exists():
            async for item in self._parse_indexeddb(indexeddb, browser_name):
                yield item
        
        # 4. Cache
        cache_paths = [
            profile_path / "Cache" / "Cache_Data",
            profile_path / "Code Cache",
            profile_path / "GPUCache",
        ]
        for cache_path in cache_paths:
            if cache_path.exists():
                async for item in self._parse_cache(cache_path, browser_name):
                    yield item
        
        # 5. History (for URL discovery)
        history_db = profile_path / "History"
        if history_db.exists():
            async for item in self._parse_history(history_db, browser_name):
                yield item
    
    async def _parse_leveldb(
        self, 
        leveldb_path: Path, 
        browser: str,
        storage_type: str
    ) -> AsyncIterator[ScrapedItem]:
        """Parse LevelDB storage for LM Arena data"""
        
        # LevelDB stores data in .ldb and .log files
        files_to_check = list(leveldb_path.glob("*.ldb")) + list(leveldb_path.glob("*.log"))
        
        for db_file in files_to_check:
            try:
                content = db_file.read_bytes()
                
                # Search for LM Arena related content
                content_str = content.decode('utf-8', errors='ignore')
                
                # Check if contains LM Arena data
                if not any(domain in content_str.lower() for domain in self.LMARENA_DOMAINS):
                    continue
                
                # Try to extract JSON objects
                json_objects = self._extract_json_from_binary(content_str)
                
                for i, json_obj in enumerate(json_objects):
                    if self._is_chat_data(json_obj):
                        conv = self._parse_chat_json(json_obj, f"{browser}_{storage_type}")
                        if conv and conv.id not in self.processed_ids:
                            self.processed_ids.add(conv.id)
                            self.conversations.append(conv)
                            
                            yield ScrapedItem(
                                id=f"lmarena:{browser}:{conv.id}",
                                source_type="lmarena",
                                source_path=str(db_file),
                                content=self._format_conversation(conv),
                                content_type="chat_conversation",
                                filename=f"lmarena_chat_{conv.id[:16]}.md",
                                metadata={
                                    "browser": browser,
                                    "storage_type": storage_type,
                                    "chat_id": conv.id,
                                    "models": conv.models,
                                    "message_count": len(conv.messages),
                                    "source": conv.source,
                                },
                                confidence_score=0.9
                            )
                
                # Also check for raw conversation text
                conversations = self._extract_conversations_from_text(content_str)
                for conv_text in conversations:
                    conv_id = self._generate_id(conv_text)
                    if conv_id not in self.processed_ids:
                        self.processed_ids.add(conv_id)
                        
                        yield ScrapedItem(
                            id=f"lmarena:{browser}:raw:{conv_id}",
                            source_type="lmarena",
                            source_path=str(db_file),
                            content=conv_text,
                            content_type="chat_raw",
                            filename=f"lmarena_raw_{conv_id[:16]}.txt",
                            metadata={
                                "browser": browser,
                                "storage_type": storage_type,
                                "extraction_method": "text_pattern",
                            },
                            confidence_score=0.7
                        )
                        
            except Exception as e:
                logger.debug(f"Error parsing {db_file}: {e}")
    
    async def _parse_indexeddb(
        self, 
        indexeddb_path: Path, 
        browser: str
    ) -> AsyncIterator[ScrapedItem]:
        """Parse IndexedDB for chat data"""
        
        # Find LM Arena related databases
        for db_dir in indexeddb_path.iterdir():
            if not db_dir.is_dir():
                continue
            
            db_name = db_dir.name.lower()
            
            # Check if related to LM Arena
            if not any(domain.replace('.', '_') in db_name or domain in db_name 
                      for domain in self.LMARENA_DOMAINS):
                continue
            
            logger.info(f"Found LM Arena IndexedDB: {db_dir.name}")
            
            # Find SQLite databases within
            for sqlite_file in db_dir.rglob("*.sqlite"):
                async for item in self._parse_sqlite_db(sqlite_file, browser, "indexeddb"):
                    yield item
            
            # Also check LevelDB within IndexedDB
            for leveldb_dir in db_dir.rglob("leveldb"):
                if leveldb_dir.is_dir():
                    async for item in self._parse_leveldb(leveldb_dir, browser, "indexeddb"):
                        yield item
    
    async def _parse_sqlite_db(
        self, 
        db_path: Path, 
        browser: str,
        source_type: str
    ) -> AsyncIterator[ScrapedItem]:
        """Parse SQLite database for chat data"""
        
        try:
            # Copy to temp file (might be locked)
            with tempfile.NamedTemporaryFile(delete=False, suffix='.sqlite') as tmp:
                tmp_path = tmp.name
            
            shutil.copy2(db_path, tmp_path)
            
            conn = sqlite3.connect(tmp_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            # Get all tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cursor.fetchall()]
            
            for table in tables:
                try:
                    cursor.execute(f"SELECT * FROM {table}")
                    rows = cursor.fetchall()
                    
                    for row in rows:
                        row_dict = dict(row)
                        row_str = json.dumps(row_dict, default=str)
                        
                        # Check if contains chat data
                        if any(term in row_str.lower() for term in ['message', 'chat', 'conversation', 'content']):
                            if self._is_chat_data(row_dict):
                                conv = self._parse_chat_json(row_dict, f"{browser}_{source_type}")
                                if conv and conv.id not in self.processed_ids:
                                    self.processed_ids.add(conv.id)
                                    self.conversations.append(conv)
                                    
                                    yield ScrapedItem(
                                        id=f"lmarena:{browser}:sqlite:{conv.id}",
                                        source_type="lmarena",
                                        source_path=str(db_path),
                                        content=self._format_conversation(conv),
                                        content_type="chat_conversation",
                                        filename=f"lmarena_chat_{conv.id[:16]}.md",
                                        metadata={
                                            "browser": browser,
                                            "source_type": source_type,
                                            "table": table,
                                            "chat_id": conv.id,
                                        },
                                        confidence_score=0.9
                                    )
                except Exception as e:
                    continue
            
            conn.close()
            os.unlink(tmp_path)
            
        except Exception as e:
            logger.debug(f"Error parsing SQLite {db_path}: {e}")
    
    async def _parse_cache(
        self, 
        cache_path: Path, 
        browser: str
    ) -> AsyncIterator[ScrapedItem]:
        """Parse browser cache for API responses"""
        
        try:
            for cache_file in cache_path.iterdir():
                if not cache_file.is_file():
                    continue
                
                try:
                    content = cache_file.read_bytes()
                    content_str = content.decode('utf-8', errors='ignore')
                    
                    # Look for LM Arena API responses
                    if not any(domain in content_str.lower() for domain in self.LMARENA_DOMAINS):
                        continue
                    
                    # Look for JSON API responses
                    json_matches = re.findall(
                        r'\{[^{}]*"(?:messages?|conversation|chat)"[^{}]*\}',
                        content_str,
                        re.DOTALL
                    )
                    
                    for json_str in json_matches:
                        try:
                            data = json.loads(json_str)
                            if self._is_chat_data(data):
                                conv = self._parse_chat_json(data, f"{browser}_cache")
                                if conv and conv.id not in self.processed_ids:
                                    self.processed_ids.add(conv.id)
                                    self.conversations.append(conv)
                                    
                                    yield ScrapedItem(
                                        id=f"lmarena:{browser}:cache:{conv.id}",
                                        source_type="lmarena",
                                        source_path=str(cache_file),
                                        content=self._format_conversation(conv),
                                        content_type="chat_conversation",
                                        filename=f"lmarena_cache_{conv.id[:16]}.md",
                                        metadata={
                                            "browser": browser,
                                            "source_type": "cache",
                                            "chat_id": conv.id,
                                        },
                                        confidence_score=0.85
                                    )
                        except json.JSONDecodeError:
                            continue
                    
                    # Also look for larger JSON blobs
                    large_json = self._extract_json_from_binary(content_str)
                    for data in large_json:
                        if self._is_chat_data(data):
                            conv = self._parse_chat_json(data, f"{browser}_cache")
                            if conv and conv.id not in self.processed_ids:
                                self.processed_ids.add(conv.id)
                                self.conversations.append(conv)
                                
                                yield ScrapedItem(
                                    id=f"lmarena:{browser}:cache:{conv.id}",
                                    source_type="lmarena",
                                    source_path=str(cache_file),
                                    content=self._format_conversation(conv),
                                    content_type="chat_conversation",
                                    filename=f"lmarena_cache_{conv.id[:16]}.md",
                                    metadata={
                                        "browser": browser,
                                        "source_type": "cache",
                                    },
                                    confidence_score=0.85
                                )
                                
                except Exception as e:
                    continue
                    
        except Exception as e:
            logger.debug(f"Error parsing cache {cache_path}: {e}")
    
    async def _parse_history(
        self, 
        history_db: Path, 
        browser: str
    ) -> AsyncIterator[ScrapedItem]:
        """Parse browser history to find LM Arena URLs"""
        
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.db') as tmp:
                tmp_path = tmp.name
            
            shutil.copy2(history_db, tmp_path)
            
            conn = sqlite3.connect(tmp_path)
            cursor = conn.cursor()
            
            # Build domain query
            domain_conditions = " OR ".join(
                f"url LIKE '%{domain}%'" for domain in self.LMARENA_DOMAINS
            )
            
            cursor.execute(f"""
                SELECT url, title, last_visit_time, visit_count
                FROM urls
                WHERE {domain_conditions}
                ORDER BY last_visit_time DESC
            """)
            
            urls = cursor.fetchall()
            conn.close()
            os.unlink(tmp_path)
            
            if urls:
                # Extract chat IDs from URLs
                chat_urls = []
                for url, title, visit_time, visit_count in urls:
                    chat_id = self._extract_chat_id_from_url(url)
                    if chat_id:
                        chat_urls.append({
                            "url": url,
                            "title": title,
                            "chat_id": chat_id,
                            "visit_count": visit_count
                        })
                
                if chat_urls:
                    # Create a summary of discovered URLs
                    url_summary = "# LM Arena Chat History from Browser\n\n"
                    url_summary += f"Browser: {browser}\n"
                    url_summary += f"Total URLs found: {len(chat_urls)}\n\n"
                    url_summary += "## Chat URLs\n\n"
                    
                    for item in chat_urls:
                        url_summary += f"- [{item['title'] or item['chat_id']}]({item['url']})\n"
                        url_summary += f"  - ID: `{item['chat_id']}`\n"
                        url_summary += f"  - Visits: {item['visit_count']}\n"
                    
                    yield ScrapedItem(
                        id=f"lmarena:{browser}:history_urls",
                        source_type="lmarena",
                        source_path=str(history_db),
                        content=url_summary,
                        content_type="url_list",
                        filename=f"lmarena_{browser}_history.md",
                        metadata={
                            "browser": browser,
                            "url_count": len(chat_urls),
                            "chat_ids": [u["chat_id"] for u in chat_urls],
                        },
                        confidence_score=1.0
                    )
                    
        except Exception as e:
            logger.debug(f"Error parsing history {history_db}: {e}")
    
    async def _scrape_firefox(self, profiles_path: Path) -> AsyncIterator[ScrapedItem]:
        """Scrape Firefox profiles"""
        
        try:
            for profile in profiles_path.iterdir():
                if not profile.is_dir():
                    continue
                
                # Check places.sqlite for history
                places_db = profile / "places.sqlite"
                if places_db.exists():
                    async for item in self._parse_firefox_history(places_db):
                        yield item
                
                # Check storage for local storage
                storage_path = profile / "storage" / "default"
                if storage_path.exists():
                    for domain_dir in storage_path.iterdir():
                        if any(domain in domain_dir.name.lower() for domain in self.LMARENA_DOMAINS):
                            async for item in self._parse_firefox_storage(domain_dir):
                                yield item
                                
        except Exception as e:
            logger.debug(f"Error scraping Firefox: {e}")
    
    async def _parse_firefox_history(self, places_db: Path) -> AsyncIterator[ScrapedItem]:
        """Parse Firefox history"""
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.sqlite') as tmp:
                tmp_path = tmp.name
            
            shutil.copy2(places_db, tmp_path)
            
            conn = sqlite3.connect(tmp_path)
            cursor = conn.cursor()
            
            domain_conditions = " OR ".join(
                f"url LIKE '%{domain}%'" for domain in self.LMARENA_DOMAINS
            )
            
            cursor.execute(f"""
                SELECT url, title, visit_count, last_visit_date
                FROM moz_places
                WHERE {domain_conditions}
                ORDER BY last_visit_date DESC
            """)
            
            urls = cursor.fetchall()
            conn.close()
            os.unlink(tmp_path)
            
            if urls:
                chat_urls = []
                for url, title, visit_count, last_visit in urls:
                    chat_id = self._extract_chat_id_from_url(url)
                    if chat_id:
                        chat_urls.append({
                            "url": url,
                            "title": title,
                            "chat_id": chat_id,
                        })
                
                if chat_urls:
                    content = "# LM Arena History from Firefox\n\n"
                    content += f"Total: {len(chat_urls)} chats\n\n"
                    for item in chat_urls:
                        content += f"- `{item['chat_id']}`: [{item['title'] or 'Untitled'}]({item['url']})\n"
                    
                    yield ScrapedItem(
                        id="lmarena:firefox:history",
                        source_type="lmarena",
                        source_path=str(places_db),
                        content=content,
                        content_type="url_list",
                        filename="lmarena_firefox_history.md",
                        metadata={
                            "browser": "firefox",
                            "chat_ids": [u["chat_id"] for u in chat_urls],
                        },
                        confidence_score=1.0
                    )
                    
        except Exception as e:
            logger.debug(f"Error parsing Firefox history: {e}")
    
    async def _parse_firefox_storage(self, storage_dir: Path) -> AsyncIterator[ScrapedItem]:
        """Parse Firefox local storage"""
        
        ls_path = storage_dir / "ls"
        if ls_path.exists():
            for db_file in ls_path.glob("*.sqlite"):
                try:
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.sqlite') as tmp:
                        tmp_path = tmp.name
                    
                    shutil.copy2(db_file, tmp_path)
                    
                    conn = sqlite3.connect(tmp_path)
                    cursor = conn.cursor()
                    
                    cursor.execute("SELECT key, value FROM data")
                    rows = cursor.fetchall()
                    
                    for key, value in rows:
                        if isinstance(value, bytes):
                            value = value.decode('utf-8', errors='ignore')
                        
                        try:
                            data = json.loads(value)
                            if self._is_chat_data(data):
                                conv = self._parse_chat_json(data, "firefox_ls")
                                if conv and conv.id not in self.processed_ids:
                                    self.processed_ids.add(conv.id)
                                    self.conversations.append(conv)
                                    
                                    yield ScrapedItem(
                                        id=f"lmarena:firefox:ls:{conv.id}",
                                        source_type="lmarena",
                                        source_path=str(db_file),
                                        content=self._format_conversation(conv),
                                        content_type="chat_conversation",
                                        filename=f"lmarena_firefox_{conv.id[:16]}.md",
                                        metadata={
                                            "browser": "firefox",
                                            "chat_id": conv.id,
                                        },
                                        confidence_score=0.9
                                    )
                        except:
                            continue
                    
                    conn.close()
                    os.unlink(tmp_path)
                    
                except Exception as e:
                    continue
    
    async def _scan_exported_files(self, export_path: Path) -> AsyncIterator[ScrapedItem]:
        """Scan for exported chat files"""
        
        patterns = [
            "*lmarena*",
            "*lmsys*",
            "*arena*",
            "*chat*.json",
            "*conversation*.json",
            "*chat*.md",
            "*conversation*.md",
        ]
        
        try:
            for root, dirs, files in os.walk(export_path):
                # Skip system directories
                dirs[:] = [d for d in dirs if not d.startswith('.') and d not in [
                    'node_modules', '__pycache__', 'venv', '.git'
                ]]
                
                for filename in files:
                    filepath = Path(root) / filename
                    
                    # Check patterns
                    matches = any(filepath.match(p) for p in patterns)
                    matches = matches or any(
                        term in filename.lower() 
                        for term in ['lmarena', 'lmsys', 'arena', 'chatgpt', 'claude', 'gpt4']
                    )
                    
                    if not matches:
                        continue
                    
                    # Skip large files
                    try:
                        if filepath.stat().st_size > 50 * 1024 * 1024:  # 50MB
                            continue
                    except:
                        continue
                    
                    try:
                        async with aiofiles.open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            content = await f.read()
                        
                        # Try JSON
                        try:
                            data = json.loads(content)
                            if self._is_chat_data(data):
                                conv = self._parse_chat_json(data, "export")
                                if conv and conv.id not in self.processed_ids:
                                    self.processed_ids.add(conv.id)
                                    self.conversations.append(conv)
                                    
                                    yield ScrapedItem(
                                        id=f"lmarena:export:{conv.id}",
                                        source_type="lmarena",
                                        source_path=str(filepath),
                                        content=self._format_conversation(conv),
                                        content_type="chat_conversation",
                                        filename=filepath.name,
                                        metadata={
                                            "source": "export",
                                            "original_path": str(filepath),
                                        },
                                        confidence_score=0.95
                                    )
                        except json.JSONDecodeError:
                            # Not JSON, check if contains code blocks
                            if '```' in content:
                                file_id = self._generate_id(content)
                                if file_id not in self.processed_ids:
                                    self.processed_ids.add(file_id)
                                    
                                    yield ScrapedItem(
                                        id=f"lmarena:export:md:{file_id}",
                                        source_type="lmarena",
                                        source_path=str(filepath),
                                        content=content,
                                        content_type="chat_export",
                                        filename=filepath.name,
                                        metadata={
                                            "source": "export",
                                            "format": "markdown",
                                        },
                                        confidence_score=0.8
                                    )
                                    
                    except Exception as e:
                        continue
                        
        except Exception as e:
            logger.debug(f"Error scanning exports: {e}")
    
    async def _extract_all_code_blocks(self) -> AsyncIterator[ScrapedItem]:
        """Extract code blocks from all conversations"""
        
        for conv in self.conversations:
            code_blocks = []
            
            for msg in conv.messages:
                blocks = self._extract_code_blocks(msg.content)
                code_blocks.extend(blocks)
            
            for i, block in enumerate(code_blocks):
                yield ScrapedItem(
                    id=f"lmarena:code:{conv.id}:{i}",
                    source_type="lmarena_code",
                    source_path=f"lmarena:{conv.id}",
                    content=block['code'],
                    content_type="source_code",
                    filename=f"{conv.id[:8]}_code_{i}.{block['extension']}",
                    language=block['language'],
                    metadata={
                        "chat_id": conv.id,
                        "block_index": i,
                        "language": block['language'],
                        "source": "lmarena_extraction",
                    },
                    confidence_score=1.0
                )
    
    # =========================================================================
    # Helper Methods
    # =========================================================================
    
    def _extract_json_from_binary(self, content: str) -> List[Dict]:
        """Extract JSON objects from binary/text content"""
        results = []
        
        # Find JSON objects
        brace_count = 0
        start_idx = None
        
        for i, char in enumerate(content):
            if char == '{':
                if brace_count == 0:
                    start_idx = i
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0 and start_idx is not None:
                    try:
                        json_str = content[start_idx:i+1]
                        if len(json_str) > 50:  # Skip tiny objects
                            data = json.loads(json_str)
                            results.append(data)
                    except:
                        pass
                    start_idx = None
        
        return results
    
    def _is_chat_data(self, data: Any) -> bool:
        """Check if data looks like chat/conversation data"""
        if not isinstance(data, dict):
            return False
        
        # Common chat data indicators
        indicators = [
            'messages' in data,
            'conversation' in data,
            'chat' in data,
            'prompt' in data and 'response' in data,
            'user' in data and 'assistant' in data,
            'human' in data and 'ai' in data,
        ]
        
        if any(indicators):
            return True
        
        # Check for message-like structure in values
        for value in data.values():
            if isinstance(value, list) and len(value) > 0:
                if isinstance(value[0], dict):
                    if any(k in value[0] for k in ['role', 'content', 'message', 'text']):
                        return True
        
        return False
    
    def _parse_chat_json(self, data: Dict, source: str) -> Optional[ChatConversation]:
        """Parse JSON data into ChatConversation"""
        try:
            conv_id = (
                data.get('id') or 
                data.get('conversation_id') or 
                data.get('chat_id') or
                self._generate_id(json.dumps(data))
            )
            
            messages = []
            
            # Try different message formats
            msg_data = (
                data.get('messages') or 
                data.get('conversation') or 
                data.get('chat') or
                []
            )
            
            if isinstance(msg_data, list):
                for msg in msg_data:
                    if isinstance(msg, dict):
                        role = msg.get('role', msg.get('sender', msg.get('type', 'unknown')))
                        content = msg.get('content', msg.get('message', msg.get('text', '')))
                        model = msg.get('model', msg.get('model_name', None))
                        
                        if content:
                            messages.append(ChatMessage(
                                role=str(role),
                                content=str(content),
                                model=model
                            ))
            
            if not messages:
                return None
            
            # Extract models used
            models = list(set(m.model for m in messages if m.model))
            
            return ChatConversation(
                id=str(conv_id),
                messages=messages,
                models=models,
                source=source,
                raw_data=data
            )
            
        except Exception as e:
            return None
    
    def _format_conversation(self, conv: ChatConversation) -> str:
        """Format conversation as markdown"""
        lines = [
            f"# LM Arena Conversation",
            f"",
            f"**ID:** `{conv.id}`",
            f"**Source:** {conv.source}",
        ]
        
        if conv.models:
            lines.append(f"**Models:** {', '.join(conv.models)}")
        
        lines.append(f"**Messages:** {len(conv.messages)}")
        lines.append("")
        lines.append("---")
        lines.append("")
        
        for i, msg in enumerate(conv.messages):
            role = msg.role.upper()
            model_info = f" ({msg.model})" if msg.model else ""
            
            lines.append(f"## {role}{model_info}")
            lines.append("")
            lines.append(msg.content)
            lines.append("")
        
        return "\n".join(lines)
    
    def _extract_code_blocks(self, content: str) -> List[Dict[str, str]]:
        """Extract code blocks from content"""
        blocks = []
        
        pattern = r'```(\w*)\n(.*?)```'
        matches = re.findall(pattern, content, re.DOTALL)
        
        lang_to_ext = {
            'python': 'py', 'py': 'py',
            'javascript': 'js', 'js': 'js',
            'typescript': 'ts', 'ts': 'ts',
            'sql': 'sql',
            'json': 'json',
            'yaml': 'yaml', 'yml': 'yaml',
            'bash': 'sh', 'shell': 'sh', 'sh': 'sh',
            'r': 'R',
            'html': 'html',
            'css': 'css',
            'rust': 'rs',
            'go': 'go',
            'java': 'java',
            'cpp': 'cpp', 'c++': 'cpp',
            'c': 'c',
            'dockerfile': 'dockerfile',
        }
        
        for lang, code in matches:
            lang = lang.lower().strip() if lang else 'text'
            blocks.append({
                'language': lang,
                'extension': lang_to_ext.get(lang, 'txt'),
                'code': code.strip()
            })
        
        return blocks
    
    def _extract_chat_id_from_url(self, url: str) -> Optional[str]:
        """Extract chat ID from URL"""
        patterns = [
            r'/c/([a-f0-9-]+)',
            r'/chat/([a-f0-9-]+)',
            r'/conversation/([a-f0-9-]+)',
            r'id=([a-f0-9-]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        
        return None
    
    def _extract_conversations_from_text(self, text: str) -> List[str]:
        """Extract conversation-like text patterns"""
        conversations = []
        
        # Look for patterns like "User: ... Assistant: ..."
        patterns = [
            r'((?:User|Human|You):\s*.*?(?:Assistant|AI|Bot|Claude|GPT):\s*.*?)(?=(?:User|Human|You):|$)',
            r'((?:\*\*User\*\*|\*\*Human\*\*).*?(?:\*\*Assistant\*\*|\*\*AI\*\*).*?)(?=\*\*User\*\*|\*\*Human\*\*|$)',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text, re.DOTALL | re.IGNORECASE)
            for match in matches:
                if len(match) > 100:  # Skip tiny matches
                    conversations.append(match.strip())
        
        return conversations
    
    def _generate_id(self, content: str) -> str:
        """Generate a unique ID from content"""
        import hashlib
        return hashlib.sha256(content.encode()).hexdigest()[:24]

2. Specialized Processors for Agents/Databases/Prompts

Python

# recovery/processors/agent_processor.py
"""
Specialized processor for Agent code recovery
"""

import re
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from pathlib import Path


@dataclass
class ExtractedAgent:
    class_name: str
    agent_id: str
    agency: str
    description: str
    methods: List[Dict[str, str]]
    tools: List[Dict[str, Any]]
    imports: List[str]
    full_code: str
    dependencies: List[str]


class AgentProcessor:
    """
    Extracts and processes agent code from various sources.
    
    Identifies:
    - Agent class definitions
    - Tool definitions
    - MCP integrations
    - Dependencies
    """
    
    # Patterns to identify agent code
    AGENT_PATTERNS = [
        r'class\s+(\w+)\s*\([^)]*BaseAgent[^)]*\)',
        r'class\s+(\w+Agent)\s*\(',
        r'agent_id\s*=\s*["\']([^"\']+)["\']',
        r'async\s+def\s+execute_task\s*\(',
        r'def\s+get_tools\s*\(',
    ]
    
    TOOL_PATTERN = r'\{\s*["\']name["\']\s*:\s*["\']([^"\']+)["\']'
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.extracted_agents: List[ExtractedAgent] = []
    
    def process(self, content: str, source_info: Dict) -> Optional[ExtractedAgent]:
        """Process content to extract agent code"""
        
        # Check if this looks like agent code
        if not self._is_agent_code(content):
            return None
        
        try:
            return self._extract_agent(content, source_info)
        except Exception as e:
            return None
    
    def _is_agent_code(self, content: str) -> bool:
        """Check if content contains agent code"""
        score = 0
        
        if 'BaseAgent' in content:
            score += 3
        if 'execute_task' in content:
            score += 2
        if 'get_tools' in content:
            score += 2
        if 'agent_id' in content:
            score += 1
        if 'async def' in content:
            score += 1
        if 'class' in content and 'Agent' in content:
            score += 2
        
        return score >= 3
    
    def _extract_agent(self, content: str, source_info: Dict) -> ExtractedAgent:
        """Extract agent details from code"""
        
        # Extract class name
        class_match = re.search(r'class\s+(\w+)\s*\(', content)
        class_name = class_match.group(1) if class_match else "UnknownAgent"
        
        # Extract agent_id
        id_match = re.search(r'agent_id\s*=\s*["\']([^"\']+)["\']', content)
        agent_id = id_match.group(1) if id_match else class_name.lower()
        
        # Extract agency
        agency_match = re.search(r'agency\s*=\s*["\']([^"\']+)["\']', content)
        agency = agency_match.group(1) if agency_match else "unknown"
        
        # Extract description
        desc_match = re.search(r'description\s*=\s*["\']([^"\']+)["\']', content)
        description = desc_match.group(1) if desc_match else ""
        
        # Extract methods
        methods = self._extract_methods(content)
        
        # Extract tools
        tools = self._extract_tools(content)
        
        # Extract imports
        imports = self._extract_imports(content)
        
        # Extract dependencies
        deps = self._extract_dependencies(content)
        
        agent = ExtractedAgent(
            class_name=class_name,
            agent_id=agent_id,
            agency=agency,
            description=description,
            methods=methods,
            tools=tools,
            imports=imports,
            full_code=content,
            dependencies=deps
        )
        
        self.extracted_agents.append(agent)
        return agent
    
    def _extract_methods(self, content: str) -> List[Dict[str, str]]:
        """Extract method definitions"""
        methods = []
        
        pattern = r'(async\s+)?def\s+(\w+)\s*\(([^)]*)\)(?:\s*->\s*([^:]+))?:'
        
        for match in re.finditer(pattern, content):
            is_async = bool(match.group(1))
            name = match.group(2)
            params = match.group(3)
            return_type = match.group(4)
            
            # Get docstring
            docstring = self._extract_docstring(content, match.end())
            
            methods.append({
                "name": name,
                "async": is_async,
                "params": params.strip(),
                "return_type": return_type.strip() if return_type else None,
                "docstring": docstring
            })
        
        return methods
    
    def _extract_docstring(self, content: str, start_pos: int) -> Optional[str]:
        """Extract docstring after function definition"""
        remaining = content[start_pos:start_pos + 500]
        
        # Look for triple quotes
        match = re.search(r'"""(.*?)"""', remaining, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        match = re.search(r"'''(.*?)'''", remaining, re.DOTALL)
        if match:
            return match.group(1).strip()
        
        return None
    
    def _extract_tools(self, content: str) -> List[Dict[str, Any]]:
        """Extract tool definitions"""
        tools = []
        
        # Look for get_tools method
        get_tools_match = re.search(
            r'def\s+get_tools\s*\([^)]*\)\s*(?:->[^:]+)?:\s*.*?return\s*\[(.*?)\]',
            content,
            re.DOTALL
        )
        
        if get_tools_match:
            tools_str = get_tools_match.group(1)
            
            # Extract individual tool dicts
            tool_pattern = r'\{[^{}]+\}'
            for match in re.finditer(tool_pattern, tools_str, re.DOTALL):
                try:
                    # Try to parse as Python dict
                    tool_str = match.group()
                    tool_str = tool_str.replace("'", '"')
                    tool_str = re.sub(r'(\w+):', r'"\1":', tool_str)
                    
                    import json
                    tool = json.loads(tool_str)
                    tools.append(tool)
                except:
                    # Just extract name
                    name_match = re.search(r'["\']name["\']\s*:\s*["\']([^"\']+)["\']', match.group())
                    if name_match:
                        tools.append({"name": name_match.group(1)})
        
        return tools
    
    def _extract_imports(self, content: str) -> List[str]:
        """Extract import statements"""
        imports = []
        
        for line in content.split('\n'):
            line = line.strip()
            if line.startswith('import ') or line.startswith('from '):
                imports.append(line)
        
        return imports
    
    def _extract_dependencies(self, content: str) -> List[str]:
        """Extract external dependencies"""
        deps = set()
        
        for line in content.split('\n'):
            if line.startswith('import '):
                module = line.split()[1].split('.')[0]
                deps.add(module)
            elif line.startswith('from '):
                module = line.split()[1].split('.')[0]
                deps.add(module)
        
        # Filter out standard library
        stdlib = {
            'os', 'sys', 'json', 're', 'typing', 'pathlib', 'datetime',
            'asyncio', 'collections', 'functools', 'itertools', 'logging',
            'dataclasses', 'abc', 'enum', 'copy', 'io', 'time', 'hashlib',
            'tempfile', 'shutil', 'subprocess', 'threading', 'multiprocessing'
        }
        
        return [d for d in deps if d not in stdlib]
    
    def get_agent_summary(self) -> Dict[str, Any]:
        """Get summary of all extracted agents"""
        return {
            "total_agents": len(self.extracted_agents),
            "agents": [
                {
                    "class": a.class_name,
                    "id": a.agent_id,
                    "agency": a.agency,
                    "methods": len(a.methods),
                    "tools": len(a.tools),
                }
                for a in self.extracted_agents
            ],
            "all_tools": [
                t for a in self.extracted_agents 
                for t in a.tools
            ],
            "all_dependencies": list(set(
                d for a in self.extracted_agents 
                for d in a.dependencies
            ))
        }

Python

# recovery/processors/database_processor.py
"""
Specialized processor for Database schema recovery
"""

import re
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class ExtractedTable:
    name: str
    columns: List[Dict[str, str]]
    primary_key: Optional[str]
    foreign_keys: List[Dict[str, str]]
    indexes: List[str]
    constraints: List[str]
    full_sql: str


@dataclass
class ExtractedSchema:
    tables: List[ExtractedTable]
    functions: List[Dict[str, str]]
    indexes: List[str]
    comments: List[str]
    full_sql: str


class DatabaseProcessor:
    """
    Extracts and processes database schemas from SQL content.
    
    Handles:
    - CREATE TABLE statements
    - Column definitions
    - Indexes
    - Functions
    - Comments
    """
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.extracted_schemas: List[ExtractedSchema] = []
    
    def process(self, content: str, source_info: Dict) -> Optional[ExtractedSchema]:
        """Process SQL content"""
        
        if not self._is_sql_schema(content):
            return None
        
        try:
            return self._extract_schema(content)
        except Exception as e:
            return None
    
    def _is_sql_schema(self, content: str) -> bool:
        """Check if content contains SQL schema"""
        indicators = [
            'CREATE TABLE',
            'CREATE INDEX',
            'ALTER TABLE',
            'PRIMARY KEY',
            'FOREIGN KEY',
            'REFERENCES',
        ]
        
        content_upper = content.upper()
        return sum(1 for ind in indicators if ind in content_upper) >= 2
    
    def _extract_schema(self, content: str) -> ExtractedSchema:
        """Extract schema details"""
        
        tables = self._extract_tables(content)
        functions = self._extract_functions(content)
        indexes = self._extract_indexes(content)
        comments = self._extract_comments(content)
        
        schema = ExtractedSchema(
            tables=tables,
            functions=functions,
            indexes=indexes,
            comments=comments,
            full_sql=content
        )
        
        self.extracted_schemas.append(schema)
        return schema
    
    def _extract_tables(self, content: str) -> List[ExtractedTable]:
        """Extract CREATE TABLE statements"""
        tables = []
        
        # Pattern to match CREATE TABLE
        pattern = r'CREATE\s+TABLE\s+(?:IF\s+NOT\s+EXISTS\s+)?(\w+)\s*\((.*?)\);'
        
        for match in re.finditer(pattern, content, re.DOTALL | re.IGNORECASE):
            table_name = match.group(1)
            table_body = match.group(2)
            
            columns = self._parse_columns(table_body)
            primary_key = self._find_primary_key(table_body)
            foreign_keys = self._find_foreign_keys(table_body)
            constraints = self._find_constraints(table_body)
            
            tables.append(ExtractedTable(
                name=table_name,
                columns=columns,
                primary_key=primary_key,
                foreign_keys=foreign_keys,
                indexes=[],
                constraints=constraints,
                full_sql=match.group(0)
            ))
        
        return tables
    
    def _parse_columns(self, table_body: str) -> List[Dict[str, str]]:
        """Parse column definitions"""
        columns = []
        
        # Split by comma, but not inside parentheses
        parts = self._split_respecting_parens(table_body)
        
        for part in parts:
            part = part.strip()
            
            # Skip constraints
            if any(kw in part.upper() for kw in ['PRIMARY KEY', 'FOREIGN KEY', 'UNIQUE', 'CHECK', 'CONSTRAINT']):
                continue
            
            # Parse column: name TYPE ...
            match = re.match(r'(\w+)\s+(\w+(?:\([^)]+\))?)\s*(.*)', part, re.IGNORECASE)
            if match:
                columns.append({
                    "name": match.group(1),
                    "type": match.group(2),
                    "constraints": match.group(3).strip()
                })
        
        return columns
    
    def _split_respecting_parens(self, s: str) -> List[str]:
        """Split by comma, respecting parentheses"""
        parts = []
        current = ""
        depth = 0
        
        for char in s:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
            elif char == ',' and depth == 0:
                parts.append(current.strip())
                current = ""
                continue
            current += char
        
        if current.strip():
            parts.append(current.strip())
        
        return parts
    
    def _find_primary_key(self, table_body: str) -> Optional[str]:
        """Find primary key"""
        # Inline PRIMARY KEY
        match = re.search(r'(\w+)\s+[^,]+PRIMARY\s+KEY', table_body, re.IGNORECASE)
        if match:
            return match.group(1)
        
        # Separate PRIMARY KEY constraint
        match = re.search(r'PRIMARY\s+KEY\s*\(([^)]+)\)', table_body, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        
        return None
    
    def _find_foreign_keys(self, table_body: str) -> List[Dict[str, str]]:
        """Find foreign key constraints"""
        fks = []
        
        pattern = r'FOREIGN\s+KEY\s*\(([^)]+)\)\s*REFERENCES\s+(\w+)\s*\(([^)]+)\)'
        
        for match in re.finditer(pattern, table_body, re.IGNORECASE):
            fks.append({
                "column": match.group(1).strip(),
                "references_table": match.group(2).strip(),
                "references_column": match.group(3).strip()
            })
        
        return fks
    
    def _find_constraints(self, table_body: str) -> List[str]:
        """Find other constraints"""
        constraints = []
        
        for kw in ['UNIQUE', 'CHECK', 'NOT NULL', 'DEFAULT']:
            if kw in table_body.upper():
                constraints.append(kw)
        
        return constraints
    
    def _extract_functions(self, content: str) -> List[Dict[str, str]]:
        """Extract function definitions"""
        functions = []
        
        pattern = r'CREATE\s+(?:OR\s+REPLACE\s+)?FUNCTION\s+(\w+)\s*\(([^)]*)\)\s*RETURNS\s+(\w+)'
        
        for match in re.finditer(pattern, content, re.IGNORECASE):
            functions.append({
                "name": match.group(1),
                "params": match.group(2).strip(),
                "returns": match.group(3)
            })
        
        return functions
    
    def _extract_indexes(self, content: str) -> List[str]:
        """Extract index definitions"""
        indexes = []
        
        pattern = r'CREATE\s+(?:UNIQUE\s+)?INDEX\s+(?:IF\s+NOT\s+EXISTS\s+)?(\w+)\s+ON\s+(\w+)'
        
        for match in re.finditer(pattern, content, re.IGNORECASE):
            indexes.append(f"{match.group(1)} ON {match.group(2)}")
        
        return indexes
    
    def _extract_comments(self, content: str) -> List[str]:
        """Extract SQL comments"""
        comments = []
        
        # Single line comments
        for match in re.finditer(r'--\s*(.+)$', content, re.MULTILINE):
            comments.append(match.group(1).strip())
        
        return comments
    
    def get_schema_summary(self) -> Dict[str, Any]:
        """Get summary of all extracted schemas"""
        all_tables = [t for s in self.extracted_schemas for t in s.tables]
        
        return {
            "total_schemas": len(self.extracted_schemas),
            "total_tables": len(all_tables),
            "tables": [
                {
                    "name": t.name,
                    "columns": len(t.columns),
                    "primary_key": t.primary_key,
                    "foreign_keys": len(t.foreign_keys),
                }
                for t in all_tables
            ],
            "all_columns": [
                {"table": t.name, **c}
                for t in all_tables
                for c in t.columns
            ]
        }

Python

# recovery/processors/prompt_processor.py
"""
Specialized processor for Prompt template recovery
"""

import re
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class ExtractedPrompt:
    name: str
    prompt_type: str  # system, user, assistant, template
    content: str
    variables: List[str]
    agent_context: Optional[str]
    full_definition: str


class PromptProcessor:
    """
    Extracts and processes prompt templates.
    
    Identifies:
    - SYSTEM_PROMPT definitions
    - Template strings with variables
    - F-strings with placeholders
    - Jinja-style templates
    """
    
    PROMPT_PATTERNS = [
        (r'(\w*SYSTEM_PROMPT\w*)\s*=\s*["\'\`]{1,3}(.*?)["\'\`]{1,3}', 'system'),
        (r'(\w*USER_PROMPT\w*)\s*=\s*["\'\`]{1,3}(.*?)["\'\`]{1,3}', 'user'),
        (r'(\w*ASSISTANT_PROMPT\w*)\s*=\s*["\'\`]{1,3}(.*?)["\'\`]{1,3}', 'assistant'),
        (r'(\w*PROMPT\w*)\s*=\s*["\'\`]{1,3}(.*?)["\'\`]{1,3}', 'template'),
        (r'(\w*TEMPLATE\w*)\s*=\s*["\'\`]{1,3}(.*?)["\'\`]{1,3}', 'template'),
    ]
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.extracted_prompts: List[ExtractedPrompt] = []
    
    def process(self, content: str, source_info: Dict) -> List[ExtractedPrompt]:
        """Process content to extract prompts"""
        prompts = []
        
        # Try each pattern
        for pattern, prompt_type in self.PROMPT_PATTERNS:
            for match in re.finditer(pattern, content, re.DOTALL | re.IGNORECASE):
                name = match.group(1)
                prompt_content = match.group(2)
                
                variables = self._extract_variables(prompt_content)
                
                prompt = ExtractedPrompt(
                    name=name,
                    prompt_type=prompt_type,
                    content=prompt_content,
                    variables=variables,
                    agent_context=source_info.get('agent_id'),
                    full_definition=match.group(0)
                )
                
                prompts.append(prompt)
                self.extracted_prompts.append(prompt)
        
        # Also look for inline prompts in method calls
        inline_prompts = self._extract_inline_prompts(content)
        prompts.extend(inline_prompts)
        
        return prompts
    
    def _extract_variables(self, content: str) -> List[str]:
        """Extract template variables"""
        variables = set()
        
        # F-string style: {variable}
        for match in re.finditer(r'\{(\w+)\}', content):
            variables.add(match.group(1))
        
        # Jinja style: {{ variable }}
        for match in re.finditer(r'\{\{\s*(\w+)\s*\}\}', content):
            variables.add(match.group(1))
        
        # Python format: %(variable)s
        for match in re.finditer(r'%\((\w+)\)', content):
            variables.add(match.group(1))
        
        return list(variables)
    
    def _extract_inline_prompts(self, content: str) -> List[ExtractedPrompt]:
        """Extract prompts from method calls"""
        prompts = []
        
        # Look for .format() or f-strings in specific contexts
        patterns = [
            r'system_prompt\s*=\s*f?["\'\`]{1,3}(.*?)["\'\`]{1,3}',
            r'user_prompt\s*=\s*f?["\'\`]{1,3}(.*?)["\'\`]{1,3}',
            r'prompt\s*=\s*f?["\'\`]{1,3}(.*?)["\'\`]{1,3}',
            r'\.generate\([^)]*prompt\s*=\s*f?["\'\`]{1,3}(.*?)["\'\`]{1,3}',
        ]
        
        for pattern in patterns:
            for match in re.finditer(pattern, content, re.DOTALL):
                prompt_content = match.group(1)
                if len(prompt_content) > 50:  # Skip trivial strings
                    prompts.append(ExtractedPrompt(
                        name=f"inline_prompt_{len(prompts)}",
                        prompt_type="inline",
                        content=prompt_content,
                        variables=self._extract_variables(prompt_content),
                        agent_context=None,
                        full_definition=match.group(0)
                    ))
        
        return prompts
    
    def get_prompt_summary(self) -> Dict[str, Any]:
        """Get summary of all extracted prompts"""
        by_type = {}
        for p in self.extracted_prompts:
            by_type.setdefault(p.prompt_type, []).append(p.name)
        
        return {
            "total_prompts": len(self.extracted_prompts),
            "by_type": {k: len(v) for k, v in by_type.items()},
            "prompts": [
                {
                    "name": p.name,
                    "type": p.prompt_type,
                    "variables": p.variables,
                    "length": len(p.content),
                }
                for p in self.extracted_prompts
            ],
            "all_variables": list(set(
                v for p in self.extracted_prompts 
                for v in p.variables
            ))
        }

3. Focused Recovery Pipeline

Python

# recovery/focused_recovery.py
"""
Focused Recovery for Agents, Databases, Prompts, and Code Snippets
"""

import asyncio
import os
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime
import json

from loguru import logger
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.table import Table
from rich.panel import Panel

from recovery.scrapers.lmarena_full_history import LMArenaFullHistoryScraper
from recovery.processors.agent_processor import AgentProcessor
from recovery.processors.database_processor import DatabaseProcessor
from recovery.processors.prompt_processor import PromptProcessor

console = Console()


class FocusedRecovery:
    """
    Focused recovery targeting:
    1. Agent definitions
    2. Database schemas
    3. Prompt templates
    4. Code snippets (from LM Arena)
    5. Workflow definitions
    """
    
    def __init__(self, username: str = "eguid"):
        self.username = username
        self.output_dir = Path(f"C:/Users/{username}/Desktop/CLAUDE RECOMENDATIONS/recovered")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Initialize scrapers
        self.lmarena_scraper = LMArenaFullHistoryScraper(username)
        
        # Initialize processors
        self.agent_processor = AgentProcessor({})
        self.database_processor = DatabaseProcessor({})
        self.prompt_processor = PromptProcessor({})
        
        # Storage
        self.recovered_agents = []
        self.recovered_schemas = []
        self.recovered_prompts = []
        self.recovered_code = []
        self.recovered_workflows = []
    
    async def run_full_recovery(self) -> Dict[str, Any]:
        """Run complete focused recovery"""
        
        console.print(Panel.fit(
            "[bold blue]🔍 FOCUSED RECOVERY[/bold blue]\n\n"
            "Targeting:\n"
            "  • Agent definitions\n"
            "  • Database schemas\n"
            "  • Prompt templates\n"
            "  • Code snippets\n"
            "  • Workflows",
            border_style="blue"
        ))
        
        results = {
            "started_at": datetime.now().isoformat(),
            "agents": 0,
            "schemas": 0,
            "prompts": 0,
            "code_blocks": 0,
            "workflows": 0,
            "total_items": 0,
        }
        
        # 1. Extract from LM Arena (your chat history)
        console.print("\n[bold cyan]Phase 1: Extracting LM Arena History[/bold cyan]")
        await self._extract_lmarena(results)
        
        # 2. Scan file locations
        console.print("\n[bold cyan]Phase 2: Scanning File Locations[/bold cyan]")
        await self._scan_file_locations(results)
        
        # 3. Process and classify
        console.print("\n[bold cyan]Phase 3: Processing & Classification[/bold cyan]")
        self._process_all(results)
        
        # 4. Save results
        console.print("\n[bold cyan]Phase 4: Saving Results[/bold cyan]")
        self._save_results(results)
        
        # Display summary
        self._display_summary(results)
        
        return results
    
    async def _extract_lmarena(self, results: Dict):
        """Extract from LM Arena"""
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Scanning browser data...", total=None)
            
            async for item in self.lmarena_scraper.scrape_all():
                results["total_items"] += 1
                
                # Process immediately based on content
                content = item.content
                
                # Check for agent code
                if self.agent_processor._is_agent_code(content):
                    agent = self.agent_processor.process(content, {"source": item.source_path})
                    if agent:
                        self.recovered_agents.append({
                            "agent": agent,
                            "source": item
                        })
                        results["agents"] += 1
                
                # Check for SQL
                if self.database_processor._is_sql_schema(content):
                    schema = self.database_processor.process(content, {"source": item.source_path})
                    if schema:
                        self.recovered_schemas.append({
                            "schema": schema,
                            "source": item
                        })
                        results["schemas"] += 1
                
                # Check for prompts
                prompts = self.prompt_processor.process(content, {"source": item.source_path})
                if prompts:
                    for prompt in prompts:
                        self.recovered_prompts.append({
                            "prompt": prompt,
                            "source": item
                        })
                        results["prompts"] += 1
                
                # Store code blocks
                if item.content_type == "source_code":
                    self.recovered_code.append(item)
                    results["code_blocks"] += 1
                
                # Check for workflows
                if '"workflow_id"' in content or '"steps":' in content:
                    self.recovered_workflows.append(item)
                    results["workflows"] += 1
                
                progress.update(task, description=f"Found {results['total_items']} items...")
    
    async def _scan_file_locations(self, results: Dict):
        """Scan file locations"""
        
        locations = [
            Path("G:/restored"),
            Path(f"C:/Users/{self.username}/OneDrive/Desktop"),
            Path(f"C:/Users/{self.username}/OneDrive/Documents"),
            Path(f"C:/Users/{self.username}/OneDrive/AppData"),
            Path(f"C:/Users/{self.username}/Documents"),
            Path(f"C:/Users/{self.username}/Desktop"),
            Path(f"\\\\wsl.localhost\\Ubuntu\\home\\{self.username}"),
        ]
        
        patterns = {
            "agent": ["*agent*.py", "*_agent.py"],
            "schema": ["*.sql", "*schema*.sql"],
            "prompt": ["*prompt*.py", "*prompts*.py"],
            "workflow": ["*workflow*.json", "*workflow*.yaml"],
        }
        
        for location in locations:
            if not location.exists():
                continue
            
            console.print(f"  Scanning: {location}")
            
            try:
                for category, file_patterns in patterns.items():
                    for pattern in file_patterns:
                        for filepath in location.rglob(pattern):
                            try:
                                content = filepath.read_text(encoding='utf-8', errors='ignore')
                                
                                if category == "agent" and self.agent_processor._is_agent_code(content):
                                    agent = self.agent_processor.process(content, {"path": str(filepath)})
                                    if agent:
                                        self.recovered_agents.append({
                                            "agent": agent,
                                            "path": str(filepath)
                                        })
                                        results["agents"] += 1
                                
                                elif category == "schema" and self.database_processor._is_sql_schema(content):
                                    schema = self.database_processor.process(content, {"path": str(filepath)})
                                    if schema:
                                        self.recovered_schemas.append({
                                            "schema": schema,
                                            "path": str(filepath)
                                        })
                                        results["schemas"] += 1
                                        
                            except Exception as e:
                                continue
                                
            except Exception as e:
                logger.debug(f"Error scanning {location}: {e}")
    
    def _process_all(self, results: Dict):
        """Additional processing"""
        # Deduplicate
        seen_agents = set()
        unique_agents = []
        for item in self.recovered_agents:
            agent_id = item["agent"].agent_id
            if agent_id not in seen_agents:
                seen_agents.add(agent_id)
                unique_agents.append(item)
        self.recovered_agents = unique_agents
        results["agents"] = len(unique_agents)
        
        # Similar for others...
    
    def _save_results(self, results: Dict):
        """Save recovered items to files"""
        
        # Create output structure
        agents_dir = self.output_dir / "agents"
        schemas_dir = self.output_dir / "schemas"
        prompts_dir = self.output_dir / "prompts"
        code_dir = self.output_dir / "code"
        workflows_dir = self.output_dir / "workflows"
        
        for d in [agents_dir, schemas_dir, prompts_dir, code_dir, workflows_dir]:
            d.mkdir(parents=True, exist_ok=True)
        
        # Save agents
        for item in self.recovered_agents:
            agent = item["agent"]
            filepath = agents_dir / f"{agent.class_name}.py"
            filepath.write_text(agent.full_code, encoding='utf-8')
            
            # Also save metadata
            meta_path = agents_dir / f"{agent.class_name}.json"
            meta_path.write_text(json.dumps({
                "class_name": agent.class_name,
                "agent_id": agent.agent_id,
                "agency": agent.agency,
                "description": agent.description,
                "methods": agent.methods,
                "tools": agent.tools,
                "dependencies": agent.dependencies,
            }, indent=2), encoding='utf-8')
        
        # Save schemas
        for i, item in enumerate(self.recovered_schemas):
            schema = item["schema"]
            
            # Name based on tables
            if schema.tables:
                name = "_".join(t.name for t in schema.tables[:3])
            else:
                name = f"schema_{i}"
            
            filepath = schemas_dir / f"{name}.sql"
            filepath.write_text(schema.full_sql, encoding='utf-8')
        
        # Save prompts
        prompts_data = []
        for item in self.recovered_prompts:
            prompt = item["prompt"]
            prompts_data.append({
                "name": prompt.name,
                "type": prompt.prompt_type,
                "content": prompt.content,
                "variables": prompt.variables,
            })
        
        prompts_file = prompts_dir / "all_prompts.json"
        prompts_file.write_text(json.dumps(prompts_data, indent=2), encoding='utf-8')
        
        # Save individual prompt files
        for item in self.recovered_prompts:
            prompt = item["prompt"]
            filepath = prompts_dir / f"{prompt.name}.txt"
            filepath.write_text(prompt.content, encoding='utf-8')
        
        # Save code blocks
        for item in self.recovered_code:
            filename = item.filename or f"code_{item.id[:16]}.txt"
            filepath = code_dir / filename
            filepath.write_text(item.content, encoding='utf-8')
        
        # Save workflows
        for item in self.recovered_workflows:
            filename = item.filename or f"workflow_{item.id[:16]}.json"
            filepath = workflows_dir / filename
            filepath.write_text(item.content, encoding='utf-8')
        
        # Save summary
        summary = {
            "recovered_at": datetime.now().isoformat(),
            "agents": results["agents"],
            "schemas": results["schemas"],
            "prompts": results["prompts"],
            "code_blocks": results["code_blocks"],
            "workflows": results["workflows"],
            "agent_list": [a["agent"].class_name for a in self.recovered_agents],
            "schema_tables": [t.name for s in self.recovered_schemas for t in s["schema"].tables],
        }
        
        summary_path = self.output_dir / "recovery_summary.json"
        summary_path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
        
        console.print(f"  [green]✓ Saved to: {self.output_dir}[/green]")
    
    def _display_summary(self, results: Dict):
        """Display recovery summary"""
        
        table = Table(title="Recovery Summary")
        table.add_column("Category", style="cyan")
        table.add_column("Count", style="green")
        table.add_column("Details")
        
        table.add_row(
            "Agents",
            str(results["agents"]),
            ", ".join(a["agent"].class_name for a in self.recovered_agents[:5]) + 
            ("..." if len(self.recovered_agents) > 5 else "")
        )
        
        table.add_row(
            "Database Schemas",
            str(results["schemas"]),
            f"{sum(len(s['schema'].tables) for s in self.recovered_schemas)} tables"
        )
        
        table.add_row(
            "Prompts",
            str(results["prompts"]),
            ", ".join(set(p["prompt"].prompt_type for p in self.recovered_prompts))
        )
        
        table.add_row(
            "Code Blocks",
            str(results["code_blocks"]),
            f"Various languages"
        )
        
        table.add_row(
            "Workflows",
            str(results["workflows"]),
            ""
        )
        
        console.print()
        console.print(table)
        console.print()
        console.print(f"[bold green]Output saved to: {self.output_dir}[/bold green]")


async def main():
    """Run focused recovery"""
    recovery = FocusedRecovery()
    await recovery.run_full_recovery()


if __name__ == "__main__":
    asyncio.run(main())

4. Quick Run Script

Python

# scripts/run_recovery.py
"""
Quick script to run focused recovery
"""

import asyncio
import sys
from pathlib import Path

# Add project root
sys.path.insert(0, str(Path(__file__).parent.parent))

from recovery.focused_recovery import FocusedRecovery


async def main():
    print("=" * 60)
    print("MAMAAI - FOCUSED RECOVERY")
    print("=" * 60)
    print()
    print("Targeting:")
    print("  • Your complete LM Arena chat history")
    print("  • Agent definitions")
    print("  • Database schemas") 
    print("  • Prompt templates")
    print("  • Code snippets")
    print("  • Workflow definitions")
    print()
    print("Scanning locations:")
    print("  • All browser data (Chrome, Edge, Firefox)")
    print("  • G:\\restored")
    print("  • OneDrive folders")
    print("  • WSL filesystem")
    print()
    
    recovery = FocusedRecovery(username="eguid")
    results = await recovery.run_full_recovery()
    
    print()
    print("=" * 60)
    print("RECOVERY COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())

5. Run It

PowerShell

# PowerShell - Run the focused recovery

cd "C:\Users\eguid\Desktop\CLAUDE RECOMENDATIONS"

# Activate virtual environment
.\venv\Scripts\Activate

# Run focused recovery
python scripts/run_recovery.py

# Or run via main.py
python main.py recovery full

This will:

    Scan ALL your browser history for LM Arena chats (Chrome, Edge, Firefox)
    Extract from browser storage (LocalStorage, SessionStorage, IndexedDB, Cache)
    Find ALL chat URLs from browser history
    Extract code blocks from every conversation
    Identify and extract:
        Agent class definitions
        Database schemas (SQL)
        Prompt templates
        Workflow JSONs
    Save everything organized to recovered/ folder

The output structure will be:

text

recovered/
├── agents/
│   ├── VFXLayoutArtist.py
│   ├── VFXLayoutArtist.json
│   ├── CameraTrackingAgent.py
│   └── ...
├── schemas/
│   ├── blender_knowledge.sql
│   ├── compatibility_notes.sql
│   └── ...
├── prompts/
│   ├── all_prompts.json
│   ├── SYSTEM_PROMPT.txt
│   └── ...
├── code/
│   ├── code_block_1.py
│   ├── code_block_2.sql
│   └── ...
├── workflows/
│   ├── blender_compatibility_workflow.json
│   └── ...
└── recovery_summary.json

Would you like me to add any additional extraction patterns or target specific content?

the whle history off lm arena

structure is old its diferent now but similR
this is old
the agents databases prompts and those this was the hardest thing snipets partitions anything
claude-opus-4-5-20251101-thinking-32k
Complete VS Code Project for Your MamaAI Agency Recovery

Based on all the code and structures you've shared, I'll create a complete VS Code project that ties everything together with your specific locations and the Argilla-based recovery system.
Complete Project Structure

text

C:\Users\eguid\Desktop\CLAUDE RECOMENDATIONS\
├── .vscode/
│   ├── settings.json
│   ├── launch.json
│   ├── tasks.json
│   └── extensions.json
├── .env
├── .env.example
├── .gitignore
├── mama-ai-recovery.code-workspace
├── requirements.txt
├── docker-compose.yml
├── pyproject.toml
│
├── config/
│   ├── __init__.py
│   ├── environment.py
│   ├── settings.py
│   └── sources.yaml
│
├── secrets/
│   ├── __init__.py
│   ├── manager.py
│   └── .gitkeep
│
├── databases/
│   └── schemas/
│       ├── blender_knowledge_schema.sql
│       ├── compatibility_schema.sql
│       ├── tutorial_extraction_schema.sql
│       └── recovery_schema.sql
│
├── core/
│   ├── __init__.py
│   ├── base_agent.py
│   ├── database.py
│   └── mcp_client.py
│
├── agencies/
│   ├── __init__.py
│   ├── blender/
│   │   ├── __init__.py
│   │   └── vfx/
│   │       └── agents/
│   │           ├── __init__.py
│   │           ├── vfx_layout_artist.py
│   │           ├── camera_tracking_agent.py
│   │           ├── projection_mapping_agent.py
│   │           └── integration_agent.py
│   └── creative/
│       └── agents/
│           ├── __init__.py
│           ├── creative_director.py
│           └── scriptwriter.py
│
├── recovery/
│   ├── __init__.py
│   ├── pipeline.py
│   ├── scrapers/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── lmarena_scraper.py
│   │   ├── wsl_scraper.py
│   │   ├── onedrive_scraper.py
│   │   ├── restored_drive_scraper.py
│   │   └── github_scraper.py
│   ├── processors/
│   │   ├── __init__.py
│   │   ├── code_processor.py
│   │   ├── workflow_processor.py
│   │   └── schema_processor.py
│   └── storage/
│       ├── __init__.py
│       ├── vector_store.py
│       └── database.py
│
├── argilla_integration/
│   ├── __init__.py
│   ├── datasets.py
│   ├── labeling.py
│   └── export.py
│
├── mcp/
│   ├── servers/
│   │   ├── vfx_mcp_server.py
│   │   ├── creative_mcp_server.py
│   │   └── recovery_mcp_server.py
│   └── prompts/
│       ├── blender_prompts.py
│       ├── vfx_prompts.py
│       └── creative_prompts.py
│
├── workflows/
│   ├── blender_compatibility_workflow.json
│   ├── addon_reverse_engineering.json
│   ├── youtube_knowledge_extraction.json
│   └── commercial_revenue_gen.json
│
├── scripts/
│   ├── scrape_blender_official_docs.py
│   ├── extract_tutorials_to_workflows.py
│   ├── load_compatibility_data.py
│   ├── addon_pattern_extractor.py
│   └── run_recovery.py
│
├── api/
│   ├── __init__.py
│   ├── main.py
│   └── routes/
│       ├── recovery.py
│       ├── search.py
│       └── agents.py
│
├── ui/
│   └── dashboard.py
│
├── tests/
│   └── __init__.py
│
├── data/
│   ├── temp_vfx/
│   ├── generated/
│   └── exports/
│
├── logs/
│   └── .gitkeep
│
└── main.py

1. VS Code Workspace File

JSON

// mama-ai-recovery.code-workspace
{
    "folders": [
        {
            "name": "🤖 MamaAI Recovery System",
            "path": "."
        }
    ],
    "settings": {
        // Python
        "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe",
        "python.analysis.typeCheckingMode": "basic",
        "python.analysis.autoImportCompletions": true,
        "python.envFile": "${workspaceFolder}/.env",
        
        // Editor
        "editor.formatOnSave": true,
        "editor.rulers": [88, 120],
        "editor.tabSize": 4,
        
        // Files
        "files.exclude": {
            "**/__pycache__": true,
            "**/*.pyc": true,
            "**/venv": true
        },
        
        // Terminal
        "terminal.integrated.env.windows": {
            "PYTHONPATH": "${workspaceFolder}",
            "PROJECT_ROOT": "${workspaceFolder}"
        },
        
        // Search
        "search.exclude": {
            "**/venv": true,
            "**/data": true,
            "**/logs": true
        }
    },
    "extensions": {
        "recommendations": [
            "ms-python.python",
            "ms-python.vscode-pylance",
            "ms-toolsai.jupyter",
            "redhat.vscode-yaml",
            "mikestead.dotenv",
            "ms-azuretools.vscode-docker",
            "eamodio.gitlens",
            "usernamehw.errorlens",
            "gruntfuggly.todo-tree"
        ]
    },
    "launch": {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "🔍 Full Recovery Pipeline",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/main.py",
                "args": ["recovery", "full"],
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            },
            {
                "name": "💬 Scrape LM Arena Chats",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/main.py",
                "args": ["recovery", "source", "lmarena"],
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            },
            {
                "name": "🐧 Scrape WSL",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/main.py",
                "args": ["recovery", "source", "wsl"],
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            },
            {
                "name": "💾 Scrape Restored Drive",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/main.py",
                "args": ["recovery", "source", "restored"],
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            },
            {
                "name": "☁️ Scrape OneDrive",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/main.py",
                "args": ["recovery", "source", "onedrive"],
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            },
            {
                "name": "🌐 Run API Server",
                "type": "debugpy",
                "request": "launch",
                "module": "uvicorn",
                "args": ["api.main:app", "--reload", "--port", "8000"],
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            },
            {
                "name": "📊 Run Dashboard",
                "type": "debugpy",
                "request": "launch",
                "module": "streamlit",
                "args": ["run", "ui/dashboard.py", "--server.port", "8501"],
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            },
            {
                "name": "🔎 Interactive Search",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/main.py",
                "args": ["search"],
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            },
            {
                "name": "🗄️ Initialize Database",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/scripts/init_database.py",
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            },
            {
                "name": "📤 Export Curated Data",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/main.py",
                "args": ["export"],
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            },
            {
                "name": "🎬 VFX MCP Server",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/mcp/servers/vfx_mcp_server.py",
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            },
            {
                "name": "🎨 Creative MCP Server",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/mcp/servers/creative_mcp_server.py",
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            }
        ],
        "compounds": [
            {
                "name": "🔥 Full Stack",
                "configurations": ["🌐 Run API Server", "📊 Run Dashboard"]
            },
            {
                "name": "🔥 MCP Servers",
                "configurations": ["🎬 VFX MCP Server", "🎨 Creative MCP Server"]
            }
        ]
    },
    "tasks": {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "🐳 Docker Up",
                "type": "shell",
                "command": "docker-compose up -d",
                "problemMatcher": []
            },
            {
                "label": "🐳 Docker Down",
                "type": "shell",
                "command": "docker-compose down",
                "problemMatcher": []
            },
            {
                "label": "📦 Install Dependencies",
                "type": "shell",
                "command": "pip install -r requirements.txt",
                "problemMatcher": []
            },
            {
                "label": "🗄️ Run Migrations",
                "type": "shell",
                "command": "python scripts/init_database.py",
                "problemMatcher": []
            },
            {
                "label": "🔍 Run Full Recovery",
                "type": "shell",
                "command": "python main.py recovery full",
                "problemMatcher": [],
                "group": {
                    "kind": "build",
                    "isDefault": true
                }
            }
        ]
    }
}

2. Environment Configuration

Bash

# .env
# ============================================================
# MAMAAI AGENCY - PROJECT RECOVERY SYSTEM
# ============================================================
# Your specific configuration for eguid
# ============================================================

# ============================================================
# PROJECT PATHS
# ============================================================
PROJECT_ROOT=C:\Users\eguid\Desktop\CLAUDE RECOMENDATIONS
AGENCIES_ROOT=C:\Users\eguid\Desktop\CLAUDE RECOMENDATIONS\agencies
WORKFLOWS_DIR=C:\Users\eguid\Desktop\CLAUDE RECOMENDATIONS\workflows
SCRIPTS_DIR=C:\Users\eguid\Desktop\CLAUDE RECOMENDATIONS\scripts
DATA_DIR=C:\Users\eguid\Desktop\CLAUDE RECOMENDATIONS\data

# ============================================================
# YOUR SPECIFIC LOCATIONS TO SCAN
# ============================================================
# WSL
WSL_PATH=\\wsl.localhost
WSL_DISTROS=Ubuntu,Ubuntu-22.04,Debian

# OneDrive Locations
ONEDRIVE_ROOT=C:\Users\eguid\OneDrive
ONEDRIVE_PERSONAL_VAULT=C:\Users\eguid\OneDrive\Personal Vault
ONEDRIVE_APPDATA=C:\Users\eguid\OneDrive\AppData
ONEDRIVE_DESKTOP=C:\Users\eguid\OneDrive\Desktop
ONEDRIVE_DRIVERS=C:\Users\eguid\OneDrive\drivers and apps
ONEDRIVE_PICTURES=C:\Users\eguid\OneDrive\Pictures

# Restored Data
RESTORED_DRIVE=G:\restored
RESTORED_DRIVE_ROOT=G:\

# ============================================================
# LM ARENA CHAT URLS (Your specific chats)
# ============================================================
LMARENA_CHAT_URLS=https://lmarena.ai/c/019b364c-8fbd-722b-949d-9bb5c17a516f,https://lmarena.ai/c/019b352d-09a8-78de-9002-5d11440aac80,https://lmarena.ai/c/019b352a-e9b8-7a99-8d3b-f7cfe5a7946e,https://lmarena.ai/c/019b3529-b512-701d-a054-bd7d1e4e6917,https://lmarena.ai/c/019b1ef3-a33d-7722-a2ea-c406c8d0a4d5,https://lmarena.ai/c/019b0a05-e1e5-7764-a9ff-94e74c1826a3,https://lmarena.ai/c/019b15a6-06aa-7090-b65f-f98510c2ad01,https://lmarena.ai/c/019b0e15-dc4e-714d-ac7b-04f592f66f8c,https://lmarena.ai/c/019b0e13-edfa-7e43-b8dd-8aa28d0b3eb3,https://lmarena.ai/c/019b0e3a-1787-7506-81cd-99d376b57b62,https://lmarena.ai/c/019b0c74-9fbf-7c68-9521-aa4c67eb165b

# ============================================================
# USER INFO
# ============================================================
WINDOWS_USERNAME=eguid
LINUX_USERNAME=eguid

# ============================================================
# DATABASE
# ============================================================
DATABASE_URL=postgresql://mama_ai:mama_ai_pass@localhost:5432/mama_ai
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_NAME=mama_ai
DATABASE_USER=mama_ai
DATABASE_PASSWORD=mama_ai_pass

# ============================================================
# VECTOR STORE (Qdrant)
# ============================================================
QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION=mamaai_recovery

# ============================================================
# ARGILLA (Data Labeling)
# ============================================================
ARGILLA_API_URL=http://localhost:6900
ARGILLA_API_KEY=admin.apikey
ARGILLA_WORKSPACE=mamaai_recovery

# ============================================================
# REDIS
# ============================================================
REDIS_URL=redis://localhost:6379

# ============================================================
# BLENDER
# ============================================================
BLENDER_VERSION=5.0
BLENDER_PATH=C:\Program Files\Blender Foundation\Blender 4.2\blender.exe

# ============================================================
# API KEYS (Fill these in!)
# ============================================================
GITHUB_TOKEN=ghp_YOUR_TOKEN_HERE
GITHUB_USERNAME=YOUR_GITHUB_USERNAME

DEEPSEEK_API_KEY=sk-YOUR_DEEPSEEK_KEY
OPENAI_API_KEY=sk-YOUR_OPENAI_KEY
SERPER_API_KEY=YOUR_SERPER_KEY

# ============================================================
# MCP SERVER PORTS
# ============================================================
MCP_BLENDER_PORT=8003
MCP_SOFTWARE_PORT=8080
MCP_CONTENT_PORT=8021
MCP_RESEARCH_PORT=8022
MCP_MARKETING_PORT=8023
MCP_VFX_PORT=8026
MCP_CREATIVE_PORT=8027
MCP_RECOVERY_PORT=8028

# ============================================================
# PROCESSING
# ============================================================
EMBEDDING_MODEL=all-MiniLM-L6-v2
CHUNK_SIZE=1000
CHUNK_OVERLAP=200

# ============================================================
# LOGGING
# ============================================================
LOG_LEVEL=INFO
LOG_FILE=logs/mamaai.log

3. Sources Configuration

YAML

# config/sources.yaml
# ============================================================
# MAMAAI RECOVERY - YOUR SPECIFIC SOURCES
# ============================================================

project_info:
  name: "MamaAI Agency Recovery"
  description: "Recovering MamaAI project data from multiple locations"
  owner: "eguid"

# Keywords to identify your project files
project_keywords:
  - "mamaai"
  - "mama_ai"
  - "MamaAI"
  - "blender_agent"
  - "vfx_agent"
  - "creative_agent"
  - "BaseAgent"
  - "execute_task"
  - "mcp_server"
  - "eguid"
  - "blender_knowledge"
  - "compatibility_notes"
  - "tutorial_knowledge"
  - "addon_patterns"

file_signatures:
  - pattern: "from core.base_agent import BaseAgent"
    type: agent_code
    weight: 3.0
  - pattern: "class.*Agent.*BaseAgent"
    type: agent_code
    weight: 2.5
  - pattern: "async def execute_task"
    type: agent_code
    weight: 2.0
  - pattern: "MamaAI Agency"
    type: documentation
    weight: 2.0
  - pattern: "bpy.ops"
    type: blender_script
    weight: 1.5
  - pattern: "def get_tools"
    type: mcp_tool
    weight: 2.0

# ============================================================
# SOURCES
# ============================================================

sources:
  # ------------------------------------------
  # 1. LM ARENA CHAT LOGS
  # ------------------------------------------
  lmarena:
    enabled: true
    priority: 1
    
    chat_urls:
      - "https://lmarena.ai/c/019b364c-8fbd-722b-949d-9bb5c17a516f"
      - "https://lmarena.ai/c/019b352d-09a8-78de-9002-5d11440aac80"
      - "https://lmarena.ai/c/019b352a-e9b8-7a99-8d3b-f7cfe5a7946e"
      - "https://lmarena.ai/c/019b3529-b512-701d-a054-bd7d1e4e6917"
      - "https://lmarena.ai/c/019b1ef3-a33d-7722-a2ea-c406c8d0a4d5"
      - "https://lmarena.ai/c/019b0a05-e1e5-7764-a9ff-94e74c1826a3"
      - "https://lmarena.ai/c/019b15a6-06aa-7090-b65f-f98510c2ad01"
      - "https://lmarena.ai/c/019b0e15-dc4e-714d-ac7b-04f592f66f8c"
      - "https://lmarena.ai/c/019b0e13-edfa-7e43-b8dd-8aa28d0b3eb3"
      - "https://lmarena.ai/c/019b0e3a-1787-7506-81cd-99d376b57b62"
      - "https://lmarena.ai/c/019b0c74-9fbf-7c68-9521-aa4c67eb165b"
    
    browser_paths:
      - "C:/Users/eguid/AppData/Local/Google/Chrome/User Data/Default"
      - "C:/Users/eguid/AppData/Local/Microsoft/Edge/User Data/Default"
    
    export_scan_paths:
      - "C:/Users/eguid/Downloads"
      - "C:/Users/eguid/Documents"
      - "C:/Users/eguid/OneDrive/Desktop"

  # ------------------------------------------
  # 2. WSL FILESYSTEM
  # ------------------------------------------
  wsl:
    enabled: true
    priority: 2
    
    distros:
      - "Ubuntu"
      - "Ubuntu-22.04"
      - "Ubuntu-20.04"
      - "Debian"
    
    base_paths:
      - "\\\\wsl.localhost\\{distro}\\home"
      - "\\\\wsl.localhost\\{distro}\\home\\eguid"
      - "\\\\wsl$\\{distro}\\home"
      - "\\\\wsl$\\{distro}\\home\\eguid"
    
    scan_paths:
      - "projects"
      - "code"
      - "dev"
      - "workspace"
      - "Documents"
      - ".config"
      - ".local/share"
    
    include_patterns:
      - "*.py"
      - "*.sql"
      - "*.json"
      - "*.yaml"
      - "*.yml"
      - "*.md"
      - "*.sh"
      - "*.toml"
      - "Dockerfile"
      - "docker-compose*.yml"
      - "requirements.txt"
      - ".bashrc"
      - ".zshrc"
      - ".gitconfig"

  # ------------------------------------------
  # 3. RESTORED DRIVE (G:)
  # ------------------------------------------
  restored:
    enabled: true
    priority: 1
    
    paths:
      - "G:/restored"
      - "G:/"
    
    deep_scan: true
    
    include_patterns:
      - "*.py"
      - "*.sql"
      - "*.json"
      - "*.yaml"
      - "*.yml"
      - "*.md"
      - "*.txt"
      - "*.sh"
      - "*.r"
      - "*.R"
      - "*.Rmd"
      - "*.toml"
      - "*.xml"
      - "*.html"
      - "*.css"
      - "*.js"
      - "*.ts"
      - "*.ipynb"
      - "Dockerfile"
      - "docker-compose*.yml"
      - "requirements.txt"
      - "package.json"
    
    exclude_patterns:
      - "$RECYCLE.BIN/*"
      - "System Volume Information/*"
      - "node_modules/*"
      - "__pycache__/*"

  # ------------------------------------------
  # 4. ONEDRIVE LOCATIONS
  # ------------------------------------------
  onedrive:
    enabled: true
    priority: 2
    
    paths:
      - "C:/Users/eguid/OneDrive/Personal Vault"
      - "C:/Users/eguid/OneDrive/AppData"
      - "C:/Users/eguid/OneDrive/Desktop"
      - "C:/Users/eguid/OneDrive/drivers and apps"
      - "C:/Users/eguid/OneDrive/Pictures"
      - "C:/Users/eguid/OneDrive/Documents"
      - "C:/Users/eguid/OneDrive"
    
    include_patterns:
      - "*.py"
      - "*.sql"
      - "*.json"
      - "*.yaml"
      - "*.yml"
      - "*.md"
      - "*.txt"
      - "*.docx"
      - "*.xlsx"
      - "*.pdf"
      - "*.zip"
      - "*.7z"
      - "*.png"
      - "*.jpg"
    
    extract_archives: true
    scan_images_for_code: false

  # ------------------------------------------
  # 5. LOCAL USER FOLDERS
  # ------------------------------------------
  local:
    enabled: true
    priority: 3
    
    paths:
      - "C:/Users/eguid/Documents"
      - "C:/Users/eguid/Desktop"
      - "C:/Users/eguid/Downloads"
      - "C:/Users/eguid/Projects"
      - "C:/Users/eguid/Code"
      - "C:/Users/eguid/dev"
      - "C:/Users/eguid/AppData/Roaming/Code/User"

  # ------------------------------------------
  # 6. GITHUB (Optional)
  # ------------------------------------------
  github:
    enabled: false  # Set to true when you have the token
    
    # Add your repos here
    repositories: []
    
    include_gists: true
    include_forks: true

# ============================================================
# CONTENT CLASSIFICATION
# ============================================================

content_types:
  agent_code:
    patterns:
      - "class.*Agent"
      - "BaseAgent"
      - "execute_task"
      - "get_tools"
    category: "agencies"
    priority: "high"
  
  database_schema:
    patterns:
      - "CREATE TABLE"
      - "ALTER TABLE"
      - "INSERT INTO"
    category: "databases"
    priority: "high"
  
  workflow:
    patterns:
      - '"workflow_id"'
      - '"steps":'
      - '"agents":'
    category: "workflows"
    priority: "high"
  
  mcp_server:
    patterns:
      - "MCP"
      - "mcp_server"
      - "@mcp.tool"
    category: "mcp"
    priority: "high"
  
  blender_script:
    patterns:
      - "import bpy"
      - "bpy.ops"
      - "bpy.data"
    category: "scripts"
    priority: "medium"
  
  prompt_template:
    patterns:
      - "SYSTEM_PROMPT"
      - "USER_PROMPT"
      - "AGENT_PROMPT"
    category: "prompts"
    priority: "medium"

4. Main Entry Point

Python

# main.py
"""
MamaAI Agency - Project Recovery System

Main entry point for the recovery system and agency operations.

Usage:
    python main.py recovery full          # Run full recovery pipeline
    python main.py recovery source <name> # Run specific source
    python main.py search                 # Interactive search
    python main.py export                 # Export curated data
    python main.py api                    # Start API server
    python main.py dashboard              # Start dashboard
    python main.py agents list            # List available agents
    python main.py mcp start <server>     # Start MCP server
"""

import asyncio
import argparse
import sys
import os
from pathlib import Path
from datetime import datetime

# Add project root to path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
from dotenv import load_dotenv

# Load environment
load_dotenv()

console = Console()


def print_banner():
    """Print the MamaAI banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║   ███╗   ███╗ █████╗ ███╗   ███╗ █████╗  █████╗ ██╗          ║
    ║   ████╗ ████║██╔══██╗████╗ ████║██╔══██╗██╔══██╗██║          ║
    ║   ██╔████╔██║███████║██╔████╔██║███████║███████║██║          ║
    ║   ██║╚██╔╝██║██╔══██║██║╚██╔╝██║██╔══██║██╔══██║██║          ║
    ║   ██║ ╚═╝ ██║██║  ██║██║ ╚═╝ ██║██║  ██║██║  ██║██║          ║
    ║   ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝          ║
    ║                                                              ║
    ║              Agency Recovery & Management System             ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    console.print(banner, style="bold blue")


async def run_recovery(args):
    """Run recovery operations"""
    from recovery.pipeline import RecoveryPipeline
    
    pipeline = RecoveryPipeline()
    
    if args.subcommand == "full":
        console.print(Panel.fit(
            "[bold blue]🔍 Running Full Recovery Pipeline[/bold blue]\n"
            "Scanning all configured sources...",
            border_style="blue"
        ))
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("[cyan]Running recovery...", total=None)
            result = await pipeline.run_full_pipeline()
        
        # Display results
        _display_recovery_results(result)
        
    elif args.subcommand == "source":
        source_name = args.source_name
        console.print(f"[bold blue]Running source: {source_name}[/bold blue]")
        
        result = await pipeline.run_single_source(source_name)
        _display_source_result(source_name, result)
    
    elif args.subcommand == "list":
        sources = pipeline.get_available_sources()
        
        table = Table(title="Available Sources")
        table.add_column("Source", style="cyan")
        table.add_column("Status", style="green")
        table.add_column("Priority")
        
        for name, info in sources.items():
            status = "✓ Enabled" if info.get("enabled") else "✗ Disabled"
            table.add_row(name, status, str(info.get("priority", "-")))
        
        console.print(table)


def _display_recovery_results(result):
    """Display recovery results"""
    table = Table(title="Recovery Results")
    table.add_column("Source", style="cyan")
    table.add_column("Items Found", style="green")
    table.add_column("Processed", style="yellow")
    table.add_column("Errors", style="red")
    
    for source, data in result.get("sources", {}).items():
        table.add_row(
            source,
            str(data.get("items_found", 0)),
            str(data.get("items_processed", 0)),
            str(len(data.get("errors", [])))
        )
    
    console.print(table)
    
    console.print(f"\n[bold green]Total Items:[/bold green] {result.get('total_items', 0)}")
    console.print(f"[bold green]Total Processed:[/bold green] {result.get('total_processed', 0)}")
    console.print(f"[bold green]Total Stored:[/bold green] {result.get('total_stored', 0)}")


def _display_source_result(source_name, result):
    """Display single source result"""
    if result.get("error"):
        console.print(f"[red]Error: {result['error']}[/red]")
        return
    
    console.print(f"\n[green]Results for {source_name}:[/green]")
    console.print(f"  Items found: {result.get('items_found', 0)}")
    console.print(f"  Items processed: {result.get('items_processed', 0)}")
    console.print(f"  Items stored: {result.get('items_stored', 0)}")
    
    if result.get('errors'):
        console.print(f"[yellow]  Errors: {len(result['errors'])}[/yellow]")


async def run_search(args):
    """Run interactive search"""
    from recovery.pipeline import RecoveryPipeline
    
    console.print(Panel.fit(
        "[bold blue]🔎 MamaAI Interactive Search[/bold blue]",
        border_style="blue"
    ))
    
    pipeline = RecoveryPipeline()
    
    while True:
        query = console.input("\n[cyan]Search query[/cyan] (or 'quit'): ")
        
        if query.lower() in ['quit', 'exit', 'q']:
            break
        
        # Parse filters
        filters = {}
        if "type:" in query:
            parts = query.split("type:")
            query = parts[0].strip()
            type_filter = parts[1].split()[0]
            filters["content_type"] = type_filter
        
        results = pipeline.search(query, limit=10, filters=filters if filters else None)
        
        if not results:
            console.print("[yellow]No results found[/yellow]")
            continue
        
        console.print(f"\n[green]Found {len(results)} results:[/green]\n")
        
        for i, result in enumerate(results, 1):
            console.print(Panel(
                f"[bold]{result.get('filename', 'Unknown')}[/bold]\n"
                f"Score: {result.get('score', 0):.3f} | "
                f"Type: {result.get('content_type', 'unknown')} | "
                f"Source: {result.get('source_type', 'unknown')}\n\n"
                f"{result.get('content', '')[:500]}...",
                title=f"Result {i}",
                border_style="blue"
            ))


async def run_export(args):
    """Export curated data"""
    from argilla_integration.export import ArgillaExporter
    
    console.print(Panel.fit(
        "[bold blue]📤 Export Curated Data[/bold blue]",
        border_style="blue"
    ))
    
    exporter = ArgillaExporter()
    
    # Get dataset name
    dataset_name = args.dataset if hasattr(args, 'dataset') else None
    if not dataset_name:
        dataset_name = console.input("Dataset name [recovery_latest]: ") or "recovery_latest"
    
    # Get export path
    default_path = f"./data/exports/{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    export_path = console.input(f"Export path [{default_path}]: ") or default_path
    
    try:
        count = await exporter.export_curated_data(
            dataset_name=dataset_name,
            output_path=export_path,
            format="structured"  # Organize by content type
        )
        console.print(f"\n[green]✓ Exported {count} items to {export_path}[/green]")
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")


def run_api(args):
    """Run API server"""
    import uvicorn
    
    port = args.port if hasattr(args, 'port') else 8000
    
    console.print(f"[bold blue]🌐 Starting API server on http://localhost:{port}[/bold blue]")
    console.print("[dim]API docs available at http://localhost:{port}/docs[/dim]")
    
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=port,
        reload=True
    )


def run_dashboard(args):
    """Run Streamlit dashboard"""
    import subprocess
    
    port = args.port if hasattr(args, 'port') else 8501
    
    console.print(f"[bold blue]📊 Starting Dashboard on http://localhost:{port}[/bold blue]")
    
    subprocess.run([
        "streamlit", "run", "ui/dashboard.py",
        "--server.port", str(port),
        "--server.headless", "true"
    ])


async def run_agents(args):
    """Agent management"""
    if args.subcommand == "list":
        from agencies import get_all_agents
        
        agents = get_all_agents()
        
        table = Table(title="Available Agents")
        table.add_column("Agent ID", style="cyan")
        table.add_column("Agency", style="green")
        table.add_column("Description")
        
        for agent_id, agent_info in agents.items():
            table.add_row(
                agent_id,
                agent_info.get("agency", "unknown"),
                agent_info.get("description", "")[:50] + "..."
            )
        
        console.print(table)
    
    elif args.subcommand == "info":
        agent_id = args.agent_id
        from agencies import get_agent_info
        
        info = get_agent_info(agent_id)
        if info:
            console.print(Panel(
                f"[bold]{info['agent_id']}[/bold]\n\n"
                f"Agency: {info['agency']}\n"
                f"Description: {info['description']}\n\n"
                f"Tools:\n" + "\n".join(f"  - {t['name']}" for t in info.get('tools', [])),
                title=f"Agent: {agent_id}"
            ))
        else:
            console.print(f"[red]Agent not found: {agent_id}[/red]")


def run_mcp(args):
    """MCP server management"""
    if args.subcommand == "start":
        server_name = args.server_name
        
        server_map = {
            "vfx": "mcp/servers/vfx_mcp_server.py",
            "creative": "mcp/servers/creative_mcp_server.py",
            "recovery": "mcp/servers/recovery_mcp_server.py",
        }
        
        if server_name not in server_map:
            console.print(f"[red]Unknown server: {server_name}[/red]")
            console.print(f"Available: {', '.join(server_map.keys())}")
            return
        
        console.print(f"[bold blue]Starting MCP Server: {server_name}[/bold blue]")
        
        import subprocess
        subprocess.run(["python", server_map[server_name]])
    
    elif args.subcommand == "list":
        table = Table(title="MCP Servers")
        table.add_column("Server", style="cyan")
        table.add_column("Port", style="green")
        table.add_column("Status")
        
        servers = [
            ("VFX", os.getenv("MCP_VFX_PORT", "8026")),
            ("Creative", os.getenv("MCP_CREATIVE_PORT", "8027")),
            ("Recovery", os.getenv("MCP_RECOVERY_PORT", "8028")),
            ("Blender", os.getenv("MCP_BLENDER_PORT", "8003")),
        ]
        
        for name, port in servers:
            # Check if running
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('localhost', int(port)))
            status = "🟢 Running" if result == 0 else "⚪ Stopped"
            sock.close()
            
            table.add_row(name, port, status)
        
        console.print(table)


def main():
    """Main entry point"""
    print_banner()
    
    parser = argparse.ArgumentParser(
        description="MamaAI Agency - Project Recovery System",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Recovery command
    recovery_parser = subparsers.add_parser("recovery", help="Recovery operations")
    recovery_sub = recovery_parser.add_subparsers(dest="subcommand")
    
    recovery_sub.add_parser("full", help="Run full recovery pipeline")
    recovery_sub.add_parser("list", help="List available sources")
    
    source_parser = recovery_sub.add_parser("source", help="Run specific source")
    source_parser.add_argument("source_name", help="Source name (lmarena, wsl, restored, onedrive, local)")
    
    # Search command
    subparsers.add_parser("search", help="Interactive search")
    
    # Export command
    export_parser = subparsers.add_parser("export", help="Export curated data")
    export_parser.add_argument("--dataset", help="Dataset name")
    
    # API command
    api_parser = subparsers.add_parser("api", help="Start API server")
    api_parser.add_argument("--port", type=int, default=8000)
    
    # Dashboard command
    dash_parser = subparsers.add_parser("dashboard", help="Start dashboard")
    dash_parser.add_argument("--port", type=int, default=8501)
    
    # Agents command
    agents_parser = subparsers.add_parser("agents", help="Agent management")
    agents_sub = agents_parser.add_subparsers(dest="subcommand")
    agents_sub.add_parser("list", help="List all agents")
    info_parser = agents_sub.add_parser("info", help="Get agent info")
    info_parser.add_argument("agent_id", help="Agent ID")
    
    # MCP command
    mcp_parser = subparsers.add_parser("mcp", help="MCP server management")
    mcp_sub = mcp_parser.add_subparsers(dest="subcommand")
    mcp_sub.add_parser("list", help="List MCP servers")
    start_parser = mcp_sub.add_parser("start", help="Start MCP server")
    start_parser.add_argument("server_name", help="Server name")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Run appropriate command
    if args.command == "recovery":
        asyncio.run(run_recovery(args))
    elif args.command == "search":
        asyncio.run(run_search(args))
    elif args.command == "export":
        asyncio.run(run_export(args))
    elif args.command == "api":
        run_api(args)
    elif args.command == "dashboard":
        run_dashboard(args)
    elif args.command == "agents":
        asyncio.run(run_agents(args))
    elif args.command == "mcp":
        run_mcp(args)


if __name__ == "__main__":
    main()

5. Recovery Pipeline

Python

# recovery/pipeline.py
"""
MamaAI Recovery Pipeline
Orchestrates the recovery of project data from multiple sources
"""

import asyncio
import os
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
import yaml

from loguru import logger
from dotenv import load_dotenv

load_dotenv()

# Import scrapers
from recovery.scrapers.lmarena_scraper import LMArenaScraper
from recovery.scrapers.wsl_scraper import WSLScraper
from recovery.scrapers.onedrive_scraper import OneDriveScraper
from recovery.scrapers.restored_drive_scraper import RestoredDriveScraper
from recovery.scrapers.base import ScrapedItem

# Import processors
from recovery.processors.code_processor import CodeProcessor
from recovery.processors.workflow_processor import WorkflowProcessor
from recovery.processors.schema_processor import SchemaProcessor

# Import storage
from recovery.storage.vector_store import VectorStore
from recovery.storage.database import DatabaseManager

# Import Argilla
from argilla_integration.datasets import ArgillaManager


class RecoveryPipeline:
    """
    Main pipeline for recovering MamaAI project data.
    
    Sources:
    - LM Arena chat logs
    - WSL filesystem
    - Restored drive (G:)
    - OneDrive locations
    - Local folders
    """
    
    def __init__(self):
        self.project_root = Path(os.getenv("PROJECT_ROOT", "."))
        self.config = self._load_config()
        
        # Initialize components
        self.vector_store = VectorStore(
            url=os.getenv("QDRANT_URL", "http://localhost:6333"),
            collection=os.getenv("QDRANT_COLLECTION", "mamaai_recovery")
        )
        
        self.database = DatabaseManager(
            url=os.getenv("DATABASE_URL")
        )
        
        self.argilla = ArgillaManager(
            api_url=os.getenv("ARGILLA_API_URL", "http://localhost:6900"),
            api_key=os.getenv("ARGILLA_API_KEY", "admin.apikey"),
            workspace=os.getenv("ARGILLA_WORKSPACE", "mamaai_recovery")
        )
        
        # Initialize processors
        self.code_processor = CodeProcessor(self.config)
        self.workflow_processor = WorkflowProcessor(self.config)
        self.schema_processor = SchemaProcessor(self.config)
        
        # Initialize scrapers
        self.scrapers = self._init_scrapers()
        
        # State
        self.status = "idle"
        self.current_run = None
        self.runs_history = []
        self.item_buffer = []
        self.buffer_size = 50
    
    def _load_config(self) -> Dict[str, Any]:
        """Load sources configuration"""
        config_path = self.project_root / "config" / "sources.yaml"
        
        if config_path.exists():
            with open(config_path) as f:
                return yaml.safe_load(f)
        
        return {"sources": {}, "project_keywords": []}
    
    def _init_scrapers(self) -> Dict[str, Any]:
        """Initialize all scrapers"""
        scrapers = {}
        sources_config = self.config.get("sources", {})
        
        # LM Arena
        if sources_config.get("lmarena", {}).get("enabled", True):
            scrapers["lmarena"] = LMArenaScraper(
                config=self.config,
                chat_urls=self._get_lmarena_urls()
            )
        
        # WSL
        if sources_config.get("wsl", {}).get("enabled", True):
            scrapers["wsl"] = WSLScraper(config=self.config)
        
        # Restored Drive
        if sources_config.get("restored", {}).get("enabled", True):
            scrapers["restored"] = RestoredDriveScraper(config=self.config)
        
        # OneDrive
        if sources_config.get("onedrive", {}).get("enabled", True):
            scrapers["onedrive"] = OneDriveScraper(config=self.config)
        
        return scrapers
    
    def _get_lmarena_urls(self) -> List[str]:
        """Get LM Arena URLs from config and environment"""
        urls = []
        
        # From environment
        env_urls = os.getenv("LMARENA_CHAT_URLS", "")
        if env_urls:
            urls.extend(env_urls.split(","))
        
        # From config
        config_urls = self.config.get("sources", {}).get("lmarena", {}).get("chat_urls", [])
        urls.extend(config_urls)
        
        # Remove duplicates
        return list(set(urls))
    
    def get_available_sources(self) -> Dict[str, Dict]:
        """Get available sources with their status"""
        sources = {}
        
        for name, scraper in self.scrapers.items():
            source_config = self.config.get("sources", {}).get(name, {})
            sources[name] = {
                "enabled": source_config.get("enabled", True),
                "priority": source_config.get("priority", 5),
                "scraper": type(scraper).__name__
            }
        
        return sources
    
    async def run_full_pipeline(self) -> Dict[str, Any]:
        """Run the complete recovery pipeline"""
        run_id = f"run_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"
        
        result = {
            "run_id": run_id,
            "started_at": datetime.utcnow().isoformat(),
            "status": "running",
            "sources": {},
            "total_items": 0,
            "total_processed": 0,
            "total_stored": 0,
            "errors": []
        }
        
        self.status = "running"
        self.current_run = result
        
        logger.info(f"Starting recovery pipeline: {run_id}")
        
        try:
            # Create Argilla dataset
            dataset = self.argilla.create_recovery_dataset(
                name=f"recovery_{run_id}"
            )
            
            # Sort scrapers by priority
            sorted_scrapers = sorted(
                self.scrapers.items(),
                key=lambda x: self.config.get("sources", {}).get(x[0], {}).get("priority", 5)
            )
            
            # Run each scraper
            for source_name, scraper in sorted_scrapers:
                source_result = {
                    "items_found": 0,
                    "items_processed": 0,
                    "errors": []
                }
                
                logger.info(f"Running scraper: {source_name}")
                
                try:
                    if await scraper.validate_connection():
                        async for item in scraper.scrape():
                            source_result["items_found"] += 1
                            result["total_items"] += 1
                            
                            # Classify and process item
                            processed_item = await self._process_item(item)
                            
                            if processed_item:
                                self.item_buffer.append(processed_item)
                                source_result["items_processed"] += 1
                                
                                if len(self.item_buffer) >= self.buffer_size:
                                    await self._flush_buffer(dataset, result)
                            
                            # Progress logging
                            if result["total_items"] % 50 == 0:
                                logger.info(f"Progress: {result['total_items']} items found")
                    else:
                        logger.warning(f"Could not validate connection for {source_name}")
                        source_result["errors"].append("Connection validation failed")
                        
                except Exception as e:
                    error_msg = f"Error in {source_name}: {str(e)}"
                    logger.error(error_msg)
                    source_result["errors"].append(error_msg)
                    result["errors"].append(error_msg)
                
                result["sources"][source_name] = source_result
            
            # Flush remaining buffer
            await self._flush_buffer(dataset, result)
            
            result["status"] = "completed"
            
        except Exception as e:
            result["status"] = "error"
            result["errors"].append(f"Pipeline error: {str(e)}")
            logger.error(f"Pipeline failed: {e}")
            
        finally:
            result["ended_at"] = datetime.utcnow().isoformat()
            self.status = "idle"
            self.runs_history.append(result)
            self.current_run = None
        
        logger.info(f"Pipeline complete: {result['total_items']} items, {result['total_processed']} processed")
        
        return result
    
    async def run_single_source(self, source_name: str) -> Dict[str, Any]:
        """Run a single source scraper"""
        if source_name not in self.scrapers:
            return {
                "error": f"Unknown source: {source_name}. Available: {list(self.scrapers.keys())}"
            }
        
        scraper = self.scrapers[source_name]
        
        result = {
            "source": source_name,
            "items_found": 0,
            "items_processed": 0,
            "items_stored": 0,
            "errors": []
        }
        
        logger.info(f"Running single source: {source_name}")
        
        try:
            if await scraper.validate_connection():
                async for item in scraper.scrape():
                    result["items_found"] += 1
                    
                    # Process item
                    processed = await self._process_item(item)
                    
                    if processed:
                        # Store directly
                        chunks = self.code_processor.chunk_and_embed(processed)
                        if chunks:
                            stored = self.vector_store.upsert_chunks(chunks)
                            result["items_stored"] += stored
                        
                        result["items_processed"] += 1
                    
                    if result["items_found"] % 25 == 0:
                        logger.info(f"Progress: {result['items_found']} items")
            else:
                result["errors"].append("Connection validation failed")
                
        except Exception as e:
            result["errors"].append(str(e))
            logger.error(f"Error in {source_name}: {e}")
        
        return result
    
    async def _process_item(self, item: ScrapedItem) -> Optional[ScrapedItem]:
        """Process and classify a scraped item"""
        try:
            # Classify content type
            content_type = self._classify_content(item.content, item.filename)
            item.metadata["classified_type"] = content_type
            
            # Apply appropriate processor
            if content_type == "agent_code":
                item = self.code_processor.process_agent_code(item)
            elif content_type == "database_schema":
                item = self.schema_processor.process_schema(item)
            elif content_type == "workflow":
                item = self.workflow_processor.process_workflow(item)
            elif content_type == "blender_script":
                item = self.code_processor.process_blender_script(item)
            
            return item
            
        except Exception as e:
            logger.warning(f"Error processing item {item.filename}: {e}")
            return item
    
    def _classify_content(self, content: str, filename: str) -> str:
        """Classify content type based on patterns"""
        content_types = self.config.get("content_types", {})
        
        for type_name, type_info in content_types.items():
            patterns = type_info.get("patterns", [])
            for pattern in patterns:
                if pattern in content:
                    return type_name
        
        # Fallback classification by extension
        ext = Path(filename).suffix.lower() if filename else ""
        
        ext_map = {
            ".py": "python_code",
            ".sql": "database_schema",
            ".json": "json_data",
            ".yaml": "yaml_data",
            ".yml": "yaml_data",
            ".md": "documentation",
        }
        
        return ext_map.get(ext, "unknown")
    
    async def _flush_buffer(self, dataset, result: Dict[str, Any]):
        """Flush buffer to storage"""
        if not self.item_buffer:
            return
        
        for item in self.item_buffer:
            try:
                # Generate embeddings and store
                chunks = self.code_processor.chunk_and_embed(item)
                if chunks:
                    stored = self.vector_store.upsert_chunks(chunks)
                    result["total_stored"] += stored
                
                result["total_processed"] += 1
                
            except Exception as e:
                logger.warning(f"Error storing item: {e}")
        
        # Add to Argilla for labeling
        try:
            self.argilla.add_items_to_dataset(dataset, self.item_buffer)
        except Exception as e:
            logger.warning(f"Error adding to Argilla: {e}")
        
        self.item_buffer.clear()
    
    def search(
        self, 
        query: str, 
        limit: int = 10, 
        filters: Optional[Dict] = None
    ) -> List[Dict[str, Any]]:
        """Search recovered data"""
        return self.vector_store.search_by_text(
            query=query,
            limit=limit,
            filters=filters
        )
    
    def get_stats(self) -> Dict[str, Any]:
        """Get pipeline statistics"""
        return {
            "status": self.status,
            "available_sources": list(self.scrapers.keys()),
            "vector_store": self.vector_store.get_statistics(),
            "total_runs": len(self.runs_history),
            "last_run": self.runs_history[-1] if self.runs_history else None
        }

6. Docker Compose

YAML

# docker-compose.yml
version: '3.8'

services:
  # PostgreSQL Database
  postgres:
    image: postgres:15
    container_name: mamaai_postgres
    environment:
      POSTGRES_USER: mama_ai
      POSTGRES_PASSWORD: mama_ai_pass
      POSTGRES_DB: mama_ai
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./databases/schemas:/docker-entrypoint-initdb.d
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U mama_ai"]
      interval: 10s
      timeout: 5s
      retries: 5

  # Qdrant Vector Database
  qdrant:
    image: qdrant/qdrant:latest
    container_name: mamaai_qdrant
    ports:
      - "6333:6333"
      - "6334:6334"
    volumes:
      - qdrant_data:/qdrant/storage
    environment:
      QDRANT__SERVICE__GRPC_PORT: 6334

  # Redis
  redis:
    image: redis:7-alpine
    container_name: mamaai_redis
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  # Elasticsearch (for Argilla)
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.5.0
    container_name: mamaai_elasticsearch
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    volumes:
      - es_data:/usr/share/elasticsearch/data
    ports:
      - "9200:9200"

  # Argilla (Data Labeling)
  argilla:
    image: argilla/argilla-server:latest
    container_name: mamaai_argilla
    ports:
      - "6900:6900"
    environment:
      ARGILLA_ELASTICSEARCH: http://elasticsearch:9200
      ARGILLA_AUTH_SECRET_KEY: mamaai-secret-key
      ARGILLA_API_KEY: admin.apikey
    depends_on:
      - elasticsearch
    volumes:
      - argilla_data:/var/lib/argilla

  # MamaAI Recovery System
  mamaai:
    build:
      context: .
      dockerfile: Dockerfile
    container_name: mamaai_app
    depends_on:
      - postgres
      - qdrant
      - redis
      - argilla
    volumes:
      - .:/app
      - /mnt/g:/mnt/g:ro  # Mount G: drive read-only
    environment:
      - DATABASE_URL=postgresql://mama_ai:mama_ai_pass@postgres:5432/mama_ai
      - QDRANT_URL=http://qdrant:6333
      - REDIS_URL=redis://redis:6379
      - ARGILLA_API_URL=http://argilla:6900
    ports:
      - "8000:8000"  # API
      - "8501:8501"  # Dashboard

volumes:
  postgres_data:
  qdrant_data:
  redis_data:
  es_data:
  argilla_data:

7. Requirements

txt

# requirements.txt

# Core
fastapi>=0.104.0
uvicorn>=0.24.0
pydantic>=2.0.0
pydantic-settings>=2.0.0

# Async
aiohttp>=3.9.0
aiofiles>=23.2.0
httpx>=0.25.0

# Database
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
asyncpg>=0.29.0

# Vector Store
qdrant-client>=1.6.0

# Embeddings
sentence-transformers>=2.2.0
torch>=2.0.0

# Data Labeling
argilla>=1.20.0

# Task Queue
celery>=5.3.0
redis>=5.0.0

# Configuration
python-dotenv>=1.0.0
pyyaml>=6.0.0

# CLI & UI
rich>=13.0.0
streamlit>=1.28.0
plotly>=5.18.0

# File Processing
chardet>=5.2.0
py7zr>=0.20.0

# GitHub
PyGithub>=2.1.0

# Logging
loguru>=0.7.0

# Utilities
pandas>=2.0.0

# MCP
mcp>=0.1.0

Quick Start Commands

PowerShell

# PowerShell - Setup

# 1. Navigate to your project
cd "C:\Users\eguid\Desktop\CLAUDE RECOMENDATIONS"

# 2. Create virtual environment
python -m venv venv
.\venv\Scripts\Activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Start Docker services
docker-compose up -d

# 5. Initialize database
python scripts/init_database.py

# 6. Run full recovery
python main.py recovery full

# Or run specific sources:
python main.py recovery source lmarena    # Your LM Arena chats
python main.py recovery source wsl        # WSL filesystem
python main.py recovery source restored   # G:\restored drive
python main.py recovery source onedrive   # OneDrive locations

# 7. Search recovered data
python main.py search

# 8. Start web interface
python main.py api          # API on http://localhost:8000
python main.py dashboard    # Dashboard on http://localhost:8501

# 9. Access Argilla for data labeling
# Open http://localhost:6900

This complete setup will:

    Scrape your LM Arena chats (all 11 URLs you provided)
    Scan WSL filesystem (\\wsl.localhost\*)
    Scan your restored drive (G:\restored)
    Scan OneDrive locations (Personal Vault, AppData, Desktop, drivers and apps, Pictures)
    Classify content (agent code, database schemas, workflows, etc.)
    Store in vector database for semantic search
    Send to Argilla for review and labeling
    Export organized data back to your project structure

Would you like me to add any additional components or modify the configuration?

workflows , pipelines, promp # Environment Configuration
Setup Instructions

    Copy the example environment file:

Bash

    copy .env.example .env

    Edit .env file with your actual values:
        Update PROJECT_ROOT to your actual project path
        Add your API keys (DeepSeek, OpenAI, Serper)
        Configure database connection if different
        Adjust Blender path if needed

    Install python-dotenv: 📁 FILE STRUCTURE OVERVIEW

text

C:\Users\eguid\Desktop\CLAUDE RECOMENDATIONS
├── databases/
│ └── schemas/
│ ├── blender_knowledge_schema.sql # NEW
│ ├── compatibility_schema.sql # NEW
│ └── tutorial_extraction_schema.sql # NEW
├── agencies/
│ ├── blender/
│ │ └── vfx/
│ │ └── agents/
│ │ ├── init.py # UPDATED
│ │ ├── vfx_layout_artist.py # NEW
│ │ ├── camera_tracking_agent.py # NEW
│ │ ├── projection_mapping_agent.py # NEW
│ │ └── integration_agent.py # NEW
│ └── creative/
│ └── agents/
│ ├── init.py # UPDATED
│ ├── creative_director.py # NEW
│ ├── social_media_strategist.py # NEW
│ ├── scriptwriter.py # NEW
│ ├── director_consultant.py # NEW
│ └── ad_techniques_researcher.py # NEW
├── mcp/
│ └── servers/
│ ├── vfx_mcp_server.py # NEW (Port 8026)
│ └── creative_mcp_server.py # NEW (Port 8027)
├── workflows/
│ ├── blender_compatibility_workflow.json # NEW
│ ├── addon_reverse_engineering.json # NEW
│ ├── youtube_knowledge_extraction.json # NEW
│ └── commercial_revenue_gen.json # NEW
├── mcp/
│ └── prompts/
│ ├── blender_prompts.py # UPDATED
│ ├── vfx_prompts.py # NEW
│ ├── creative_prompts.py # NEW
│ └── software_prompts.py # UPDATED
└── scripts/
├── scrape_blender_official_docs.py # NEW
├── extract_tutorials_to_workflows.py # NEW
├── load_compatibility_data.py # NEW
└── addon_pattern_extractor.py # NEW

📊 PART 1: DATABASE SCHEMAS
1.1 Blender Knowledge Schema

File: databases/schemas/blender_knowledge_schema.sql

SQL

-- ============================================================
-- BLENDER KNOWLEDGE DATABASE SCHEMA
-- MamaAI Agency - Blender Documentation & Learning System
-- Generated: 2025-12-19
-- Target: PostgreSQL 14+
-- ============================================================

-- Drop existing tables if recreating
-- DROP TABLE IF EXISTS compatibility_notes CASCADE;
-- DROP TABLE IF EXISTS api_details CASCADE;
-- DROP TABLE IF EXISTS tutorial_knowledge CASCADE;
-- DROP TABLE IF EXISTS addon_patterns CASCADE;
-- DROP TABLE IF EXISTS blender_keywords CASCADE;
-- DROP TABLE IF EXISTS blender_tools CASCADE;

-- ============================================================
-- 1. COMPATIBILITY NOTES TABLE
-- Tracks breaking changes across Blender versions
-- ============================================================
CREATE TABLE IF NOT EXISTS compatibility_notes (
id BIGSERIAL PRIMARY KEY,
note_id TEXT UNIQUE NOT NULL,

text

-- Version Information
affected_version TEXT NOT NULL,           -- e.g., '5.0', '4.3'
affected_version_end TEXT,                -- For version ranges
min_supported_version TEXT,               -- Minimum version this applies to

-- Change Classification
affected_area TEXT NOT NULL,              -- 'Grease Pencil', 'Geometry Nodes', 'Python API'
affected_module TEXT,                     -- 'bpy.ops.mesh', 'bpy.types.GreasePencil'
change_type TEXT NOT NULL CHECK (change_type IN (
    'breaking_change',
    'deprecation', 
    'removal',
    'api_change',
    'behavior_change',
    'new_feature',
    'enhancement',
    'bug_fix'
)),
severity TEXT CHECK (severity IN ('critical', 'high', 'medium', 'low', 'info')),

-- Content
title TEXT NOT NULL,
description TEXT NOT NULL,

-- Migration Information
old_method TEXT,                          -- Previous way of doing things
old_code_pattern TEXT,                    -- Old code example
new_method TEXT,                          -- New recommended method
new_code_pattern TEXT,                    -- New code example
migration_steps JSONB,                    -- Array of migration steps
migration_script TEXT,                    -- Auto-migration script if available

-- Affected Components
affected_operators TEXT[],                -- Array of operator IDs
affected_properties TEXT[],               -- Array of property paths
affected_node_types TEXT[],               -- Array of node types

-- Source & Metadata
source_url TEXT,
documentation_url TEXT,
tags TEXT[],

-- Agent Guidance
agent_instructions TEXT,                  -- How agents should handle this
check_script TEXT,                        -- Python script to check if affected

-- Timestamps
created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()

);

-- ============================================================
-- 2. API DETAILS TABLE
-- Blender Python API documentation with version tracking
-- ============================================================
CREATE TABLE IF NOT EXISTS api_details (
id BIGSERIAL PRIMARY KEY,
api_id TEXT UNIQUE NOT NULL,

text

-- API Path
module_path TEXT NOT NULL,               -- e.g., 'bpy.ops.mesh'
function_name TEXT NOT NULL,             -- e.g., 'primitive_cube_add'
full_path TEXT GENERATED ALWAYS AS (module_path || '.' || function_name) STORED,

-- API Type
api_type TEXT NOT NULL CHECK (api_type IN (
    'function',
    'class',
    'property',
    'operator',
    'method',
    'constant',
    'enum',
    'module',
    'node_type'
)),

-- Version Tracking
introduced_version TEXT,
deprecated_version TEXT,
removed_version TEXT,
is_stable BOOLEAN DEFAULT TRUE,

-- Signature & Types
signature TEXT,                          -- Full function signature
return_type TEXT,
parameters JSONB,                        -- Array of {name, type, default, description}

-- Documentation
description TEXT,
long_description TEXT,
example_code TEXT,
notes TEXT,
warnings TEXT[],

-- Relationships
parent_class TEXT,                       -- For methods: the parent class
related_apis TEXT[],                     -- Array of related API paths
see_also TEXT[],                         -- Cross-references

-- Context & Requirements
mode_context TEXT[],                     -- ['OBJECT', 'EDIT_MESH', 'SCULPT']
poll_requirements TEXT,                  -- When this can be called

-- Source
documentation_url TEXT,
source_file TEXT,                        -- Blender source file

-- Search & Categorization
category TEXT,                           -- 'Mesh', 'Material', 'Animation'
subcategory TEXT,
tags TEXT[],
keywords TEXT[],                         -- For search

-- Timestamps
created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()

);

-- ============================================================
-- 3. TUTORIAL KNOWLEDGE TABLE
-- Parsed workflows from YouTube tutorials and documentation
-- ============================================================
CREATE TABLE IF NOT EXISTS tutorial_knowledge (
id BIGSERIAL PRIMARY KEY,
tutorial_id TEXT UNIQUE NOT NULL,

text

-- Source Information
source_type TEXT NOT NULL CHECK (source_type IN (
    'youtube',
    'blender_manual',
    'blender_api_docs',
    'github_addon',
    'sketchfab',
    'external_tutorial'
)),
source_id TEXT,                          -- Video ID, doc path, etc.
source_url TEXT,

-- Content
title TEXT NOT NULL,
description TEXT,
channel_name TEXT,                       -- For YouTube
channel_id TEXT,

-- Classification
agency_owner TEXT DEFAULT 'blender',     -- Which agency owns this knowledge
category TEXT NOT NULL,                  -- 'modeling', 'vfx', 'lighting', 'rigging'
subcategory TEXT,
difficulty_level INTEGER DEFAULT 2 CHECK (difficulty_level BETWEEN 1 AND 5),
estimated_duration_minutes INTEGER,

-- Extracted Workflow
steps JSONB NOT NULL DEFAULT '[]',       -- Array of step objects
-- Step format: {
--   "step_num": 1,
--   "title": "Step title",
--   "instruction": "Detailed instruction",
--   "keyboard_shortcut": "Shift+A",
--   "operator_path": "bpy.ops.mesh.primitive_cube_add",
--   "tool_prediction": "modeling_agent.create_primitive",
--   "expected_result": "Cube appears in scene",
--   "timestamp_start": 120,
--   "timestamp_end": 180
-- }

-- Extracted Tools & Techniques
extracted_tools TEXT[],                  -- Array of tool IDs used
extracted_operators TEXT[],              -- Array of bpy.ops paths
techniques_used TEXT[],                  -- Array of technique names

-- Requirements
blender_version_min TEXT,
blender_version_max TEXT,
required_addons TEXT[],
prerequisites TEXT[],                    -- Array of tutorial_ids

-- Raw Content
raw_transcript TEXT,
raw_description TEXT,

-- Metrics
view_count INTEGER,
like_count INTEGER,
quality_score REAL,                      -- Calculated quality (0-10)

-- Processing Status
is_processed BOOLEAN DEFAULT FALSE,
processing_status TEXT,
last_processed_at TIMESTAMPTZ,

-- Timestamps
upload_date DATE,
created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()

);

-- ============================================================
-- 4. ADDON PATTERNS TABLE
-- Reverse-engineered code patterns from Blender addons
-- ============================================================
CREATE TABLE IF NOT EXISTS addon_patterns (
id BIGSERIAL PRIMARY KEY,
pattern_id TEXT UNIQUE NOT NULL,

text

-- Addon Information
addon_name TEXT NOT NULL,
addon_module TEXT,                       -- Python module name
addon_version TEXT,
addon_author TEXT,
addon_source TEXT,                       -- 'github', 'blender_extensions', 'local'
addon_source_url TEXT,

-- Extracted Pattern
pattern_type TEXT NOT NULL CHECK (pattern_type IN (
    'operator',
    'panel',
    'menu',
    'property_group',
    'node',
    'modifier',
    'handler',
    'utility_function',
    'material_generator',
    'mesh_generator',
    'animation_tool'
)),

-- Original Code
class_name TEXT,
bl_idname TEXT,                          -- Blender identifier
bl_label TEXT,
original_code TEXT NOT NULL,

-- Extracted Logic
extracted_logic TEXT,                    -- Simplified/cleaned version
core_operations TEXT[],                  -- Key operations performed

-- API Dependencies
api_dependencies TEXT[],                 -- Required bpy modules
external_dependencies TEXT[],            -- External Python packages

-- Compatibility
blender_version_min TEXT,
blender_version_max TEXT,
blender_version_compatible TEXT[],

-- Tool Conversion
converted_to_tool BOOLEAN DEFAULT FALSE,
tool_definition JSONB,                   -- MCP tool definition
agent_method_code TEXT,                  -- Generated agent method

-- Quality & Usefulness
complexity_score INTEGER,                -- 1-10
reusability_score INTEGER,               -- 1-10
is_verified BOOLEAN DEFAULT FALSE,

-- Timestamps
created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()

);

-- ============================================================
-- 5. BLENDER KEYWORDS TABLE
-- Keywords for search and categorization
-- ============================================================
CREATE TABLE IF NOT EXISTS blender_keywords (
id BIGSERIAL PRIMARY KEY,
keyword TEXT NOT NULL UNIQUE,

text

-- Classification
category TEXT,                           -- 'modeling', 'materials', 'animation'
domain TEXT DEFAULT 'blender',
weight REAL DEFAULT 1.0,

-- Relationships
synonyms TEXT[],
parent_keyword TEXT,
related_keywords TEXT[],

-- Usage
is_stop_word BOOLEAN DEFAULT FALSE,
occurrence_count INTEGER DEFAULT 0,

-- Mappings
maps_to_tool TEXT,                       -- Tool ID this keyword maps to
maps_to_operator TEXT,                   -- bpy.ops path
maps_to_area TEXT,                       -- Blender area

created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()

);

-- ============================================================
-- 6. BLENDER TOOLS TABLE
-- Tool registry for MCP exposure
-- ============================================================
CREATE TABLE IF NOT EXISTS blender_tools (
id BIGSERIAL PRIMARY KEY,
tool_id TEXT UNIQUE NOT NULL,

text

-- Tool Information
name TEXT NOT NULL,
description TEXT,
category TEXT NOT NULL,
subcategory TEXT,

-- MCP Definition
mcp_server TEXT DEFAULT 'blender',       -- Which MCP server exposes this
mcp_tool_name TEXT,                      -- Name in MCP
tool_definition JSONB NOT NULL,          -- Full MCP tool definition

-- Implementation
agent_id TEXT,                           -- Which agent implements this
method_name TEXT,                        -- Method name on agent
operator_path TEXT,                      -- Underlying bpy.ops path
implementation_code TEXT,                -- Actual Python code

-- Parameters
parameters JSONB,                        -- Parameter definitions
required_parameters TEXT[],
optional_parameters TEXT[],

-- Context
mode_context TEXT[],                     -- Required modes
object_type_context TEXT[],              -- Required object types
prerequisites TEXT[],                    -- Required setup

-- Version Compatibility
blender_version_min TEXT,
blender_version_max TEXT,

-- Keyboard Shortcuts
default_shortcut TEXT,
menu_path TEXT,

-- Source
source_addon TEXT,
source_pattern_id TEXT,                  -- References addon_patterns.pattern_id
documentation_url TEXT,

-- Status
is_active BOOLEAN DEFAULT TRUE,
is_verified BOOLEAN DEFAULT FALSE,

created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()

);

-- ============================================================
-- 7. WORKFLOW DEFINITIONS TABLE
-- Store workflow JSONs with metadata
-- ============================================================
CREATE TABLE IF NOT EXISTS workflow_definitions (
id BIGSERIAL PRIMARY KEY,
workflow_id TEXT UNIQUE NOT NULL,

text

-- Workflow Info
name TEXT NOT NULL,
description TEXT,
category TEXT NOT NULL,
subcategory TEXT,

-- Agencies & Agents
agencies TEXT[] NOT NULL,
primary_agency TEXT,
agents_used TEXT[],

-- Workflow Definition
definition JSONB NOT NULL,               -- Full workflow JSON
steps_count INTEGER,

-- Requirements
difficulty TEXT CHECK (difficulty IN ('beginner', 'intermediate', 'advanced', 'expert')),
estimated_duration_minutes INTEGER,
blender_version_min TEXT,
blender_version_max TEXT,
required_addons TEXT[],
prerequisites TEXT[],                    -- Array of workflow_ids

-- Classification
tags TEXT[],
keywords TEXT[],

-- Source
source TEXT,                             -- 'manual', 'tutorial', 'generated'
source_url TEXT,
source_tutorial_id TEXT,                 -- References tutorial_knowledge.tutorial_id

-- Status
is_active BOOLEAN DEFAULT TRUE,
is_verified BOOLEAN DEFAULT FALSE,
execution_count INTEGER DEFAULT 0,
success_rate REAL,

-- Timestamps
created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()

);

-- ============================================================
-- INDEXES FOR PERFORMANCE
-- ============================================================

-- Compatibility Notes
CREATE INDEX IF NOT EXISTS idx_compat_version ON compatibility_notes(affected_version);
CREATE INDEX IF NOT EXISTS idx_compat_area ON compatibility_notes(affected_area);
CREATE INDEX IF NOT EXISTS idx_compat_type ON compatibility_notes(change_type);
CREATE INDEX IF NOT EXISTS idx_compat_severity ON compatibility_notes(severity);
CREATE INDEX IF NOT EXISTS idx_compat_module ON compatibility_notes(affected_module);

-- API Details
CREATE INDEX IF NOT EXISTS idx_api_module ON api_details(module_path);
CREATE INDEX IF NOT EXISTS idx_api_function ON api_details(function_name);
CREATE INDEX IF NOT EXISTS idx_api_full_path ON api_details(full_path);
CREATE INDEX IF NOT EXISTS idx_api_type ON api_details(api_type);
CREATE INDEX IF NOT EXISTS idx_api_version ON api_details(introduced_version);
CREATE INDEX IF NOT EXISTS idx_api_category ON api_details(category);

-- Tutorial Knowledge
CREATE INDEX IF NOT EXISTS idx_tutorial_source ON tutorial_knowledge(source_type);
CREATE INDEX IF NOT EXISTS idx_tutorial_category ON tutorial_knowledge(category);
CREATE INDEX IF NOT EXISTS idx_tutorial_agency ON tutorial_knowledge(agency_owner);
CREATE INDEX IF NOT EXISTS idx_tutorial_difficulty ON tutorial_knowledge(difficulty_level);
CREATE INDEX IF NOT EXISTS idx_tutorial_processed ON tutorial_knowledge(is_processed);

-- Addon Patterns
CREATE INDEX IF NOT EXISTS idx_addon_name ON addon_patterns(addon_name);
CREATE INDEX IF NOT EXISTS idx_addon_type ON addon_patterns(pattern_type);
CREATE INDEX IF NOT EXISTS idx_addon_converted ON addon_patterns(converted_to_tool);

-- Keywords
CREATE INDEX IF NOT EXISTS idx_keyword_text ON blender_keywords(keyword);
CREATE INDEX IF NOT EXISTS idx_keyword_category ON blender_keywords(category);
CREATE INDEX IF NOT EXISTS idx_keyword_domain ON blender_keywords(domain);

-- Tools
CREATE INDEX IF NOT EXISTS idx_tool_category ON blender_tools(category);
CREATE INDEX IF NOT EXISTS idx_tool_agent ON blender_tools(agent_id);
CREATE INDEX IF NOT EXISTS idx_tool_mcp ON blender_tools(mcp_server);

-- Workflows
CREATE INDEX IF NOT EXISTS idx_workflow_category ON workflow_definitions(category);
CREATE INDEX IF NOT EXISTS idx_workflow_agencies ON workflow_definitions USING GIN(agencies);
CREATE INDEX IF NOT EXISTS idx_workflow_active ON workflow_definitions(is_active);

-- ============================================================
-- FULL TEXT SEARCH
-- ============================================================

-- Tutorial search
CREATE INDEX IF NOT EXISTS idx_tutorial_fts ON tutorial_knowledge
USING GIN(to_tsvector('english', coalesce(title, '') || ' ' || coalesce(description, '')));

-- API search
CREATE INDEX IF NOT EXISTS idx_api_fts ON api_details
USING GIN(to_tsvector('english', coalesce(description, '') || ' ' || coalesce(function_name, '')));

-- Compatibility search
CREATE INDEX IF NOT EXISTS idx_compat_fts ON compatibility_notes
USING GIN(to_tsvector('english', coalesce(title, '') || ' ' || coalesce(description, '')));

-- ============================================================
-- HELPER FUNCTIONS
-- ============================================================

-- Function to check version compatibility
CREATE OR REPLACE FUNCTION check_blender_version_compatible(
check_version TEXT,
min_version TEXT,
max_version TEXT
) RETURNS BOOLEAN AS $$
DECLARE
check_parts INTEGER[];
min_parts INTEGER[];
max_parts INTEGER[];
BEGIN
-- Parse versions into integer arrays
check_parts := string_to_array(check_version, '.')::INTEGER[];

text

IF min_version IS NOT NULL THEN
    min_parts := string_to_array(min_version, '.')::INTEGER[];
    IF check_parts < min_parts THEN
        RETURN FALSE;
    END IF;
END IF;

IF max_version IS NOT NULL THEN
    max_parts := string_to_array(max_version, '.')::INTEGER[];
    IF check_parts > max_parts THEN
        RETURN FALSE;
    END IF;
END IF;

RETURN TRUE;

END;

-- Function to get compatibility issues for a version and area
CREATE OR REPLACE FUNCTION get_compatibility_issues(
user_version TEXT,
check_area TEXT DEFAULT NULL
) RETURNS TABLE (
note_id TEXT,
title TEXT,
change_type TEXT,
severity TEXT,
description TEXT,
new_method TEXT
) AS $$
BEGIN
RETURN QUERY
SELECT
cn.note_id,
cn.title,
cn.change_type,
cn.severity,
cn.description,
cn.new_method
FROM compatibility_notes cn
WHERE cn.affected_version <= user_version
AND (check_area IS NULL OR cn.affected_area ILIKE '%' || check_area || '%')
AND cn.change_type IN ('breaking_change', 'removal', 'deprecation')
ORDER BY cn.severity DESC, cn.affected_version DESC;
END;

-- ============================================================
-- INITIAL DATA: BLENDER 5.0 COMPATIBILITY NOTES
-- ============================================================

INSERT INTO compatibility_notes (
note_id, affected_version, affected_area, affected_module,
change_type, severity, title, description,
old_method, old_code_pattern, new_method, new_code_pattern,
migration_steps, tags, agent_instructions
) VALUES
-- Grease Pencil 3.0 (Blender 4.3+)
(
'compat_gp3_data_model',
'4.3',
'Grease Pencil',
'bpy.types.GreasePencil',
'breaking_change',
'critical',
'Grease Pencil Data Model Completely Rewritten',
'The Grease Pencil data model has been fully rewritten in Blender 4.3+. Old GP objects are incompatible and must be converted.',
'bpy.types.GreasePencil, bpy.types.GPencilStroke',
'gpencil_obj = bpy.data.grease_pencils.new("GP")',
'bpy.types.GreasePencilv3, new stroke API',
'gpencil_obj = bpy.data.grease_pencils_v3.new("GP")',
'["1. Open file in Blender 4.3+", "2. Use File > Legacy Data > Convert Grease Pencil", "3. Save as new file"]'::JSONB,
ARRAY['grease_pencil', 'gp3', 'migration', 'breaking'],
'CRITICAL: Before any Grease Pencil operation, check user version. If >= 4.3, use GreasePencilv3 API. If migrating old files, run conversion first.'
),
-- Blender 5.0 Blendfile Format
(
'compat_50_blendfile',
'5.0',
'File Format',
'bpy.ops.wm',
'breaking_change',
'critical',
'Blender 5.0 File Format Incompatible with Older Versions',
'Files saved in Blender 5.0 cannot be opened in any older version. This is a permanent forward-only change.',
'Save normally',
NULL,
'Export to intermediate format for older versions',
NULL,
'["1. Keep backup in older format", "2. Use File > Export for compatibility", "3. Use glTF/FBX for external sharing"]'::JSONB,
ARRAY['blender_5', 'file_format', 'compatibility', 'breaking'],
'WARN user before saving: Files saved in 5.0 cannot be opened in older Blender versions. Recommend keeping versioned backups.'
),
-- IDProperties API Change
(
'compat_50_idproperties',
'5.0',
'Python API',
'bpy.types.ID',
'api_change',
'high',
'IDProperties Direct Dict Access Removed',
'Direct dictionary-like access to ID properties is removed. Use explicit methods.',
'obj["custom_prop"]',
'value = obj["my_property"]',
'obj.get("custom_prop") or obj.id_properties_get()',
'value = obj.get("my_property", default_value)',
'["1. Replace obj[key] with obj.get(key, default)", "2. Update all custom property access"]'::JSONB,
ARRAY['api', 'idproperties', 'python', 'blender_5'],
'When accessing custom properties, always use .get() method with default value. Never use direct dict access [].'
),
-- EEVEE Rewrite (Blender 4.2+)
(
'compat_42_eevee_next',
'4.2',
'Rendering',
'bpy.context.scene.eevee',
'breaking_change',
'high',
'EEVEE Completely Rewritten (EEVEE Next)',
'EEVEE rendering engine was completely rewritten in 4.2. Many settings and nodes have changed.',
'Old EEVEE settings',
'scene.eevee.use_gtao = True',
'New EEVEE settings structure',
'scene.eevee.use_raytracing = True',
'["1. Review all EEVEE material settings", "2. Update render settings", "3. Test render output"]'::JSONB,
ARRAY['eevee', 'rendering', 'eevee_next', 'blender_42'],
'For rendering operations in 4.2+, use new EEVEE settings. Check for raytracing and light probe changes.'
),
-- Max Data Block Name Length
(
'compat_50_name_length',
'5.0',
'Data Blocks',
'bpy.types.ID',
'behavior_change',
'medium',
'Maximum Data-Block Name Length Increased',
'Maximum name length increased from 63 bytes to 255 bytes. Old scripts may have hard-coded limits.',
'63 byte limit',
'name = name[:63]',
'255 byte limit',
'name = name[:255]',
'["1. Remove hard-coded 63 character limits", "2. Update name truncation logic"]'::JSONB,
ARRAY['naming', 'data_blocks', 'blender_5'],
'When generating object names, can now use up to 255 characters. Update any name truncation logic.'
),
-- GPU Requirements
(
'compat_50_gpu',
'5.0',
'System Requirements',
NULL,
'breaking_change',
'high',
'Increased GPU Requirements',
'Blender 5.0 requires more modern GPU. Minimum: OpenGL 4.3 / Vulkan 1.2.',
'OpenGL 3.3',
NULL,
'OpenGL 4.3 / Vulkan 1.2',
NULL,
'["1. Check GPU compatibility before upgrade", "2. Update graphics drivers"]'::JSONB,
ARRAY['gpu', 'system_requirements', 'blender_5'],
'Before running GPU-intensive operations, verify user meets minimum GPU requirements.'
),
-- Intel Mac Removed
(
'compat_50_intel_mac',
'5.0',
'Platform Support',
NULL,
'removal',
'critical',
'Intel Mac Support Removed',
'Blender 5.0 no longer supports Intel-based Macs. Apple Silicon only.',
'Intel Mac supported',
NULL,
'Apple Silicon Mac only',
NULL,
'["1. Upgrade to Apple Silicon Mac", "2. Or use Blender 4.2 LTS on Intel Mac"]'::JSONB,
ARRAY['mac', 'intel', 'platform', 'blender_5'],
'If user reports Mac issues, check if Intel Mac. Recommend 4.2 LTS for Intel Mac users.'
)
ON CONFLICT (note_id) DO UPDATE SET
updated_at = NOW(),
description = EXCLUDED.description,
migration_steps = EXCLUDED.migration_steps;

-- ============================================================
-- INITIAL DATA: BLENDER KEYWORDS
-- ============================================================

INSERT INTO blender_keywords (keyword, category, domain, synonyms, maps_to_area) VALUES
('modeling', 'modeling', 'blender', ARRAY['model', 'mesh', '3d modeling'], 'VIEW_3D'),
('sculpting', 'sculpting', 'blender', ARRAY['sculpt', 'clay', 'digital sculpting'], 'VIEW_3D'),
('texturing', 'materials', 'blender', ARRAY['texture', 'uv', 'mapping'], 'IMAGE_EDITOR'),
('materials', 'materials', 'blender', ARRAY['material', 'shader', 'shading'], 'NODE_EDITOR'),
('animation', 'animation', 'blender', ARRAY['animate', 'keyframe', 'motion'], 'DOPESHEET_EDITOR'),
('rigging', 'rigging', 'blender', ARRAY['rig', 'armature', 'bones', 'skeleton'], 'VIEW_3D'),
('rendering', 'rendering', 'blender', ARRAY['render', 'cycles', 'eevee'], 'PROPERTIES'),
('compositing', 'compositing', 'blender', ARRAY['composite', 'post', 'vfx'], 'NODE_EDITOR'),
('geometry nodes', 'geometry_nodes', 'blender', ARRAY['geonodes', 'procedural'], 'NODE_EDITOR'),
('grease pencil', 'grease_pencil', 'blender', ARRAY['gpencil', '2d animation', 'drawing'], 'VIEW_3D'),
('lighting', 'lighting', 'blender', ARRAY['light', 'illumination', 'hdri'], 'VIEW_3D'),
('camera', 'camera', 'blender', ARRAY['cam', 'view', 'shot'], 'VIEW_3D'),
('physics', 'physics', 'blender', ARRAY['simulation', 'dynamics', 'cloth', 'fluid'], 'PROPERTIES'),
('particles', 'particles', 'blender', ARRAY['particle', 'hair', 'fur'], 'PROPERTIES'),
('motion tracking', 'vfx', 'blender', ARRAY['tracking', 'camera tracking', 'matchmove'], 'CLIP_EDITOR'),
('video editing', 'vse', 'blender', ARRAY['vse', 'sequencer', 'editing'], 'SEQUENCE_EDITOR')
ON CONFLICT (keyword) DO NOTHING;

COMMIT;

🎬 PART 2: VFX AGENCY AGENTS
2.1 VFX Agency Init

File: agencies/blender/vfx/agents/init.py

Python

"""
VFX Agency Agents
Sub-agency of Blender Agency for VFX operations

Agents:

    VFXLayoutArtist: Build 3D scenes from plates/cards + footage
    CameraTrackingAgent: Perform tracking, solve, lens setup
    ProjectionMappingAgent: Create camera projection from images/matte paintings
    IntegrationAgent: Add generated elements (assets, geometry nodes, AI images)
    """

from .vfx_layout_artist import VFXLayoutArtist
from .camera_tracking_agent import CameraTrackingAgent
from .projection_mapping_agent import ProjectionMappingAgent
from .integration_agent import IntegrationAgent

all = [
"VFXLayoutArtist",
"CameraTrackingAgent",
"ProjectionMappingAgent",
"IntegrationAgent",
]
Agent registry for MCP

VFX_AGENTS = {
"vfx_layout_artist": VFXLayoutArtist,
"camera_tracking_agent": CameraTrackingAgent,
"projection_mapping_agent": ProjectionMappingAgent,
"integration_agent": IntegrationAgent,
}

2.2 VFX Layout Artist Agent

File: agencies/blender/vfx/agents/vfx_layout_artist.py

Python

"""
VFX Layout Artist Agent
Builds 3D scenes from plates, cards, and footage for VFX work.

Capabilities:

    Create geometry for projection
    Setup camera and scene from tracking data
    Build parallax card setups
    Create depth-based scene layouts
    """

import json
from typing import Dict, Any, Optional, List
from pathlib import Path
from datetime import datetime, timezone

from core.base_agent import BaseAgent
from config.settings import settings
from loguru import logger

class VFXLayoutArtist(BaseAgent):
"""
VFX Layout Artist - Builds 3D scenes for VFX compositing.

text

This agent specializes in:
- Creating projection geometry from matte paintings
- Setting up camera rigs for parallax effects
- Building card-based environments
- Preparing scenes for camera tracking integration
"""

def __init__(self, **kwargs):
    super().__init__(
        agent_id="vfx_layout_artist",
        agency="blender",
        description="Builds 3D scenes from plates, cards, and footage for VFX work",
        **kwargs
    )
    
    # VFX-specific settings
    self.temp_vfx_path = Path(settings.PROJECT_ROOT) / "data" / "temp_vfx"
    self.temp_vfx_path.mkdir(parents=True, exist_ok=True)
    
    # Blender version for compatibility
    self.blender_version = "5.0"

async def execute_task(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main task execution dispatcher.
    
    Supported tasks:
    - setup_vfx_scene: Initialize a VFX scene with proper settings
    - create_projection_plane: Create a plane for matte painting projection
    - create_parallax_cards: Create multiple cards at different depths
    - create_depth_geometry: Create geometry from depth map
    - setup_camera_rig: Setup camera with constraints for VFX work
    """
    task_type = params.get("task_type", "setup_vfx_scene")
    
    task_handlers = {
        "setup_vfx_scene": self._setup_vfx_scene,
        "create_projection_plane": self._create_projection_plane,
        "create_parallax_cards": self._create_parallax_cards,
        "create_depth_geometry": self._create_depth_geometry,
        "setup_camera_rig": self._setup_camera_rig,
    }
    
    handler = task_handlers.get(task_type)
    if not handler:
        return {"status": "error", "message": f"Unknown task type: {task_type}"}
    
    try:
        # Check compatibility before execution
        compat_issues = await self._check_compatibility(params)
        if compat_issues:
            logger.warning(f"Compatibility issues found: {compat_issues}")
            params["_compatibility_warnings"] = compat_issues
        
        result = await handler(params)
        return result
    except Exception as e:
        logger.error(f"VFX Layout Artist error: {e}")
        return {"status": "error", "message": str(e)}

async def _check_compatibility(self, params: Dict[str, Any]) -> List[str]:
    """Check for Blender version compatibility issues."""
    warnings = []
    
    try:
        # Query compatibility database
        query = """
            SELECT title, description, new_method 
            FROM compatibility_notes 
            WHERE affected_area IN ('Rendering', 'Compositing', 'Camera')
            AND affected_version <= $1
            AND change_type IN ('breaking_change', 'deprecation')
            ORDER BY affected_version DESC
            LIMIT 5
        """
        results = await self.db.fetch_all(query, [self.blender_version])
        
        for row in results:
            warnings.append(f⚠️ {row['title']}: {row['new_method'] or row['description'][:100]}")
    except Exception as e:
        logger.debug(f"Compatibility check skipped: {e}")
    
    return warnings

async def _setup_vfx_scene(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Initialize a VFX scene with proper settings.
    
    Args:
        shot_name: Name for the VFX shot
        resolution_x: Render resolution X (default: 1920)
        resolution_y: Render resolution Y (default: 1080)
        fps: Frame rate (default: 24)
        frame_start: Start frame (default: 1)
        frame_end: End frame (default: 250)
    """
    shot_name = params.get("shot_name", "VFX_Shot")
    resolution_x = params.get("resolution_x", 1920)
    resolution_y = params.get("resolution_y", 1080)
    fps = params.get("fps", 24)
    frame_start = params.get("frame_start", 1)
    frame_end = params.get("frame_end", 250)
    
    script = f'''

import bpy
Clear default scene

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
Scene settings

scene = bpy.context.scene
scene.name = "{shot_name}"
Render settings

scene.render.resolution_x = {resolution_x}
scene.render.resolution_y = {resolution_y}
scene.render.fps = {fps}
Frame range

scene.frame_start = {frame_start}
scene.frame_end = {frame_end}
scene.frame_current = {frame_start}
VFX-optimized render settings

scene.render.engine = 'BLENDER_EEVEE_NEXT' # EEVEE Next for fast preview
scene.render.film_transparent = True # Transparent background for compositing
Color management for VFX

scene.view_settings.view_transform = 'Standard' # Linear workflow
Create VFX collections

vfx_collection = bpy.data.collections.new("{shot_name}_VFX")
bpy.context.scene.collection.children.link(vfx_collection)

plates_collection = bpy.data.collections.new("Plates")
vfx_collection.children.link(plates_collection)

geometry_collection = bpy.data.collections.new("Geometry")
vfx_collection.children.link(geometry_collection)

cameras_collection = bpy.data.collections.new("Cameras")
vfx_collection.children.link(cameras_collection)
Add main VFX camera

bpy.ops.object.camera_add(location=(0, -10, 2))
camera = bpy.context.active_object
camera.name = "{shot_name}_Camera"
cameras_collection.objects.link(camera)
bpy.context.scene.collection.objects.unlink(camera)
scene.camera = camera
Camera settings for VFX

camera.data.lens = 35 # Standard lens
camera.data.sensor_width = 36 # Full frame sensor
camera.data.clip_start = 0.1
camera.data.clip_end = 10000

print(f"VFX Scene '{{scene.name}}' created successfully")
print(f"Resolution: {{scene.render.resolution_x}}x{{scene.render.resolution_y}} @ {{scene.render.fps}}fps")
'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "shot_name": shot_name,
        "resolution": f"{resolution_x}x{resolution_y}",
        "fps": fps,
        "frame_range": f"{frame_start}-{frame_end}",
        "blender_result": result,
        "compatibility_warnings": params.get("_compatibility_warnings", [])
    }

async def _create_projection_plane(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a plane for matte painting projection.
    
    Args:
        image_path: Path to the matte painting image
        plane_name: Name for the projection plane
        distance: Distance from camera (default: 100)
        scale: Scale multiplier (default: 1.0)
    """
    image_path = params.get("image_path", "")
    plane_name = params.get("plane_name", "Projection_Plane")
    distance = params.get("distance", 100)
    scale = params.get("scale", 1.0)
    
    if not image_path:
        return {"status": "error", "message": "image_path is required"}
    
    # Escape path for Python
    image_path_escaped = image_path.replace("\\", "\\\\")
    
    script = f'''

import bpy
import os
Load image

image_path = r"{image_path_escaped}"
if not os.path.exists(image_path):
raise FileNotFoundError(f"Image not found: {{image_path}}")

image = bpy.data.images.load(image_path)
img_width, img_height = image.size
Calculate aspect ratio

aspect_ratio = img_width / img_height
Create projection plane

bpy.ops.mesh.primitive_plane_add(size=1, location=(0, {distance}, 0))
plane = bpy.context.active_object
plane.name = "{plane_name}"
Scale plane to match image aspect

plane.scale.x = {distance} * aspect_ratio * {scale}
plane.scale.z = {distance} * {scale}
bpy.ops.object.transform_apply(scale=True)
Rotate to face camera (assuming camera at Y-)

plane.rotation_euler.x = 1.5708 # 90 degrees
Create emission material for projection

mat = bpy.data.materials.new(name="{plane_name}_Material")
mat.use_nodes = True
nodes = mat.node_tree.nodes
links = mat.node_tree.links
Clear default nodes

nodes.clear()
Add nodes

output = nodes.new('ShaderNodeOutputMaterial')
emission = nodes.new('ShaderNodeEmission')
tex_image = nodes.new('ShaderNodeTexImage')
tex_coord = nodes.new('ShaderNodeTexCoord')
Position nodes

output.location = (300, 0)
emission.location = (100, 0)
tex_image.location = (-200, 0)
tex_coord.location = (-400, 0)
Setup texture

tex_image.image = image
Connect nodes

links.new(tex_coord.outputs['UV'], tex_image.inputs['Vector'])
links.new(tex_image.outputs['Color'], emission.inputs['Color'])
links.new(emission.outputs['Emission'], output.inputs['Surface'])
Assign material

plane.data.materials.append(mat)
Add to VFX collection if exists

for coll in bpy.data.collections:
if 'Plates' in coll.name:
coll.objects.link(plane)
bpy.context.scene.collection.objects.unlink(plane)
break

print(f"Projection plane '{{plane.name}}' created")
print(f"Image size: {{img_width}}x{{img_height}}, Aspect: {{aspect_ratio:.2f}}")
'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "plane_name": plane_name,
        "image_path": image_path,
        "distance": distance,
        "blender_result": result
    }

async def _create_parallax_cards(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create multiple cards at different depths for parallax effect.
    
    Args:
        cards: List of card definitions
               [{"image_path": "...", "depth": 50, "name": "BG_Layer"}]
        camera_name: Name of the camera to use for projection
    """
    cards = params.get("cards", [])
    camera_name = params.get("camera_name", "Camera")
    
    if not cards:
        return {"status": "error", "message": "cards list is required"}
    
    created_cards = []
    for i, card in enumerate(cards):
        result = await self._create_projection_plane({
            "image_path": card.get("image_path", ""),
            "plane_name": card.get("name", f"Parallax_Card_{i}"),
            "distance": card.get("depth", 50 + i * 20),
            "scale": card.get("scale", 1.0)
        })
        created_cards.append(result)
    
    return {
        "status": "success",
        "cards_created": len(created_cards),
        "cards": created_cards
    }

async def _create_depth_geometry(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create geometry from a depth map for parallax displacement.
    
    Args:
        color_image: Path to color/albedo image
        depth_image: Path to depth map image
        displacement_strength: Strength of displacement (default: 1.0)
        subdivisions: Number of subdivisions (default: 100)
    """
    color_image = params.get("color_image", "")
    depth_image = params.get("depth_image", "")
    displacement_strength = params.get("displacement_strength", 1.0)
    subdivisions = params.get("subdivisions", 100)
    
    color_escaped = color_image.replace("\\", "\\\\")
    depth_escaped = depth_image.replace("\\", "\\\\")
    
    script = f'''

import bpy
Create subdivided plane

bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, 0))
plane = bpy.context.active_object
plane.name = "Depth_Geometry"
Subdivide for displacement

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.subdivide(number_cuts={subdivisions})
bpy.ops.object.mode_set(mode='OBJECT')
Create material with displacement

mat = bpy.data.materials.new(name="Depth_Material")
mat.use_nodes = True
nodes = mat.node_tree.nodes
links = mat.node_tree.links

nodes.clear()
Nodes

output = nodes.new('ShaderNodeOutputMaterial')
principled = nodes.new('ShaderNodeBsdfPrincipled')
tex_color = nodes.new('ShaderNodeTexImage')
tex_depth = nodes.new('ShaderNodeTexImage')
displacement = nodes.new('ShaderNodeDisplacement')
Load images

if r"{color_escaped}":
tex_color.image = bpy.data.images.load(r"{color_escaped}")
if r"{depth_escaped}":
tex_depth.image = bpy.data.images.load(r"{depth_escaped}")
tex_depth.image.colorspace_settings.name = 'Non-Color'
Connect

links.new(tex_color.outputs['Color'], principled.inputs['Base Color'])
links.new(principled.outputs['BSDF'], output.inputs['Surface'])
links.new(tex_depth.outputs['Color'], displacement.inputs['Height'])
displacement.inputs['Scale'].default_value = {displacement_strength}
links.new(displacement.outputs['Displacement'], output.inputs['Displacement'])
Enable displacement

mat.cycles.displacement_method = 'BOTH'
plane.data.materials.append(mat)
Add displacement modifier for viewport

mod = plane.modifiers.new(name="Displace", type='DISPLACE')
if tex_depth.image:
disp_tex = bpy.data.textures.new("Depth_Tex", type='IMAGE')
disp_tex.image = tex_depth.image
mod.texture = disp_tex
mod.strength = {displacement_strength}

print(f"Depth geometry created with {{subdivisions * subdivisions}} faces")
'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "displacement_strength": displacement_strength,
        "subdivisions": subdivisions,
        "blender_result": result
    }

async def _setup_camera_rig(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Setup a camera rig for VFX work with constraints.
    
    Args:
        camera_name: Name for the camera
        rig_type: Type of rig ('static', 'track_to', 'follow_path')
        target_name: Object to track (for track_to)
    """
    camera_name = params.get("camera_name", "VFX_Camera")
    rig_type = params.get("rig_type", "static")
    target_name = params.get("target_name", "")
    
    script = f'''

import bpy
Create camera if not exists

camera = bpy.data.objects.get("{camera_name}")
if not camera:
bpy.ops.object.camera_add(location=(0, -10, 2))
camera = bpy.context.active_object
camera.name = "{camera_name}"
Camera settings

camera.data.lens = 35
camera.data.sensor_width = 36

rig_type = "{rig_type}"

if rig_type == "track_to":
target = bpy.data.objects.get("{target_name}")
if target:
constraint = camera.constraints.new('TRACK_TO')
constraint.target = target
constraint.track_axis = 'TRACK_NEGATIVE_Z'
constraint.up_axis = 'UP_Y'

elif rig_type == "follow_path":
# Create camera path
bpy.ops.curve.primitive_bezier_curve_add()
path = bpy.context.active_object
path.name = "{camera_name}_Path"

text

constraint = camera.constraints.new('FOLLOW_PATH')
constraint.target = path
constraint.use_curve_follow = True

Set as scene camera

bpy.context.scene.camera = camera

print(f"Camera rig '{{camera.name}}' created with {{rig_type}} setup")
'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "camera_name": camera_name,
        "rig_type": rig_type,
        "blender_result": result
    }

def get_tools(self) -> List[Dict[str, Any]]:
    """Return MCP tool definitions for this agent."""
    return [
        {
            "name": "setup_vfx_scene",
            "description": "Initialize a VFX scene with proper settings for compositing work",
            "parameters": {
                "shot_name": {"type": "string", "description": "Name for the VFX shot"},
                "resolution_x": {"type": "integer", "default": 1920},
                "resolution_y": {"type": "integer", "default": 1080},
                "fps": {"type": "integer", "default": 24},
                "frame_start": {"type": "integer", "default": 1},
                "frame_end": {"type": "integer", "default": 250}
            }
        },
        {
            "name": "create_projection_plane",
            "description": "Create a plane for matte painting projection",
            "parameters": {
                "image_path": {"type": "string", "required": True},
                "plane_name": {"type": "string", "default": "Projection_Plane"},
                "distance": {"type": "number", "default": 100},
                "scale": {"type": "number", "default": 1.0}
            }
        },
        {
            "name": "create_parallax_cards",
            "description": "Create multiple cards at different depths for parallax",
            "parameters": {
                "cards": {"type": "array", "required": True},
                "camera_name": {"type": "string", "default": "Camera"}
            }
        },
        {
            "name": "create_depth_geometry",
            "description": "Create geometry from depth map for displacement",
            "parameters": {
                "color_image": {"type": "string"},
                "depth_image": {"type": "string"},
                "displacement_strength": {"type": "number", "default": 1.0},
                "subdivisions": {"type": "integer", "default": 100}
            }
        },
        {
            "name": "setup_camera_rig",
            "description": "Setup camera rig with constraints for VFX",
            "parameters": {
                "camera_name": {"type": "string", "default": "VFX_Camera"},
                "rig_type": {"type": "string", "enum": ["static", "track_to", "follow_path"]},
                "target_name": {"type": "string"}
            }
        }
    ]

2.3 Camera Tracking Agent

File: agencies/blender/vfx/agents/camera_tracking_agent.py

Python

"""
Camera Tracking Agent
Performs motion tracking, camera solving, and lens setup.

Capabilities:

    Load and analyze footage
    Detect and track features
    Solve camera motion
    Setup lens distortion
    Create tracking geometry
    """

import json
from typing import Dict, Any, Optional, List
from pathlib import Path

from core.base_agent import BaseAgent
from config.settings import settings
from loguru import logger

class CameraTrackingAgent(BaseAgent):
"""
Camera Tracking Agent - Solves camera motion from footage.

text

This agent specializes in:
- Loading footage into Movie Clip Editor
- Automatic feature detection and tracking
- Camera motion solving
- Lens distortion calibration
- Creating 3D geometry from tracking data
"""

def __init__(self, **kwargs):
    super().__init__(
        agent_id="camera_tracking_agent",
        agency="blender",
        description="Performs motion tracking, camera solving, and lens setup",
        **kwargs
    )
    self.blender_version = "5.0"

async def execute_task(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main task execution dispatcher.
    
    Supported tasks:
    - load_footage: Load video footage for tracking
    - detect_features: Auto-detect tracking features
    - track_markers: Track detected markers
    - solve_camera: Solve camera motion
    - setup_lens: Configure lens distortion
    - create_tracking_scene: Create 3D scene from solve
    """
    task_type = params.get("task_type", "load_footage")
    
    task_handlers = {
        "load_footage": self._load_footage,
        "detect_features": self._detect_features,
        "track_markers": self._track_markers,
        "solve_camera": self._solve_camera,
        "setup_lens": self._setup_lens,
        "create_tracking_scene": self._create_tracking_scene,
        "full_tracking_pipeline": self._full_tracking_pipeline,
    }
    
    handler = task_handlers.get(task_type)
    if not handler:
        return {"status": "error", "message": f"Unknown task type: {task_type}"}
    
    try:
        # Check compatibility
        compat_issues = await self._check_compatibility()
        if compat_issues:
            params["_compatibility_warnings"] = compat_issues
        
        result = await handler(params)
        return result
    except Exception as e:
        logger.error(f"Camera Tracking Agent error: {e}")
        return {"status": "error", "message": str(e)}

async def _check_compatibility(self) -> List[str]:
    """Check for tracking-related compatibility issues."""
    warnings = []
    try:
        query = """
            SELECT title, description, new_method
            FROM compatibility_notes
            WHERE affected_area ILIKE '%tracking%' 
               OR affected_area ILIKE '%camera%'
               OR affected_area ILIKE '%movie clip%'
            AND affected_version <= $1
            LIMIT 3
        """
        results = await self.db.fetch_all(query, [self.blender_version])
        for row in results:
            warnings.append(f"⚠️ {row['title']}")
    except Exception as e:
        logger.debug(f"Compatibility check skipped: {e}")
    return warnings

async def _load_footage(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Load video footage into the Movie Clip Editor.
    
    Args:
        footage_path: Path to video file
        clip_name: Name for the clip (optional)
    """
    footage_path = params.get("footage_path", "")
    clip_name = params.get("clip_name", "Tracking_Footage")
    
    if not footage_path:
        return {"status": "error", "message": "footage_path is required"}
    
    footage_escaped = footage_path.replace("\\", "\\\\")
    
    script = f'''

import bpy
import os

footage_path = r"{footage_escaped}"
if not os.path.exists(footage_path):
raise FileNotFoundError(f"Footage not found: {{footage_path}}")
Load clip

clip = bpy.data.movieclips.load(footage_path)
clip.name = "{clip_name}"
Get clip info

frame_start = clip.frame_start
frame_duration = clip.frame_duration
size = clip.size
Set scene to match clip

scene = bpy.context.scene
scene.frame_start = frame_start
scene.frame_end = frame_start + frame_duration - 1
scene.render.resolution_x = size[0]
scene.render.resolution_y = size[1]
Switch to clip editor

for area in bpy.context.screen.areas:
if area.type == 'CLIP_EDITOR':
area.spaces.active.clip = clip
break

print(f"Loaded footage: {{clip.name}}")
print(f"Size: {{size[0]}}x{{size[1]}}, Frames: {{frame_duration}}")
'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "clip_name": clip_name,
        "footage_path": footage_path,
        "blender_result": result
    }

async def _detect_features(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Auto-detect tracking features in the footage.
    
    Args:
        clip_name: Name of the clip to process
        threshold: Detection threshold (default: 0.5)
        min_distance: Minimum distance between markers
        margin: Margin from frame edges
    """
    clip_name = params.get("clip_name", "")
    threshold = params.get("threshold", 0.5)
    min_distance = params.get("min_distance", 100)
    margin = params.get("margin", 16)
    
    script = f'''

import bpy
Get clip

clip = bpy.data.movieclips.get("{clip_name}")
if not clip:
clip = list(bpy.data.movieclips)[-1] if bpy.data.movieclips else None

if not clip:
raise ValueError("No movie clip available")
Set clip as active

for area in bpy.context.screen.areas:
if area.type == 'CLIP_EDITOR':
area.spaces.active.clip = clip
break
Detect features

bpy.ops.clip.detect_features(
threshold={threshold},
min_distance={min_distance},
margin={margin}
)
Count markers

tracking = clip.tracking
markers_count = len(tracking.tracks)

print(f"Detected {{markers_count}} tracking markers")
'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "threshold": threshold,
        "blender_result": result
    }

async def _track_markers(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Track detected markers through the footage.
    
    Args:
        clip_name: Name of the clip
        forwards: Track forwards (default: True)
        backwards: Track backwards (default: True)
    """
    clip_name = params.get("clip_name", "")
    forwards = params.get("forwards", True)
    backwards = params.get("backwards", True)
    
    script = f'''

import bpy
Get clip

clip = bpy.data.movieclips.get("{clip_name}")
if not clip:
clip = list(bpy.data.movieclips)[-1] if bpy.data.movieclips else None

if not clip:
raise ValueError("No movie clip available")
Set clip as active

for area in bpy.context.screen.areas:
if area.type == 'CLIP_EDITOR':
area.spaces.active.clip = clip
# Override context for tracking
with bpy.context.temp_override(area=area):
# Track forwards
if {str(forwards).lower()}:
bpy.ops.clip.track_markers(backwards=False, sequence=True)

text

        # Track backwards
        if {str(backwards).lower()}:
            bpy.ops.clip.track_markers(backwards=True, sequence=True)
    break

Get tracking stats

tracking = clip.tracking
good_tracks = sum(1 for t in tracking.tracks if len(t.markers) > 10)

print(f"Tracking complete. Good tracks: {{good_tracks}}")
'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "forwards": forwards,
        "backwards": backwards,
        "blender_result": result
    }

async def _solve_camera(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Solve camera motion from tracked markers.
    
    Args:
        clip_name: Name of the clip
        focal_length: Known focal length (optional)
        sensor_width: Sensor width in mm (default: 36)
    """
    clip_name = params.get("clip_name", "")
    focal_length = params.get("focal_length")
    sensor_width = params.get("sensor_width", 36)
    
    focal_setup = ""
    if focal_length:
        focal_setup = f"""

Set known focal length

clip.tracking.camera.focal_length = {focal_length}
clip.tracking.camera.focal_length_pixels = {focal_length} * clip.size[0] / {sensor_width}
"""

text

    script = f'''

import bpy
Get clip

clip = bpy.data.movieclips.get("{clip_name}")
if not clip:
clip = list(bpy.data.movieclips)[-1] if bpy.data.movieclips else None

if not clip:
raise ValueError("No movie clip available")
Camera settings

clip.tracking.camera.sensor_width = {sensor_width}
{focal_setup}
Set clip as active and solve

for area in bpy.context.screen.areas:
if area.type == 'CLIP_EDITOR':
area.spaces.active.clip = clip
with bpy.context.temp_override(area=area):
bpy.ops.clip.solve_camera()
break
Get solve error

reconstruction = clip.tracking.reconstruction
solve_error = reconstruction.average_error if reconstruction else -1

print(f"Camera solve complete. Average error: {{solve_error:.4f}} px")
'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "sensor_width": sensor_width,
        "focal_length": focal_length,
        "blender_result": result
    }

async def _setup_lens(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Configure lens distortion settings.
    
    Args:
        clip_name: Name of the clip
        distortion_model: 'POLYNOMIAL' or 'DIVISION'
        k1, k2, k3: Distortion coefficients
    """
    clip_name = params.get("clip_name", "")
    distortion_model = params.get("distortion_model", "POLYNOMIAL")
    k1 = params.get("k1", 0.0)
    k2 = params.get("k2", 0.0)
    k3 = params.get("k3", 0.0)
    
    script = f'''

import bpy

clip = bpy.data.movieclips.get("{clip_name}")
if not clip:
clip = list(bpy.data.movieclips)[-1] if bpy.data.movieclips else None

if clip:
camera = clip.tracking.camera
camera.distortion_model = '{distortion_model}'
camera.k1 = {k1}
camera.k2 = {k2}
camera.k3 = {k3}

text

print(f"Lens distortion configured: K1={{camera.k1}}, K2={{camera.k2}}, K3={{camera.k3}}")

'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "distortion_model": distortion_model,
        "blender_result": result
    }

async def _create_tracking_scene(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create 3D scene from camera solve.
    
    Args:
        clip_name: Name of the clip
        setup_tracking_scene: Setup scene with tracked camera
    """
    clip_name = params.get("clip_name", "")
    
    script = f'''

import bpy

clip = bpy.data.movieclips.get("{clip_name}")
if not clip:
clip = list(bpy.data.movieclips)[-1] if bpy.data.movieclips else None

if not clip:
raise ValueError("No movie clip available")
Set clip as active

for area in bpy.context.screen.areas:
if area.type == 'CLIP_EDITOR':
area.spaces.active.clip = clip
with bpy.context.temp_override(area=area):
# Setup tracking scene
bpy.ops.clip.setup_tracking_scene()
break

print("Tracking scene created with solved camera and track points")
'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "blender_result": result
    }

async def _full_tracking_pipeline(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Run the complete tracking pipeline from footage to solved camera.
    
    Args:
        footage_path: Path to video file
        focal_length: Known focal length (optional)
        auto_detect: Auto-detect features (default: True)
    """
    footage_path = params.get("footage_path", "")
    
    if not footage_path:
        return {"status": "error", "message": "footage_path is required"}
    
    results = []
    
    # Step 1: Load footage
    load_result = await self._load_footage({"footage_path": footage_path})
    results.append(("load_footage", load_result))
    
    if load_result.get("status") != "success":
        return {"status": "error", "step": "load_footage", "results": results}
    
    # Step 2: Detect features
    detect_result = await self._detect_features({})
    results.append(("detect_features", detect_result))
    
    # Step 3: Track markers
    track_result = await self._track_markers({})
    results.append(("track_markers", track_result))
    
    # Step 4: Solve camera
    solve_params = {}
    if params.get("focal_length"):
        solve_params["focal_length"] = params["focal_length"]
    
    solve_result = await self._solve_camera(solve_params)
    results.append(("solve_camera", solve_result))
    
    # Step 5: Create tracking scene
    scene_result = await self._create_tracking_scene({})
    results.append(("create_tracking_scene", scene_result))
    
    return {
        "status": "success",
        "pipeline": "complete",
        "steps_completed": len(results),
        "results": results
    }

def get_tools(self) -> List[Dict[str, Any]]:
    """Return MCP tool definitions for this agent."""
    return [
        {
            "name": "load_footage",
            "description": "Load video footage for camera tracking",
            "parameters": {
                "footage_path": {"type": "string", "required": True},
                "clip_name": {"type": "string", "default": "Tracking_Footage"}
            }
        },
        {
            "name": "detect_features",
            "description": "Auto-detect tracking features in footage",
            "parameters": {
                "clip_name": {"type": "string"},
                "threshold": {"type": "number", "default": 0.5},
                "min_distance": {"type": "integer", "default": 100}
            }
        },
        {
            "name": "track_markers",
            "description": "Track markers through footage",
            "parameters": {
                "clip_name": {"type": "string"},
                "forwards": {"type": "boolean", "default": True},
                "backwards": {"type": "boolean", "default": True}
            }
        },
        {
            "name": "solve_camera",
            "description": "Solve camera motion from tracking data",
            "parameters": {
                "clip_name": {"type": "string"},
                "focal_length": {"type": "number"},
                "sensor_width": {"type": "number", "default": 36}
            }
        },
        {
            "name": "full_tracking_pipeline",
            "description": "Run complete tracking pipeline from footage to solved camera",
            "parameters": {
                "footage_path": {"type": "string", "required": True},
                "focal_length": {"type": "number"}
            }
        }
    ]

2.4 Projection Mapping Agent

File: agencies/blender/vfx/agents/projection_mapping_agent.py

Python

"""
Projection Mapping Agent
Creates camera projection from images and matte paintings.

Capabilities:

    Project images onto geometry
    Create depth-based parallax
    Setup UV projection from camera
    Generate matte paintings with Z-Image
    """

import json
from typing import Dict, Any, Optional, List
from pathlib import Path
from datetime import datetime, timezone

from core.base_agent import BaseAgent
from config.settings import settings
from loguru import logger

class ProjectionMappingAgent(BaseAgent):
"""
Projection Mapping Agent - Creates camera projections for VFX.

text

This agent specializes in:
- Camera projection mapping
- Matte painting projection
- Depth-based parallax effects
- AI-generated background integration via Z-Image
"""

def __init__(self, **kwargs):
    super().__init__(
        agent_id="projection_mapping_agent",
        agency="blender",
        description="Creates camera projection from images and matte paintings",
        **kwargs
    )
    
    self.z_image_output_dir = Path(settings.PROJECT_ROOT) / "data" / "generated" / "z_image"
    self.z_image_output_dir.mkdir(parents=True, exist_ok=True)
    self.blender_version = "5.0"

async def execute_task(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Main task execution dispatcher.
    
    Supported tasks:
    - generate_matte_painting: Generate matte painting with Z-Image
    - setup_camera_projection: Setup camera projection for image
    - create_projection_material: Create material for projection
    - project_to_geometry: Project image onto 3D geometry
    - create_parallax_scene: Create parallax scene from image + depth
    """
    task_type = params.get("task_type", "setup_camera_projection")
    
    task_handlers = {
        "generate_matte_painting": self._generate_matte_painting,
        "setup_camera_projection": self._setup_camera_projection,
        "create_projection_material": self._create_projection_material,
        "project_to_geometry": self._project_to_geometry,
        "create_parallax_scene": self._create_parallax_scene,
    }
    
    handler = task_handlers.get(task_type)
    if not handler:
        return {"status": "error", "message": f"Unknown task type: {task_type}"}
    
    try:
        result = await handler(params)
        return result
    except Exception as e:
        logger.error(f"Projection Mapping Agent error: {e}")
        return {"status": "error", "message": str(e)}

async def _generate_matte_painting(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate a matte painting using Z-Image AI.
    
    Args:
        prompt: Description of the matte painting
        style: Style preset ('cinematic', 'fantasy', 'scifi', 'realistic')
        width: Image width (default: 1920)
        height: Image height (default: 1080)
    """
    prompt = params.get("prompt", "Epic cinematic landscape, dramatic clouds, photorealistic")
    style = params.get("style", "cinematic")
    width = params.get("width", 1920)
    height = params.get("height", 1080)
    
    # Style presets
    style_modifiers = {
        "cinematic": ", cinematic lighting, dramatic atmosphere, 4K matte painting",
        "fantasy": ", fantasy art style, magical atmosphere, detailed environment",
        "scifi": ", science fiction, futuristic, detailed technology, cinematic",
        "realistic": ", photorealistic, high detail, natural lighting, 8K quality"
    }
    
    full_prompt = prompt + style_modifiers.get(style, style_modifiers["cinematic"])
    
    # Generate filename
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    output_filename = f"matte_painting_{timestamp}.png"
    output_path = self.z_image_output_dir / output_filename
    
    # Call Z-Image generator via Content Agency
    try:
        result = await self.use_tool(
            "content", "image_generator", "generate_z_image",
            prompt=full_prompt,
            output_path=str(output_path),
            width=width,
            height=height
        )
        
        if result and result.get("status") == "success":
            # Save metadata
            metadata = {
                "prompt": full_prompt,
                "style": style,
                "width": width,
                "height": height,
                "output_path": str(output_path),
                "generated_at": timestamp,
                "model": "Z-Image-Turbo"
            }
            
            metadata_path = self.z_image_output_dir / f"{output_filename}.json"
            metadata_path.write_text(json.dumps(metadata, indent=2))
            
            return {
                "status": "success",
                "image_path": str(output_path),
                "metadata": metadata
            }
    except Exception as e:
        logger.warning(f"Z-Image generation failed, using fallback: {e}")
    
    # Fallback: Use a placeholder or existing image
    return {
        "status": "warning",
        "message": "Z-Image generation not available. Use manual image.",
        "expected_path": str(output_path)
    }

async def _setup_camera_projection(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Setup camera projection for an image onto geometry.
    
    Args:
        image_path: Path to the image to project
        camera_name: Name of the projection camera
        target_object: Object to project onto
    """
    image_path = params.get("image_path", "")
    camera_name = params.get("camera_name", "Projection_Camera")
    target_object = params.get("target_object", "")
    
    if not image_path:
        return {"status": "error", "message": "image_path is required"}
    
    image_escaped = image_path.replace("\\", "\\\\")
    
    script = f'''

import bpy
import os

image_path = r"{image_escaped}"
if not os.path.exists(image_path):
raise FileNotFoundError(f"Image not found: {{image_path}}")
Load image

image = bpy.data.images.load(image_path)
Get or create projection camera

camera = bpy.data.objects.get("{camera_name}")
if not camera:
bpy.ops.object.camera_add(location=(0, -10, 2))
camera = bpy.context.active_object
camera.name = "{camera_name}"
Set camera as background

camera.data.show_background_images = True
bg = camera.data.background_images.new()
bg.image = image
bg.display_depth = 'FRONT'
bg.alpha = 0.5
Create projection empty for UV Project modifier

bpy.ops.object.empty_add(type='IMAGE', location=camera.location)
projector = bpy.context.active_object
projector.name = "{camera_name}_Projector"
projector.data = image
projector.empty_display_size = 5
Copy camera transforms to projector

projector.location = camera.location
projector.rotation_euler = camera.rotation_euler
If target object specified, add UV Project modifier

target = bpy.data.objects.get("{target_object}")
if target:
mod = target.modifiers.new(name="UV_Project", type='UV_PROJECT')
mod.projectors[0].object = projector
mod.scale_x = image.size[0] / 1000
mod.scale_y = image.size[1] / 1000

print(f"Camera projection setup complete: {{camera.name}}")
'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "camera_name": camera_name,
        "image_path": image_path,
        "blender_result": result
    }

async def _create_projection_material(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a material for camera projection.
    
    Args:
        image_path: Path to the image
        material_name: Name for the material
        use_emission: Use emission shader (for unlit look)
        mix_factor: Mix with base color (0-1)
    """
    image_path = params.get("image_path", "")
    material_name = params.get("material_name", "Projection_Material")
    use_emission = params.get("use_emission", True)
    mix_factor = params.get("mix_factor", 1.0)
    
    if not image_path:
        return {"status": "error", "message": "image_path is required"}
    
    image_escaped = image_path.replace("\\", "\\\\")
    
    shader_type = "ShaderNodeEmission" if use_emission else "ShaderNodeBsdfPrincipled"
    
    script = f'''

import bpy
import os

image_path = r"{image_escaped}"
if not os.path.exists(image_path):
raise FileNotFoundError(f"Image not found: {{image_path}}")
Load image

image = bpy.data.images.load(image_path)
Create material

mat = bpy.data.materials.new(name="{material_name}")
mat.use_nodes = True
nodes = mat.node_tree.nodes
links = mat.node_tree.links
Clear default nodes

nodes.clear()
Add nodes

output = nodes.new('ShaderNodeOutputMaterial')
shader = nodes.new('{shader_type}')
tex_image = nodes.new('ShaderNodeTexImage')
tex_coord = nodes.new('ShaderNodeTexCoord')
mapping = nodes.new('ShaderNodeMapping')
Position nodes

output.location = (400, 0)
shader.location = (200, 0)
tex_image.location = (-100, 0)
mapping.location = (-300, 0)
tex_coord.location = (-500, 0)
Setup texture

tex_image.image = image
tex_image.projection = 'FLAT'
Connect nodes

links.new(tex_coord.outputs['UV'], mapping.inputs['Vector'])
links.new(mapping.outputs['Vector'], tex_image.inputs['Vector'])

if '{shader_type}' == 'ShaderNodeEmission':
links.new(tex_image.outputs['Color'], shader.inputs['Color'])
shader.inputs['Strength'].default_value = 1.0
links.new(shader.outputs['Emission'], output.inputs['Surface'])
else:
links.new(tex_image.outputs['Color'], shader.inputs['Base Color'])
links.new(shader.outputs['BSDF'], output.inputs['Surface'])

print(f"Projection material '{{mat.name}}' created")
'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "material_name": material_name,
        "use_emission": use_emission,
        "blender_result": result
    }

async def _project_to_geometry(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Project an image onto existing 3D geometry using camera projection.
    
    Args:
        image_path: Path to image
        target_object: Object to project onto
        camera_name: Projection camera name
    """
    image_path = params.get("image_path", "")
    target_object = params.get("target_object", "")
    camera_name = params.get("camera_name", "Projection_Camera")
    
    # First create the material
    mat_result = await self._create_projection_material({
        "image_path": image_path,
        "material_name": f"{target_object}_Projection"
    })
    
    # Then setup the projection
    proj_result = await self._setup_camera_projection({
        "image_path": image_path,
        "camera_name": camera_name,
        "target_object": target_object
    })
    
    # Apply material to object
    script = f'''

import bpy

target = bpy.data.objects.get("{target_object}")
mat = bpy.data.materials.get("{target_object}_Projection")

if target and mat:
if target.data.materials:
target.data.materials[0] = mat
else:
target.data.materials.append(mat)
print(f"Applied projection material to {{target.name}}")
else:
print("Target object or material not found")
'''

text

    apply_result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "target_object": target_object,
        "material_result": mat_result,
        "projection_result": proj_result,
        "apply_result": apply_result
    }

async def _create_parallax_scene(self, params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a complete parallax scene from image + depth map.
    
    Args:
        color_image: Path to color image
        depth_image: Path to depth map
        layers: Number of parallax layers (default: 5)
        depth_range: Total depth range (default: 50)
    """
    color_image = params.get("color_image", "")
    depth_image = params.get("depth_image", "")
    layers = params.get("layers", 5)
    depth_range = params.get("depth_range", 50)
    
    if not color_image:
        return {"status": "error", "message": "color_image is required"}
    
    color_escaped = color_image.replace("\\", "\\\\")
    depth_escaped = depth_image.replace("\\", "\\\\") if depth_image else ""
    
    script = f'''

import bpy
import os

color_path = r"{color_escaped}"
depth_path = r"{depth_escaped}"

if not os.path.exists(color_path):
raise FileNotFoundError(f"Color image not found: {{color_path}}")
Load images

color_img = bpy.data.images.load(color_path)
depth_img = None
if depth_path and os.path.exists(depth_path):
depth_img = bpy.data.images.load(depth_path)
depth_img.colorspace_settings.name = 'Non-Color'

img_width, img_height = color_img.size
aspect = img_width / img_height
Create parallax collection

parallax_coll = bpy.data.collections.new("Parallax_Scene")
bpy.context.scene.collection.children.link(parallax_coll)
Create layers at different depths

layers = {layers}
depth_range = {depth_range}
layer_spacing = depth_range / layers

for i in range(layers):
depth = 20 + (i * layer_spacing)

text

# Create plane
bpy.ops.mesh.primitive_plane_add(size=1, location=(0, depth, 0))
plane = bpy.context.active_object
plane.name = f"Parallax_Layer_{{i}}"

# Scale to match image aspect
plane.scale.x = depth * aspect * 0.5
plane.scale.z = depth * 0.5
bpy.ops.object.transform_apply(scale=True)

# Rotate to face camera
plane.rotation_euler.x = 1.5708

# Create material
mat = bpy.data.materials.new(name=f"Parallax_Mat_{{i}}")
mat.use_nodes = True
mat.blend_method = 'BLEND'

nodes = mat.node_tree.nodes
links = mat.node_tree.links
nodes.clear()

output = nodes.new('ShaderNodeOutputMaterial')
principled = nodes.new('ShaderNodeBsdfPrincipled')
tex = nodes.new('ShaderNodeTexImage')

tex.image = color_img
links.new(tex.outputs['Color'], principled.inputs['Base Color'])
links.new(tex.outputs['Alpha'], principled.inputs['Alpha'])
links.new(principled.outputs['BSDF'], output.inputs['Surface'])

plane.data.materials.append(mat)

# Move to collection
parallax_coll.objects.link(plane)
bpy.context.scene.collection.objects.unlink(plane)

Create camera

bpy.ops.object.camera_add(location=(0, 0, 2))
camera = bpy.context.active_object
camera.name = "Parallax_Camera"
bpy.context.scene.camera = camera

print(f"Created parallax scene with {{layers}} layers")
'''

text

    result = await self.use_tool(
        "blender", "python_scripter", "execute_script",
        script_content=script
    )
    
    return {
        "status": "success",
        "layers": layers,
        "depth_range": depth_range,
        "blender_result": result
    }

def get_tools(self) -> List[Dict[str, Any]]:
    """Return MCP tool definitions for this agent."""
    return [
        {
            "name": "generate_matte_painting",
            "description": "Generate a matte painting using Z-Image AI",
            "parameters": {
                "prompt": {"type": "string", "required": True},
                "style": {"type": "string", "enum": ["cinematic", "fantasy", "scifi", "realistic"]},
                "width": {"type": "integer", "default": 1920},
                "height": {"type": "integer", "default": 1080}
            }
        },
        {
            "name": "setup_camera_projection",
            "description": "Setup camera projection for an image",
            "parameters": {
                "image_path": {"type": "string", "required": True},
                "camera_name": {"type": "string", "default": "Projection_Camera"},
                "target_object": {"type": "string"}
            }
        },
        {
            "name": "create_parallax_scene",
            "description": "Create parallax scene from image and depth",
            "parameters": {
                "color_image": {"type": "string", "required": True},
                "depth_image": {"type": "string"},
                "layers": {"type": "integer", "default": 5},
                "depth_range": {"type": "number", "default": 50}
            }
        }
    ]

Bash

pip install python-dotenv

    Use in your code:

Python

    from config.environment import EnvironmentConfig

    # Access configuration
    db_url = EnvironmentConfig.DATABASE_URL
    blender_path = EnvironmentConfig.BLENDER_PATH

Configuration Variables
Project Paths

    PROJECT_ROOT - Main project directory
    AGENCIES_ROOT - Agencies directory
    WORKFLOWS_DIR - Workflows directory
    SCRIPTS_DIR - Scripts directory

Database

    DATABASE_URL - Full PostgreSQL connection string
    DATABASE_NAME - Database name (default: mama_ai)
    DATABASE_HOST - Database host (default: localhost)
    DATABASE_PORT - Database port (default: 5432)

Blender

    BLENDER_VERSION - Target Blender version (default: 5.0)
    BLENDER_PATH - Path to Blender executable

API Keys

    DEEPSEEK_API_KEY - DeepSeek API key
    OPENAI_API_KEY - OpenAI API key
    SERPER_API_KEY - Serper API key

MCP Server Ports

    MCP_BLENDER_PORT - 8003
    MCP_SOFTWARE_PORT - 8080
    MCP_CONTENT_PORT - 8021
    MCP_RESEARCH_PORT - 8022
    MCP_MARKETING_PORT - 8023
    MCP_VFX_PORT - 8026
    MCP_CREATIVE_PORT - 8027

claude-opus-4-5-20251101-thinking-32k
Complete Setup for Your Specific Locations

I'll create a ready-to-use configuration with all your specific paths and LM Arena URLs.
1. Your Complete .env File

Bash

# .env
# ============================================
# PROJECT RECOVERY SYSTEM - YOUR CONFIGURATION
# ============================================

# ============================================
# GITHUB
# ============================================
# Get token from: https://github.com/settings/tokens
# Required scopes: repo, gist, read:user
GITHUB_TOKEN=ghp_YOUR_TOKEN_HERE
GITHUB_USERNAME=YOUR_GITHUB_USERNAME

# ============================================
# YOUR SYSTEM INFO
# ============================================
WINDOWS_USERNAME=eguid
LINUX_USERNAME=eguid

# ============================================
# ARGILLA (Data Labeling)
# ============================================
ARGILLA_API_URL=http://localhost:6900
ARGILLA_API_KEY=admin.apikey
ARGILLA_WORKSPACE=project_recovery

# ============================================
# DATABASE
# ============================================
DATABASE_URL=postgresql://recovery:recovery_pass@localhost:5432/project_recovery
POSTGRES_USER=recovery
POSTGRES_PASSWORD=recovery_pass
POSTGRES_DB=project_recovery

# ============================================
# VECTOR STORE
# ============================================
QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION=project_fragments

# ============================================
# REDIS
# ============================================
REDIS_URL=redis://localhost:6379

# ============================================
# PROCESSING
# ============================================
EMBEDDING_MODEL=all-MiniLM-L6-v2
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
SCRAPE_INTERVAL_HOURS=6
LOG_LEVEL=INFO

2. Your Specific Sources Configuration

YAML

# config/sources.yaml
# ============================================
# YOUR PROJECT RECOVERY SOURCES
# ============================================

project_info:
  name: "Eguid Project Recovery"
  description: "Recovering lost project data from multiple locations"
  owner: "eguid"

# Keywords to identify YOUR project files
project_keywords:
  - "eguid"
  # Add your project-specific keywords here:
  # - "your_project_name"
  # - "your_function_names"
  # - "unique_identifiers"

file_signatures: []
  # Add unique patterns from your code:
  # - pattern: "# Copyright eguid"
  #   type: source_code
  #   weight: 2.0

# ============================================
# SOURCES
# ============================================

sources:
  # ------------------------------------------
  # 1. LM ARENA CHAT LOGS
  # ------------------------------------------
  lmarena_chatlogs:
    enabled: true
    
    # Your specific chat URLs
    chat_urls:
      - "https://lmarena.ai/c/019b364c-8fbd-722b-949d-9bb5c17a516f"
      - "https://lmarena.ai/c/019b352d-09a8-78de-9002-5d11440aac80"
      - "https://lmarena.ai/c/019b352a-e9b8-7a99-8d3b-f7cfe5a7946e"
      - "https://lmarena.ai/c/019b3529-b512-701d-a054-bd7d1e4e6917"
      - "https://lmarena.ai/c/019b1ef3-a33d-7722-a2ea-c406c8d0a4d5"
      - "https://lmarena.ai/c/019b0a05-e1e5-7764-a9ff-94e74c1826a3"
      - "https://lmarena.ai/c/019b15a6-06aa-7090-b65f-f98510c2ad01"
      - "https://lmarena.ai/c/019b0e15-dc4e-714d-ac7b-04f592f66f8c"
      - "https://lmarena.ai/c/019b0e13-edfa-7e43-b8dd-8aa28d0b3eb3"
      - "https://lmarena.ai/c/019b0e3a-1787-7506-81cd-99d376b57b62"
      - "https://lmarena.ai/c/019b0c74-9fbf-7c68-9521-aa4c67eb165b"
    
    # Browser data paths for additional chat discovery
    browser_data_paths:
      - "C:/Users/eguid/AppData/Local/Google/Chrome/User Data/Default"
      - "C:/Users/eguid/AppData/Local/Microsoft/Edge/User Data/Default"
      - "C:/Users/eguid/AppData/Roaming/Mozilla/Firefox/Profiles"
    
    # Where you might have exported chats
    exported_chats_paths:
      - "C:/Users/eguid/Downloads"
      - "C:/Users/eguid/Documents"
      - "C:/Users/eguid/OneDrive/Desktop"
      - "G:/restored"
    
    chat_patterns:
      - "*lmarena*"
      - "*chat*.json"
      - "*conversation*.json"
      - "*arena*"
      - "*.md"

  # ------------------------------------------
  # 2. WSL (Windows Subsystem for Linux)
  # ------------------------------------------
  wsl_system:
    enabled: true
    
    # WSL paths
    paths:
      - "\\\\wsl.localhost\\Ubuntu\\home"
      - "\\\\wsl.localhost\\Ubuntu\\home\\eguid"
      - "\\\\wsl.localhost\\Ubuntu\\home\\eguid\\projects"
      - "\\\\wsl.localhost\\Ubuntu\\home\\eguid\\code"
      - "\\\\wsl.localhost\\Ubuntu\\home\\eguid\\Documents"
      - "\\\\wsl.localhost\\Ubuntu\\home\\eguid\\.config"
      # Alternative WSL path format
      - "\\\\wsl$\\Ubuntu\\home"
      - "\\\\wsl$\\Ubuntu\\home\\eguid"
      
    # Also check for other distros
    check_distros:
      - "Ubuntu"
      - "Ubuntu-22.04"
      - "Ubuntu-20.04"
      - "Debian"
      - "kali-linux"
      
    include_patterns:
      - "*.py"
      - "*.r"
      - "*.R"
      - "*.Rmd"
      - "*.js"
      - "*.ts"
      - "*.jsx"
      - "*.tsx"
      - "*.go"
      - "*.rs"
      - "*.java"
      - "*.cpp"
      - "*.c"
      - "*.h"
      - "*.sh"
      - "*.bash"
      - "*.zsh"
      - "*.md"
      - "*.txt"
      - "*.json"
      - "*.yaml"
      - "*.yml"
      - "*.toml"
      - "*.sql"
      - "*.html"
      - "*.css"
      - "*.xml"
      - "*.ipynb"
      - "Dockerfile"
      - "docker-compose*.yml"
      - "Makefile"
      - "*.env"
      - ".bashrc"
      - ".zshrc"
      - ".gitconfig"
      - "requirements.txt"
      - "package.json"
      
    exclude_patterns:
      - "node_modules/*"
      - "__pycache__/*"
      - ".git/objects/*"
      - "venv/*"
      - ".venv/*"
      - ".cache/*"
      - "*.pyc"

  # ------------------------------------------
  # 3. RESTORED DATA (G: Drive)
  # ------------------------------------------
  restored_drive:
    enabled: true
    
    paths:
      - "G:/restored"
      - "G:/"
      
    deep_scan: true
    
    include_patterns:
      - "*.py"
      - "*.r"
      - "*.R"
      - "*.Rmd"
      - "*.rmd"
      - "*.Rproj"
      - "*.RData"
      - "*.rda"
      - "*.rds"
      - "*.js"
      - "*.ts"
      - "*.jsx"
      - "*.tsx"
      - "*.json"
      - "*.yaml"
      - "*.yml"
      - "*.md"
      - "*.txt"
      - "*.sql"
      - "*.html"
      - "*.css"
      - "*.sh"
      - "*.ipynb"
      - "*.csv"
      - "*.xml"
      - "*.toml"
      - "Dockerfile"
      - "docker-compose*.yml"
      - "Makefile"
      - "requirements.txt"
      - "package.json"
      - "*.env"
      - "*.config"
      - "*.conf"
      
    exclude_patterns:
      - "$RECYCLE.BIN/*"
      - "System Volume Information/*"
      - "*.tmp"
      - "*.log"
      - "node_modules/*"
      - "__pycache__/*"

  # ------------------------------------------
  # 4. ONEDRIVE LOCATIONS
  # ------------------------------------------
  onedrive:
    enabled: true
    
    paths:
      # Personal Vault - might need special handling
      - "C:/Users/eguid/OneDrive/Personal Vault"
      
      # AppData in OneDrive
      - "C:/Users/eguid/OneDrive/AppData"
      
      # Desktop synced to OneDrive
      - "C:/Users/eguid/OneDrive/Desktop"
      
      # Drivers and apps folder
      - "C:/Users/eguid/OneDrive/drivers and apps"
      
      # Pictures
      - "C:/Users/eguid/OneDrive/Pictures"
      
      # Also check main OneDrive folder
      - "C:/Users/eguid/OneDrive"
      - "C:/Users/eguid/OneDrive/Documents"
      
    include_patterns:
      - "*.py"
      - "*.r"
      - "*.R"
      - "*.Rmd"
      - "*.js"
      - "*.ts"
      - "*.json"
      - "*.yaml"
      - "*.yml"
      - "*.md"
      - "*.txt"
      - "*.sql"
      - "*.html"
      - "*.css"
      - "*.sh"
      - "*.ipynb"
      - "*.csv"
      - "*.xml"
      - "*.docx"
      - "*.xlsx"
      - "*.pdf"
      - "*.zip"
      - "*.7z"
      - "*.rar"
      - "*.png"
      - "*.jpg"
      - "*.jpeg"
      - "*.gif"
      - "*.svg"
      - "Dockerfile"
      - "requirements.txt"
      - "package.json"
      
    exclude_patterns:
      - "*.tmp"
      - "~$*"
      - ".~*"
      
    # Special handling for screenshots that might contain code
    scan_images_for_text: false

  # ------------------------------------------
  # 5. LOCAL USER FOLDERS
  # ------------------------------------------
  local_user:
    enabled: true
    
    paths:
      - "C:/Users/eguid/Documents"
      - "C:/Users/eguid/Desktop"
      - "C:/Users/eguid/Downloads"
      - "C:/Users/eguid/Projects"
      - "C:/Users/eguid/Code"
      - "C:/Users/eguid/dev"
      - "C:/Users/eguid/workspace"
      - "C:/Users/eguid/repos"
      - "C:/Users/eguid/git"
      - "C:/Users/eguid/.config"
      - "C:/Users/eguid/AppData/Roaming/Code/User"
      
    include_patterns:
      - "*.py"
      - "*.r"
      - "*.R"
      - "*.Rmd"
      - "*.js"
      - "*.ts"
      - "*.json"
      - "*.yaml"
      - "*.yml"
      - "*.md"
      - "*.txt"
      - "*.sql"
      - "*.sh"
      - "*.ipynb"
      - "Dockerfile"
      - "requirements.txt"
      - "package.json"
      
    exclude_patterns:
      - "node_modules/*"
      - "__pycache__/*"
      - "venv/*"
      - ".venv/*"
      - "AppData/Local/Temp/*"

  # ------------------------------------------
  # 6. GITHUB (Optional - enable if needed)
  # ------------------------------------------
  github:
    enabled: false  # Set to true and add your username
    
    # repositories:
    #   - owner: "YOUR_GITHUB_USERNAME"
    #     repo: "repo-name"
    
    include_gists: true
    include_forks: true

3. Complete LM Arena Scraper with URL Fetching

Python

# scrapers/lmarena_scraper.py
"""
LM Arena Chat Logs Scraper
Fetches chat logs from LM Arena URLs and browser storage
"""
import asyncio
import aiohttp
import aiofiles
import json
import os
import re
import sqlite3
import shutil
import tempfile
from pathlib import Path
from datetime import datetime
from typing import AsyncIterator, Dict, Any, List, Optional, Set
from dataclasses import dataclass
from urllib.parse import urlparse

from .base import BaseScraper, ScrapedItem, SourceType, ContentType


@dataclass
class ChatMessage:
    role: str
    content: str
    model: Optional[str] = None
    timestamp: Optional[str] = None


@dataclass
class ChatConversation:
    id: str
    url: str
    messages: List[ChatMessage]
    metadata: Dict[str, Any]


class LMArenaScraperError(Exception):
    """Custom exception for LM Arena scraper errors"""
    pass


class LMArenaScraper(BaseScraper):
    """
    Comprehensive scraper for LM Arena chat logs.
    
    Sources:
    1. Direct URL fetching (if accessible)
    2. Browser local storage
    3. Browser history
    4. Exported chat files
    5. Browser cache
    """
    
    # Your specific chat URLs
    CHAT_URLS = [
        "https://lmarena.ai/c/019b364c-8fbd-722b-949d-9bb5c17a516f",
        "https://lmarena.ai/c/019b352d-09a8-78de-9002-5d11440aac80",
        "https://lmarena.ai/c/019b352a-e9b8-7a99-8d3b-f7cfe5a7946e",
        "https://lmarena.ai/c/019b3529-b512-701d-a054-bd7d1e4e6917",
        "https://lmarena.ai/c/019b1ef3-a33d-7722-a2ea-c406c8d0a4d5",
        "https://lmarena.ai/c/019b0a05-e1e5-7764-a9ff-94e74c1826a3",
        "https://lmarena.ai/c/019b15a6-06aa-7090-b65f-f98510c2ad01",
        "https://lmarena.ai/c/019b0e15-dc4e-714d-ac7b-04f592f66f8c",
        "https://lmarena.ai/c/019b0e13-edfa-7e43-b8dd-8aa28d0b3eb3",
        "https://lmarena.ai/c/019b0e3a-1787-7506-81cd-99d376b57b62",
        "https://lmarena.ai/c/019b0c74-9fbf-7c68-9521-aa4c67eb165b",
    ]
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.username = config.get("windows_username", os.environ.get("USERNAME", "eguid"))
        self.processed_ids: Set[str] = set()
        
    @property
    def source_type(self) -> SourceType:
        return SourceType.LOCAL_FILESYSTEM
    
    async def validate_connection(self) -> bool:
        return True
    
    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        """Main scraping method"""
        config = self.config.get("sources", {}).get("lmarena_chatlogs", {})
        
        if not config.get("enabled", True):
            return
        
        print("[LMArena] Starting LM Arena chat log scraping...")
        
        # 1. Try to fetch from URLs directly
        chat_urls = config.get("chat_urls", []) + self.CHAT_URLS
        chat_urls = list(set(chat_urls))  # Remove duplicates
        
        print(f"[LMArena] Processing {len(chat_urls)} chat URLs...")
        async for item in self._fetch_chat_urls(chat_urls):
            yield item
        
        # 2. Scan browser data
        browser_paths = config.get("browser_data_paths", [
            f"C:/Users/{self.username}/AppData/Local/Google/Chrome/User Data/Default",
            f"C:/Users/{self.username}/AppData/Local/Microsoft/Edge/User Data/Default",
            f"C:/Users/{self.username}/AppData/Roaming/Mozilla/Firefox/Profiles",
        ])
        
        print("[LMArena] Scanning browser data...")
        for browser_path in browser_paths:
            if Path(browser_path).exists():
                async for item in self._scan_browser_data(Path(browser_path)):
                    yield item
        
        # 3. Scan exported chat files
        export_paths = config.get("exported_chats_paths", [
            f"C:/Users/{self.username}/Downloads",
            f"C:/Users/{self.username}/Documents",
            f"C:/Users/{self.username}/OneDrive/Desktop",
            "G:/restored",
        ])
        
        print("[LMArena] Scanning for exported chats...")
        for export_path in export_paths:
            if Path(export_path).exists():
                async for item in self._scan_exported_chats(Path(export_path)):
                    yield item
        
        # 4. Scan browser history for more URLs
        print("[LMArena] Scanning browser history...")
        async for item in self._scan_browser_history():
            yield item
        
        print(f"[LMArena] Completed. Processed {len(self.processed_ids)} unique chats.")
    
    async def _fetch_chat_urls(self, urls: List[str]) -> AsyncIterator[ScrapedItem]:
        """
        Attempt to fetch chat content from URLs.
        Note: LM Arena may require authentication or might not expose raw chat data.
        We'll try multiple approaches.
        """
        async with aiohttp.ClientSession() as session:
            for url in urls:
                chat_id = self._extract_chat_id(url)
                
                if chat_id in self.processed_ids:
                    continue
                
                print(f"[LMArena] Processing chat: {chat_id}")
                
                # Try different API endpoints
                api_endpoints = [
                    f"https://lmarena.ai/api/conversation/{chat_id}",
                    f"https://lmarena.ai/api/chat/{chat_id}",
                    f"https://arena.lmsys.org/api/conversation/{chat_id}",
                ]
                
                chat_data = None
                
                for endpoint in api_endpoints:
                    try:
                        async with session.get(endpoint, timeout=10) as response:
                            if response.status == 200:
                                chat_data = await response.json()
                                break
                    except Exception as e:
                        continue
                
                if chat_data:
                    # Successfully fetched from API
                    item = await self._process_chat_data(chat_id, url, chat_data)
                    if item:
                        self.processed_ids.add(chat_id)
                        yield item
                else:
                    # Create a reference item even if we can't fetch content
                    yield ScrapedItem(
                        id=f"lmarena:url:{chat_id}",
                        source_type=self.source_type,
                        source_path=url,
                        content=f"""# LM Arena Chat Reference
                        
**Chat ID:** {chat_id}
**URL:** {url}

*Unable to fetch content directly. Please open the URL in your browser and export the chat manually.*

## Manual Export Instructions:
1. Open the URL: {url}
2. If logged in, the chat should be visible
3. Copy the conversation content
4. Save as a .md or .json file in your Downloads folder
5. Re-run this scraper to capture the content
""",
                        content_type=ContentType.DATA,
                        filename=f"lmarena_chat_{chat_id}.md",
                        metadata={
                            "source": "lmarena_url",
                            "chat_id": chat_id,
                            "url": url,
                            "status": "reference_only",
                            "needs_manual_export": True
                        },
                        confidence_score=0.5
                    )
                    self.processed_ids.add(chat_id)
                
                await asyncio.sleep(0.5)  # Rate limiting
    
    def _extract_chat_id(self, url: str) -> str:
        """Extract chat ID from URL"""
        # URL format: https://lmarena.ai/c/019b364c-8fbd-722b-949d-9bb5c17a516f
        match = re.search(r'/c/([a-f0-9-]+)', url)
        if match:
            return match.group(1)
        return url.split('/')[-1]
    
    async def _process_chat_data(
        self, 
        chat_id: str, 
        url: str, 
        data: Dict[str, Any]
    ) -> Optional[ScrapedItem]:
        """Process fetched chat data into a ScrapedItem"""
        try:
            # Format the chat content
            content = self._format_chat_content(data)
            
            # Extract code blocks
            code_blocks = self._extract_code_blocks(content)
            
            return ScrapedItem(
                id=f"lmarena:chat:{chat_id}",
                source_type=self.source_type,
                source_path=url,
                content=content,
                content_type=ContentType.DATA,
                filename=f"lmarena_chat_{chat_id}.md",
                metadata={
                    "source": "lmarena_api",
                    "chat_id": chat_id,
                    "url": url,
                    "has_code_blocks": len(code_blocks) > 0,
                    "code_block_count": len(code_blocks),
                    "code_languages": list(set(cb.get('language', 'unknown') for cb in code_blocks)),
                    "raw_data": data
                },
                confidence_score=1.0
            )
        except Exception as e:
            print(f"[LMArena] Error processing chat {chat_id}: {e}")
            return None
    
    def _format_chat_content(self, data: Dict[str, Any]) -> str:
        """Format chat data into readable markdown"""
        lines = [f"# LM Arena Conversation\n"]
        
        # Handle different data structures
        messages = data.get('messages', data.get('conversation', data.get('chat', [])))
        
        if isinstance(messages, list):
            for msg in messages:
                if isinstance(msg, dict):
                    role = msg.get('role', msg.get('sender', 'unknown')).upper()
                    content = msg.get('content', msg.get('message', msg.get('text', '')))
                    model = msg.get('model', '')
                    
                    if model:
                        lines.append(f"\n## {role} ({model})\n")
                    else:
                        lines.append(f"\n## {role}\n")
                    
                    lines.append(content)
                    lines.append("\n")
                elif isinstance(msg, str):
                    lines.append(msg)
                    lines.append("\n")
        elif isinstance(messages, str):
            lines.append(messages)
        
        # Add metadata if available
        if 'created_at' in data:
            lines.append(f"\n---\n*Created: {data['created_at']}*\n")
        
        return '\n'.join(lines)
    
    def _extract_code_blocks(self, content: str) -> List[Dict[str, Any]]:
        """Extract code blocks from content"""
        blocks = []
        
        # Match markdown code blocks
        pattern = r'```(\w*)\n(.*?)```'
        matches = re.findall(pattern, content, re.DOTALL)
        
        lang_to_ext = {
            'python': 'py', 'py': 'py',
            'javascript': 'js', 'js': 'js',
            'typescript': 'ts', 'ts': 'ts',
            'java': 'java',
            'cpp': 'cpp', 'c++': 'cpp',
            'c': 'c',
            'go': 'go', 'golang': 'go',
            'rust': 'rs', 'rs': 'rs',
            'ruby': 'rb', 'rb': 'rb',
            'r': 'R',
            'sql': 'sql',
            'bash': 'sh', 'shell': 'sh', 'sh': 'sh',
            'html': 'html',
            'css': 'css',
            'json': 'json',
            'yaml': 'yaml', 'yml': 'yaml',
            'xml': 'xml',
            'dockerfile': 'dockerfile',
            'makefile': 'makefile',
        }
        
        for lang, code in matches:
            lang = lang.lower().strip() if lang else 'text'
            blocks.append({
                'language': lang,
                'extension': lang_to_ext.get(lang, 'txt'),
                'code': code.strip()
            })
        
        return blocks
    
    async def _scan_browser_data(self, browser_path: Path) -> AsyncIterator[ScrapedItem]:
        """Scan browser local storage and IndexedDB for chat data"""
        try:
            # Look for Local Storage
            local_storage = browser_path / "Local Storage" / "leveldb"
            if local_storage.exists():
                async for item in self._scan_leveldb(local_storage, "local_storage"):
                    yield item
            
            # Look for IndexedDB
            indexeddb = browser_path / "IndexedDB"
            if indexeddb.exists():
                for idb_dir in indexeddb.iterdir():
                    if 'lmarena' in str(idb_dir).lower() or 'lmsys' in str(idb_dir).lower():
                        async for item in self._scan_indexeddb(idb_dir):
                            yield item
            
            # Look for Session Storage
            session_storage = browser_path / "Session Storage"
            if session_storage.exists():
                async for item in self._scan_leveldb(session_storage, "session_storage"):
                    yield item
            
            # Look for cache
            cache_path = browser_path / "Cache" / "Cache_Data"
            if cache_path.exists():
                async for item in self._scan_cache(cache_path):
                    yield item
                    
        except Exception as e:
            print(f"[LMArena] Error scanning browser data: {e}")
    
    async def _scan_leveldb(self, path: Path, storage_type: str) -> AsyncIterator[ScrapedItem]:
        """Scan LevelDB storage for LM Arena data"""
        try:
            # LevelDB files have .ldb extension
            for ldb_file in path.glob("*.ldb"):
                try:
                    async with aiofiles.open(ldb_file, 'rb') as f:
                        content = await f.read()
                    
                    # Look for LM Arena related content
                    content_str = content.decode('utf-8', errors='ignore')
                    
                    if any(term in content_str.lower() for term in ['lmarena', 'lmsys', 'arena', 'chatbot']):
                        # Try to extract useful data
                        yield ScrapedItem(
                            id=f"lmarena:browser:{storage_type}:{ldb_file.name}",
                            source_type=self.source_type,
                            source_path=str(ldb_file),
                            content=content_str[:50000],  # Limit size
                            content_type=ContentType.DATA,
                            filename=f"browser_{storage_type}_{ldb_file.name}.txt",
                            metadata={
                                "source": f"browser_{storage_type}",
                                "browser_path": str(path),
                                "file": str(ldb_file)
                            },
                            confidence_score=0.7
                        )
                except Exception as e:
                    continue
                    
        except Exception as e:
            print(f"[LMArena] Error scanning LevelDB: {e}")
    
    async def _scan_indexeddb(self, idb_path: Path) -> AsyncIterator[ScrapedItem]:
        """Scan IndexedDB for chat data"""
        try:
            for db_file in idb_path.rglob("*.sqlite"):
                try:
                    # Copy to temp file (might be locked)
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.sqlite') as tmp:
                        tmp_path = tmp.name
                    
                    shutil.copy2(db_file, tmp_path)
                    
                    conn = sqlite3.connect(tmp_path)
                    cursor = conn.cursor()
                    
                    # Get all tables
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                    tables = cursor.fetchall()
                    
                    for (table_name,) in tables:
                        try:
                            cursor.execute(f"SELECT * FROM {table_name}")
                            rows = cursor.fetchall()
                            
                            if rows:
                                content = json.dumps(rows, indent=2, default=str)
                                
                                if any(term in content.lower() for term in ['message', 'chat', 'conversation']):
                                    yield ScrapedItem(
                                        id=f"lmarena:idb:{table_name}:{db_file.name}",
                                        source_type=self.source_type,
                                        source_path=str(db_file),
                                        content=content[:50000],
                                        content_type=ContentType.DATA,
                                        filename=f"indexeddb_{table_name}.json",
                                        metadata={
                                            "source": "browser_indexeddb",
                                            "table": table_name,
                                            "row_count": len(rows)
                                        },
                                        confidence_score=0.8
                                    )
                        except:
                            continue
                    
                    conn.close()
                    os.unlink(tmp_path)
                    
                except Exception as e:
                    continue
                    
        except Exception as e:
            print(f"[LMArena] Error scanning IndexedDB: {e}")
    
    async def _scan_cache(self, cache_path: Path) -> AsyncIterator[ScrapedItem]:
        """Scan browser cache for LM Arena API responses"""
        try:
            for cache_file in cache_path.glob("*"):
                if cache_file.is_file():
                    try:
                        async with aiofiles.open(cache_file, 'rb') as f:
                            content = await f.read()
                        
                        content_str = content.decode('utf-8', errors='ignore')
                        
                        # Look for API responses containing chat data
                        if 'lmarena' in content_str.lower() and any(
                            term in content_str.lower() 
                            for term in ['message', 'conversation', 'chat', 'content']
                        ):
                            # Try to extract JSON
                            json_match = re.search(r'\{.*"messages".*\}', content_str, re.DOTALL)
                            if json_match:
                                try:
                                    data = json.loads(json_match.group())
                                    formatted = self._format_chat_content(data)
                                    
                                    yield ScrapedItem(
                                        id=f"lmarena:cache:{cache_file.name}",
                                        source_type=self.source_type,
                                        source_path=str(cache_file),
                                        content=formatted,
                                        content_type=ContentType.DATA,
                                        filename=f"cached_chat_{cache_file.name[:16]}.md",
                                        metadata={
                                            "source": "browser_cache",
                                            "cache_file": str(cache_file)
                                        },
                                        confidence_score=0.9
                                    )
                                except json.JSONDecodeError:
                                    pass
                    except:
                        continue
                        
        except Exception as e:
            print(f"[LMArena] Error scanning cache: {e}")
    
    async def _scan_exported_chats(self, export_path: Path) -> AsyncIterator[ScrapedItem]:
        """Scan for exported chat files"""
        patterns = [
            "*lmarena*",
            "*chat*.json",
            "*conversation*.json",
            "*arena*",
            "*lmsys*",
        ]
        
        try:
            for root, dirs, files in os.walk(export_path):
                # Skip system directories
                dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__']]
                
                for filename in files:
                    filepath = Path(root) / filename
                    
                    # Check if matches patterns
                    matches = any(
                        filepath.match(p) for p in patterns
                    ) or any(
                        term in filename.lower() 
                        for term in ['lmarena', 'chat', 'conversation', 'arena', 'lmsys']
                    )
                    
                    if not matches:
                        continue
                    
                    # Skip large files
                    try:
                        if filepath.stat().st_size > 10 * 1024 * 1024:  # 10MB
                            continue
                    except:
                        continue
                    
                    try:
                        async with aiofiles.open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            content = await f.read()
                        
                        # Try to parse as JSON
                        try:
                            data = json.loads(content)
                            formatted = self._format_chat_content(data)
                            content = formatted
                        except json.JSONDecodeError:
                            pass
                        
                        # Extract code blocks
                        code_blocks = self._extract_code_blocks(content)
                        
                        yield ScrapedItem(
                            id=f"lmarena:export:{filepath.name}",
                            source_type=self.source_type,
                            source_path=str(filepath),
                            content=content,
                            content_type=ContentType.DATA,
                            filename=filepath.name,
                            metadata={
                                "source": "exported_file",
                                "original_path": str(filepath),
                                "has_code_blocks": len(code_blocks) > 0,
                                "code_block_count": len(code_blocks)
                            },
                            confidence_score=0.95
                        )
                        
                        # Also yield individual code blocks
                        for i, block in enumerate(code_blocks):
                            yield ScrapedItem(
                                id=f"lmarena:code:{filepath.stem}:{i}",
                                source_type=self.source_type,
                                source_path=f"{filepath}#code-block-{i}",
                                content=block['code'],
                                content_type=ContentType.SOURCE_CODE,
                                filename=f"{filepath.stem}_code_{i}.{block['extension']}",
                                metadata={
                                    "source": "chat_code_block",
                                    "original_file": str(filepath),
                                    "block_index": i,
                                    "language": block.get('language')
                                },
                                language=block.get('language'),
                                confidence_score=1.0
                            )
                            
                    except Exception as e:
                        continue
                        
        except Exception as e:
            print(f"[LMArena] Error scanning exports: {e}")
    
    async def _scan_browser_history(self) -> AsyncIterator[ScrapedItem]:
        """Scan browser history for additional LM Arena URLs"""
        history_paths = {
            'chrome': Path(f"C:/Users/{self.username}/AppData/Local/Google/Chrome/User Data/Default/History"),
            'edge': Path(f"C:/Users/{self.username}/AppData/Local/Microsoft/Edge/User Data/Default/History"),
        }
        
        found_urls = []
        
        for browser, history_path in history_paths.items():
            if not history_path.exists():
                continue
            
            try:
                # Copy to temp file (database might be locked)
                with tempfile.NamedTemporaryFile(delete=False, suffix='.db') as tmp:
                    tmp_path = tmp.name
                
                shutil.copy2(history_path, tmp_path)
                
                conn = sqlite3.connect(tmp_path)
                cursor = conn.cursor()
                
                cursor.execute("""
                    SELECT url, title, last_visit_time 
                    FROM urls 
                    WHERE url LIKE '%lmarena%' OR url LIKE '%lmsys%' OR url LIKE '%arena%'
                    ORDER BY last_visit_time DESC
                """)
                
                urls = cursor.fetchall()
                conn.close()
                os.unlink(tmp_path)
                
                for url, title, visit_time in urls:
                    if '/c/' in url:  # Chat URL
                        chat_id = self._extract_chat_id(url)
                        if chat_id not in self.processed_ids:
                            found_urls.append({
                                'url': url,
                                'title': title,
                                'browser': browser
                            })
                            
            except Exception as e:
                print(f"[LMArena] Error scanning {browser} history: {e}")
        
        # Process found URLs
        if found_urls:
            print(f"[LMArena] Found {len(found_urls)} additional URLs from browser history")
            
            # Create a summary of found URLs
            url_list = "\n".join([f"- [{u['title'] or 'Chat'}]({u['url']})" for u in found_urls])
            
            yield ScrapedItem(
                id="lmarena:history:discovered_urls",
                source_type=self.source_type,
                source_path="browser:history",
                content=f"""# Discovered LM Arena Chats from Browser History

{url_list}

---
*These URLs were discovered in your browser history. They may contain additional project-related conversations.*
""",
                content_type=ContentType.DATA,
                filename="discovered_lmarena_urls.md",
                metadata={
                    "source": "browser_history",
                    "url_count": len(found_urls),
                    "urls": [u['url'] for u in found_urls]
                },
                confidence_score=0.8
            )
            
            # Also try to fetch each URL
            async for item in self._fetch_chat_urls([u['url'] for u in found_urls]):
                yield item

4. WSL/Linux Scraper for Your Paths

Python

# scrapers/wsl_scraper.py
"""
WSL (Windows Subsystem for Linux) Scraper
"""
import asyncio
import aiofiles
import os
import subprocess
from pathlib import Path, PureWindowsPath
from datetime import datetime
from typing import AsyncIterator, Dict, Any, List, Set
from .base import BaseScraper, ScrapedItem, SourceType, ContentType


class WSLScraper(BaseScraper):
    """Scraper for WSL filesystems"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.username = config.get("linux_username", "eguid")
        self.scanned_paths: Set[str] = set()
        
    @property
    def source_type(self) -> SourceType:
        return SourceType.LOCAL_FILESYSTEM
    
    async def validate_connection(self) -> bool:
        """Check if WSL is available"""
        try:
            result = subprocess.run(
                ['wsl', '--list', '--quiet'],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0 and bool(result.stdout.strip())
        except Exception:
            return False
    
    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        """Scrape WSL filesystem"""
        config = self.config.get("sources", {}).get("wsl_system", {})
        
        if not config.get("enabled", True):
            return
        
        print("[WSL] Starting WSL filesystem scan...")
        
        # Get available distros
        distros = await self._get_distros()
        print(f"[WSL] Found distros: {distros}")
        
        # Configured distros to check
        check_distros = config.get("check_distros", ["Ubuntu", "Ubuntu-22.04", "Ubuntu-20.04", "Debian"])
        
        for distro in distros:
            if distro not in check_distros and not any(d in distro for d in check_distros):
                continue
            
            print(f"[WSL] Scanning distro: {distro}")
            
            # Try different path formats
            wsl_bases = [
                f"\\\\wsl.localhost\\{distro}",
                f"\\\\wsl$\\{distro}",
            ]
            
            for wsl_base in wsl_bases:
                base_path = Path(wsl_base)
                
                if not base_path.exists():
                    continue
                
                # Paths to scan
                scan_paths = [
                    base_path / "home",
                    base_path / "home" / self.username,
                    base_path / "home" / self.username / "projects",
                    base_path / "home" / self.username / "code",
                    base_path / "home" / self.username / "Documents",
                    base_path / "home" / self.username / ".config",
                ]
                
                # Add configured paths
                for configured_path in config.get("paths", []):
                    p = Path(configured_path)
                    if p.exists():
                        scan_paths.append(p)
                
                for scan_path in scan_paths:
                    if scan_path.exists() and str(scan_path) not in self.scanned_paths:
                        self.scanned_paths.add(str(scan_path))
                        async for item in self._scan_directory(scan_path, config):
                            yield item
                
                break  # Found working path format
    
    async def _get_distros(self) -> List[str]:
        """Get list of installed WSL distros"""
        try:
            result = subprocess.run(
                ['wsl', '--list', '--quiet'],
                capture_output=True,
                text=True,
                timeout=10,
                encoding='utf-16-le'  # WSL uses UTF-16
            )
            
            if result.returncode == 0:
                # Clean up the output
                distros = []
                for line in result.stdout.strip().split('\n'):
                    line = line.strip().replace('\x00', '')
                    if line and line not in ['Windows Subsystem for Linux Distributions:']:
                        distros.append(line)
                return distros
        except Exception as e:
            print(f"[WSL] Error getting distros: {e}")
        
        return ["Ubuntu"]  # Default
    
    async def _scan_directory(
        self, 
        base_path: Path, 
        config: Dict
    ) -> AsyncIterator[ScrapedItem]:
        """Scan a directory recursively"""
        include_patterns = config.get("include_patterns", [
            "*.py", "*.r", "*.R", "*.Rmd", "*.js", "*.ts",
            "*.json", "*.yaml", "*.yml", "*.md", "*.sh",
            "*.sql", "*.html", "*.css", "Dockerfile",
            ".bashrc", ".zshrc", ".gitconfig"
        ])
        
        exclude_patterns = config.get("exclude_patterns", [
            "node_modules/*", "__pycache__/*", ".git/objects/*",
            "venv/*", ".venv/*", ".cache/*"
        ])
        
        exclude_dirs = {
            'node_modules', '__pycache__', '.git', '.cache',
            'venv', '.venv', '.local/share/Trash', 'snap'
        }
        
        try:
            for root, dirs, files in os.walk(base_path):
                # Filter directories
                dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.cache')]
                
                for filename in files:
                    filepath = Path(root) / filename
                    
                    # Check if matches patterns
                    matches = False
                    for pattern in include_patterns:
                        if pattern.startswith('.'):
                            if filename == pattern.lstrip('*.'):
                                matches = True
                                break
                        elif filepath.match(pattern):
                            matches = True
                            break
                        elif filename == pattern:
                            matches = True
                            break
                    
                    if not matches:
                        continue
                    
                    try:
                        item = await self._process_file(filepath)
                        if item:
                            yield item
                    except Exception as e:
                        pass
                
                await asyncio.sleep(0)  # Yield control
                
        except PermissionError:
            pass
        except Exception as e:
            print(f"[WSL] Error scanning {base_path}: {e}")
    
    async def _process_file(self, filepath: Path) -> ScrapedItem | None:
        """Process a single file"""
        try:
            stat = filepath.stat()
            
            # Skip large files
            if stat.st_size > 5 * 1024 * 1024:  # 5MB
                return None
            
            # Skip empty files
            if stat.st_size == 0:
                return None
            
            # Read file
            async with aiofiles.open(filepath, 'rb') as f:
                raw = await f.read()
            
            # Skip binary files
            if b'\x00' in raw[:4096]:
                return None
            
            try:
                content = raw.decode('utf-8')
            except UnicodeDecodeError:
                content = raw.decode('utf-8', errors='ignore')
            
            # Check relevance
            is_relevant, confidence = self.is_relevant(content, filepath.name)
            
            # WSL files might be valuable configs
            is_config = filepath.name.startswith('.') or filepath.name in [
                'Makefile', 'Dockerfile', 'docker-compose.yml'
            ]
            
            return ScrapedItem(
                id=f"wsl:{filepath.as_posix()}",
                source_type=self.source_type,
                source_path=str(filepath),
                content=content,
                content_type=ContentType.CONFIGURATION if is_config else self.detect_content_type(content, filepath.name),
                file_extension=filepath.suffix.lstrip('.') if filepath.suffix else None,
                filename=filepath.name,
                metadata={
                    "wsl_path": str(filepath),
                    "is_config_file": is_config,
                    "source": "wsl"
                },
                created_at=datetime.fromtimestamp(stat.st_ctime),
                modified_at=datetime.fromtimestamp(stat.st_mtime),
                language=self.detect_language(content, filepath.name),
                confidence_score=max(confidence, 0.3) if is_relevant or is_config else 0.2
            )
            
        except Exception as e:
            return None

5. OneDrive and Restored Drive Scraper

Python

# scrapers/onedrive_scraper.py
"""
OneDrive and Restored Drive Scraper
"""
import asyncio
import aiofiles
import os
import chardet
from pathlib import Path
from datetime import datetime
from typing import AsyncIterator, Dict, Any, List, Set
import zipfile
import py7zr
import rarfile
from .base import BaseScraper, ScrapedItem, SourceType, ContentType


class OneDriveRestoredScraper(BaseScraper):
    """
    Scraper for OneDrive folders and restored data
    Handles: Regular files, archives (zip, 7z, rar), and special folders
    """
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.username = config.get("windows_username", os.environ.get("USERNAME", "eguid"))
        self.scanned_paths: Set[str] = set()
        self.max_file_size = 10 * 1024 * 1024  # 10MB
        
    @property
    def source_type(self) -> SourceType:
        return SourceType.LOCAL_FILESYSTEM
    
    async def validate_connection(self) -> bool:
        return True
    
    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        """Scrape OneDrive and restored locations"""
        
        # 1. Scan OneDrive
        onedrive_config = self.config.get("sources", {}).get("onedrive", {})
        if onedrive_config.get("enabled", True):
            print("[OneDrive] Scanning OneDrive folders...")
            async for item in self._scan_onedrive(onedrive_config):
                yield item
        
        # 2. Scan Restored Drive
        restored_config = self.config.get("sources", {}).get("restored_drive", {})
        if restored_config.get("enabled", True):
            print("[Restored] Scanning restored drive...")
            async for item in self._scan_restored(restored_config):
                yield item
        
        # 3. Scan Local User folders
        local_config = self.config.get("sources", {}).get("local_user", {})
        if local_config.get("enabled", True):
            print("[Local] Scanning local user folders...")
            async for item in self._scan_local_user(local_config):
                yield item
    
    async def _scan_onedrive(self, config: Dict) -> AsyncIterator[ScrapedItem]:
        """Scan OneDrive folders"""
        paths = config.get("paths", [
            f"C:/Users/{self.username}/OneDrive/Personal Vault",
            f"C:/Users/{self.username}/OneDrive/AppData",
            f"C:/Users/{self.username}/OneDrive/Desktop",
            f"C:/Users/{self.username}/OneDrive/drivers and apps",
            f"C:/Users/{self.username}/OneDrive/Pictures",
            f"C:/Users/{self.username}/OneDrive",
            f"C:/Users/{self.username}/OneDrive/Documents",
        ])
        
        include_patterns = config.get("include_patterns", [
            "*.py", "*.r", "*.R", "*.Rmd", "*.js", "*.ts",
            "*.json", "*.yaml", "*.yml", "*.md", "*.txt",
            "*.sql", "*.html", "*.css", "*.sh", "*.ipynb",
            "*.csv", "*.xml", "*.docx", "*.xlsx", "*.pdf",
            "*.zip", "*.7z", "*.rar",
            "Dockerfile", "requirements.txt", "package.json"
        ])
        
        for path_str in paths:
            path = Path(path_str)
            
            if not path.exists():
                continue
            
            if str(path) in self.scanned_paths:
                continue
            
            self.scanned_paths.add(str(path))
            print(f"[OneDrive] Scanning: {path}")
            
            async for item in self._scan_directory(path, include_patterns, "onedrive"):
                yield item
    
    async def _scan_restored(self, config: Dict) -> AsyncIterator[ScrapedItem]:
        """Scan restored drive"""
        paths = config.get("paths", ["G:/restored", "G:/"])
        
        include_patterns = config.get("include_patterns", [
            "*.py", "*.r", "*.R", "*.Rmd", "*.js", "*.ts",
            "*.json", "*.yaml", "*.yml", "*.md", "*.txt",
            "*.sql", "*.html", "*.css", "*.sh", "*.ipynb",
            "*.csv", "*.xml", "*.toml",
            "Dockerfile", "docker-compose*.yml", "Makefile",
            "requirements.txt", "package.json", "*.env", "*.config"
        ])
        
        for path_str in paths:
            path = Path(path_str)
            
            if not path.exists():
                print(f"[Restored] Path not found: {path}")
                continue
            
            if str(path) in self.scanned_paths:
                continue
            
            self.scanned_paths.add(str(path))
            print(f"[Restored] Scanning: {path}")
            
            async for item in self._scan_directory(path, include_patterns, "restored"):
                yield item
    
    async def _scan_local_user(self, config: Dict) -> AsyncIterator[ScrapedItem]:
        """Scan local user folders"""
        paths = config.get("paths", [
            f"C:/Users/{self.username}/Documents",
            f"C:/Users/{self.username}/Desktop",
            f"C:/Users/{self.username}/Downloads",
            f"C:/Users/{self.username}/Projects",
            f"C:/Users/{self.username}/Code",
            f"C:/Users/{self.username}/dev",
            f"C:/Users/{self.username}/workspace",
            f"C:/Users/{self.username}/repos",
            f"C:/Users/{self.username}/git",
        ])
        
        include_patterns = config.get("include_patterns", [
            "*.py", "*.r", "*.R", "*.Rmd", "*.js", "*.ts",
            "*.json", "*.yaml", "*.yml", "*.md", "*.txt",
            "*.sql", "*.sh", "*.ipynb",
            "Dockerfile", "requirements.txt", "package.json"
        ])
        
        for path_str in paths:
            path = Path(path_str)
            
            if not path.exists():
                continue
            
            if str(path) in self.scanned_paths:
                continue
            
            self.scanned_paths.add(str(path))
            print(f"[Local] Scanning: {path}")
            
            async for item in self._scan_directory(path, include_patterns, "local"):
                yield item
    
    async def _scan_directory(
        self,
        base_path: Path,
        include_patterns: List[str],
        source_tag: str
    ) -> AsyncIterator[ScrapedItem]:
        """Recursively scan a directory"""
        exclude_dirs = {
            'node_modules', '__pycache__', '.git', '.svn',
            'venv', '.venv', 'env', '$RECYCLE.BIN',
            'System Volume Information', 'Windows',
            'Program Files', 'Program Files (x86)',
            'AppData', '.cache', 'cache', 'Cache'
        }
        
        try:
            for root, dirs, files in os.walk(base_path, followlinks=False):
                # Filter directories
                dirs[:] = [
                    d for d in dirs 
                    if d not in exclude_dirs 
                    and not d.startswith('.')
                    and not d.startswith('~')
                ]
                
                for filename in files:
                    filepath = Path(root) / filename
                    
                    # Skip temp files
                    if filename.startswith('~') or filename.startswith('.'):
                        continue
                    
                    # Check if matches patterns
                    matches = any(
                        filepath.match(p) or filename == p.lstrip('*.')
                        for p in include_patterns
                    )
                    
                    if not matches:
                        continue
                    
                    try:
                        # Handle archives
                        if filepath.suffix.lower() in ['.zip', '.7z', '.rar']:
                            async for item in self._extract_archive(filepath, source_tag):
                                yield item
                        else:
                            item = await self._process_file(filepath, source_tag)
                            if item:
                                yield item
                    except Exception as e:
                        pass
                
                await asyncio.sleep(0)  # Yield control
                
        except PermissionError:
            pass
        except Exception as e:
            print(f"[{source_tag}] Error scanning {base_path}: {e}")
    
    async def _process_file(self, filepath: Path, source_tag: str) -> ScrapedItem | None:
        """Process a single file"""
        try:
            stat = filepath.stat()
            
            # Skip large files
            if stat.st_size > self.max_file_size:
                return None
            
            # Skip empty files
            if stat.st_size == 0:
                return None
            
            # Read file
            async with aiofiles.open(filepath, 'rb') as f:
                raw = await f.read()
            
            # Skip binary files
            if b'\x00' in raw[:4096]:
                # But allow PDFs and images for reference
                if filepath.suffix.lower() in ['.pdf', '.png', '.jpg', '.jpeg', '.gif', '.svg']:
                    return ScrapedItem(
                        id=f"{source_tag}:binary:{filepath.as_posix()}",
                        source_type=self.source_type,
                        source_path=str(filepath),
                        content=f"[Binary file: {filepath.name}]\nSize: {stat.st_size} bytes\nPath: {filepath}",
                        content_type=ContentType.BINARY,
                        file_extension=filepath.suffix.lstrip('.'),
                        filename=filepath.name,
                        metadata={
                            "source": source_tag,
                            "is_binary": True,
                            "size_bytes": stat.st_size
                        },
                        confidence_score=0.3
                    )
                return None
            
            # Detect encoding
            detected = chardet.detect(raw[:10000])
            encoding = detected.get('encoding', 'utf-8') or 'utf-8'
            
            try:
                content = raw.decode(encoding)
            except (UnicodeDecodeError, LookupError):
                content = raw.decode('utf-8', errors='ignore')
            
            # Check relevance
            is_relevant, confidence = self.is_relevant(content, filepath.name)
            
            return ScrapedItem(
                id=f"{source_tag}:{filepath.as_posix()}",
                source_type=self.source_type,
                source_path=str(filepath.absolute()),
                content=content,
                content_type=self.detect_content_type(content, filepath.name),
                file_extension=filepath.suffix.lstrip('.') if filepath.suffix else None,
                filename=filepath.name,
                metadata={
                    "source": source_tag,
                    "absolute_path": str(filepath.absolute()),
                    "encoding": encoding,
                    "size_bytes": stat.st_size
                },
                created_at=datetime.fromtimestamp(stat.st_ctime),
                modified_at=datetime.fromtimestamp(stat.st_mtime),
                size_bytes=stat.st_size,
                language=self.detect_language(content, filepath.name),
                confidence_score=max(confidence, 0.2)
            )
            
        except Exception as e:
            return None
    
    async def _extract_archive(self, archive_path: Path, source_tag: str) -> AsyncIterator[ScrapedItem]:
        """Extract and process files from archives"""
        print(f"[{source_tag}] Extracting archive: {archive_path.name}")
        
        try:
            if archive_path.suffix.lower() == '.zip':
                async for item in self._extract_zip(archive_path, source_tag):
                    yield item
            elif archive_path.suffix.lower() == '.7z':
                async for item in self._extract_7z(archive_path, source_tag):
                    yield item
            elif archive_path.suffix.lower() == '.rar':
                async for item in self._extract_rar(archive_path, source_tag):
                    yield item
        except Exception as e:
            print(f"[{source_tag}] Error extracting {archive_path}: {e}")
    
    async def _extract_zip(self, archive_path: Path, source_tag: str) -> AsyncIterator[ScrapedItem]:
        """Extract ZIP archive"""
        try:
            with zipfile.ZipFile(archive_path, 'r') as zf:
                for file_info in zf.filelist:
                    if file_info.is_dir():
                        continue
                    
                    # Skip large files
                    if file_info.file_size > self.max_file_size:
                        continue
                    
                    filename = file_info.filename
                    
                    # Check if interesting file
                    ext = Path(filename).suffix.lower()
                    if ext not in ['.py', '.r', '.js', '.ts', '.json', '.yaml', '.yml', 
                                   '.md', '.txt', '.sql', '.sh', '.html', '.css']:
                        continue
                    
                    try:
                        content = zf.read(file_info.filename)
                        
                        # Skip binary
                        if b'\x00' in content[:1024]:
                            continue
                        
                        try:
                            text_content = content.decode('utf-8')
                        except:
                            text_content = content.decode('utf-8', errors='ignore')
                        
                        yield ScrapedItem(
                            id=f"{source_tag}:zip:{archive_path.name}:{filename}",
                            source_type=self.source_type,
                            source_path=f"{archive_path}!{filename}",
                            content=text_content,
                            content_type=self.detect_content_type(text_content, filename),
                            file_extension=ext.lstrip('.'),
                            filename=Path(filename).name,
                            metadata={
                                "source": source_tag,
                                "archive": str(archive_path),
                                "archive_type": "zip",
                                "internal_path": filename
                            },
                            language=self.detect_language(text_content, filename),
                            confidence_score=0.7
                        )
                    except Exception:
                        continue
                        
        except zipfile.BadZipFile:
            pass
    
    async def _extract_7z(self, archive_path: Path, source_tag: str) -> AsyncIterator[ScrapedItem]:
        """Extract 7z archive"""
        try:
            with py7zr.SevenZipFile(archive_path, mode='r') as archive:
                for filename, bio in archive.read().items():
                    if bio is None:
                        continue
                    
                    content = bio.read()
                    
                    # Check size
                    if len(content) > self.max_file_size:
                        continue
                    
                    # Check if interesting file
                    ext = Path(filename).suffix.lower()
                    if ext not in ['.py', '.r', '.js', '.ts', '.json', '.yaml', '.yml',
                                   '.md', '.txt', '.sql', '.sh', '.html', '.css']:
                        continue
                    
                    # Skip binary
                    if b'\x00' in content[:1024]:
                        continue
                    
                    try:
                        text_content = content.decode('utf-8')
                    except:
                        text_content = content.decode('utf-8', errors='ignore')
                    
                    yield ScrapedItem(
                        id=f"{source_tag}:7z:{archive_path.name}:{filename}",
                        source_type=self.source_type,
                        source_path=f"{archive_path}!{filename}",
                        content=text_content,
                        content_type=self.detect_content_type(text_content, filename),
                        file_extension=ext.lstrip('.'),
                        filename=Path(filename).name,
                        metadata={
                            "source": source_tag,
                            "archive": str(archive_path),
                            "archive_type": "7z",
                            "internal_path": filename
                        },
                        language=self.detect_language(text_content, filename),
                        confidence_score=0.7
                    )
                    
        except Exception as e:
            pass
    
    async def _extract_rar(self, archive_path: Path, source_tag: str) -> AsyncIterator[ScrapedItem]:
        """Extract RAR archive"""
        try:
            with rarfile.RarFile(archive_path, 'r') as rf:
                for file_info in rf.infolist():
                    if file_info.isdir():
                        continue
                    
                    if file_info.file_size > self.max_file_size:
                        continue
                    
                    filename = file_info.filename
                    ext = Path(filename).suffix.lower()
                    
                    if ext not in ['.py', '.r', '.js', '.ts', '.json', '.yaml', '.yml',
                                   '.md', '.txt', '.sql', '.sh', '.html', '.css']:
                        continue
                    
                    try:
                        content = rf.read(file_info.filename)
                        
                        if b'\x00' in content[:1024]:
                            continue
                        
                        try:
                            text_content = content.decode('utf-8')
                        except:
                            text_content = content.decode('utf-8', errors='ignore')
                        
                        yield ScrapedItem(
                            id=f"{source_tag}:rar:{archive_path.name}:{filename}",
                            source_type=self.source_type,
                            source_path=f"{archive_path}!{filename}",
                            content=text_content,
                            content_type=self.detect_content_type(text_content, filename),
                            file_extension=ext.lstrip('.'),
                            filename=Path(filename).name,
                            metadata={
                                "source": source_tag,
                                "archive": str(archive_path),
                                "archive_type": "rar",
                                "internal_path": filename
                            },
                            language=self.detect_language(text_content, filename),
                            confidence_score=0.7
                        )
                    except Exception:
                        continue
                        
        except Exception:
            pass

6. Updated Pipeline with All Your Scrapers

Python

# orchestrator/pipeline.py
"""
Complete Recovery Pipeline with all your specific sources
"""
import asyncio
from typing import List, Dict, Any, Optional
from datetime import datetime
from dataclasses import dataclass
import logging
import os

from scrapers.base import ScrapedItem, SourceType
from scrapers.github_scraper import GitHubScraper
from scrapers.lmarena_scraper import LMArenaScraper
from scrapers.wsl_scraper import WSLScraper
from scrapers.onedrive_scraper import OneDriveRestoredScraper
from processors.processor import DataProcessor
from storage.vector_store import VectorStore
from argilla_integration.datasets import ArgillaManager
from config.settings import settings, load_sources_config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class RecoveryPipeline:
    """Main pipeline for recovering your project data"""
    
    def __init__(self):
        self.config = load_sources_config()
        
        # Add runtime config
        self.config["windows_username"] = os.environ.get("WINDOWS_USERNAME", "eguid")
        self.config["linux_username"] = os.environ.get("LINUX_USERNAME", "eguid")
        
        # Initialize processor
        self.processor = DataProcessor(
            embedding_model=settings.embedding_model,
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )
        
        # Initialize storage
        self.vector_store = VectorStore(
            url=settings.qdrant_url,
            collection_name=settings.qdrant_collection
        )
        
        # Initialize Argilla
        self.argilla = ArgillaManager(
            api_url=settings.argilla_api_url,
            api_key=settings.argilla_api_key,
            workspace=settings.argilla_workspace
        )
        
        # Initialize scrapers
        self.scrapers = self._init_scrapers()
        
        # State
        self.status = "idle"
        self.runs_history = []
        self.item_buffer = []
        self.buffer_size = 50
        
    def _init_scrapers(self) -> Dict[str, Any]:
        """Initialize all scrapers for your specific sources"""
        scrapers = {}
        
        logger.info("Initializing scrapers...")
        
        # 1. LM Arena Chat Logs
        logger.info("  - LM Arena scraper")
        scrapers['lmarena'] = LMArenaScraper(self.config)
        
        # 2. WSL/Linux
        logger.info("  - WSL scraper")
        scrapers['wsl'] = WSLScraper(self.config)
        
        # 3. OneDrive + Restored + Local
        logger.info("  - OneDrive/Restored/Local scraper")
        scrapers['files'] = OneDriveRestoredScraper(self.config)
        
        # 4. GitHub (optional)
        if self.config.get("sources", {}).get("github", {}).get("enabled", False):
            logger.info("  - GitHub scraper")
            scrapers['github'] = GitHubScraper(
                self.config,
                token=settings.github_token
            )
        
        return scrapers
    
    async def run_full_pipeline(self) -> Dict:
        """Run the complete recovery pipeline"""
        run_id = f"run_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"
        
        result = {
            "run_id": run_id,
            "started_at": datetime.utcnow().isoformat(),
            "status": "running",
            "sources": {},
            "total_items": 0,
            "total_processed": 0,
            "total_stored": 0,
            "errors": []
        }
        
        self.status = "running"
        logger.info(f"{'='*60}")
        logger.info(f"Starting pipeline run: {run_id}")
        logger.info(f"{'='*60}")
        
        try:
            # Create Argilla dataset
            dataset = self.argilla.create_recovery_dataset(
                name=f"recovery_{run_id}"
            )
            logger.info(f"Created Argilla dataset: recovery_{run_id}")
            
            # Run each scraper
            for source_name, scraper in self.scrapers.items():
                source_result = {
                    "items_found": 0,
                    "items_processed": 0,
                    "errors": []
                }
                
                logger.info(f"\n{'='*40}")
                logger.info(f"Running scraper: {source_name}")
                logger.info(f"{'='*40}")
                
                try:
                    if await scraper.validate_connection():
                        async for item in scraper.scrape():
                            source_result["items_found"] += 1
                            result["total_items"] += 1
                            
                            await self._process_item(item, dataset, result)
                            
                            if result["total_items"] % 50 == 0:
                                logger.info(f"Progress: {result['total_items']} items scraped, {result['total_processed']} processed")
                    else:
                        msg = f"Could not connect to {source_name}"
                        logger.warning(msg)
                        source_result["errors"].append(msg)
                        
                except Exception as e:
                    error_msg = f"Error in {source_name}: {str(e)}"
                    logger.error(error_msg)
                    source_result["errors"].append(error_msg)
                    result["errors"].append(error_msg)
                
                result["sources"][source_name] = source_result
                logger.info(f"Completed {source_name}: {source_result['items_found']} items found")
            
            # Flush remaining buffer
            await self._flush_buffer(dataset, result)
            
            result["status"] = "completed"
            
        except Exception as e:
            result["status"] = "error"
            result["errors"].append(f"Pipeline error: {str(e)}")
            logger.error(f"Pipeline failed: {e}")
            
        finally:
            result["ended_at"] = datetime.utcnow().isoformat()
            self.status = "idle"
            self.runs_history.append(result)
        
        # Print summary
        logger.info(f"\n{'='*60}")
        logger.info("PIPELINE COMPLETE")
        logger.info(f"{'='*60}")
        logger.info(f"  Total Items Scraped: {result['total_items']}")
        logger.info(f"  Total Processed: {result['total_processed']}")
        logger.info(f"  Total Stored: {result['total_stored']}")
        logger.info(f"  Errors: {len(result['errors'])}")
        logger.info(f"{'='*60}")
        
        return result
    
    async def run_single_source(self, source_name: str) -> Dict:
        """Run only a specific source scraper"""
        if source_name not in self.scrapers:
            return {"error": f"Unknown source: {source_name}. Available: {list(self.scrapers.keys())}"}
        
        scraper = self.scrapers[source_name]
        
        result = {
            "source": source_name,
            "items_found": 0,
            "items_processed": 0,
            "items_stored": 0,
            "errors": []
        }
        
        logger.info(f"Running single source: {source_name}")
        
        try:
            if await scraper.validate_connection():
                async for item in scraper.scrape():
                    result["items_found"] += 1
                    
                    # Process immediately
                    chunks = self.processor.process(item)
                    if chunks:
                        stored = self.vector_store.upsert_chunks(chunks)
                        result["items_processed"] += 1
                        result["items_stored"] += stored
                        
                    if result["items_found"] % 50 == 0:
                        logger.info(f"Progress: {result['items_found']} items found")
            else:
                result["errors"].append("Connection validation failed")
                
        except Exception as e:
            result["errors"].append(str(e))
            logger.error(f"Error: {e}")
        
        logger.info(f"Completed: {result['items_found']} found, {result['items_processed']} processed")
        return result
    
    async def _process_item(self, item: ScrapedItem, dataset, result: Dict):
        """Process a single item"""
        self.item_buffer.append(item)
        
        if len(self.item_buffer) >= self.buffer_size:
            await self._flush_buffer(dataset, result)
    
    async def _flush_buffer(self, dataset, result: Dict):
        """Flush buffer to storage"""
        if not self.item_buffer:
            return
        
        for item in self.item_buffer:
            try:
                chunks = self.processor.process(item)
                if chunks:
                    stored = self.vector_store.upsert_chunks(chunks)
                    result["total_stored"] += stored
                result["total_processed"] += 1
            except Exception as e:
                logger.warning(f"Error processing item: {e}")
        
        # Add to Argilla
        try:
            self.argilla.add_items_to_dataset(dataset, self.item_buffer)
        except Exception as e:
            logger.warning(f"Error adding to Argilla: {e}")
        
        self.item_buffer.clear()
    
    def search(self, query: str, limit: int = 10, filters: Dict = None) -> List[Dict]:
        """Search recovered data"""
        return self.vector_store.search_by_text(
            query,
            self.processor.embedding_model,
            limit,
            filters
        )
    
    def get_stats(self) -> Dict:
        """Get system statistics"""
        return {
            "status": self.status,
            "vector_store": self.vector_store.get_statistics(),
            "total_runs": len(self.runs_history),
            "scrapers": list(self.scrapers.keys()),
            "last_run": self.runs_history[-1] if self.runs_history else None
        }

7. Main Entry Point

Python

# main.py
"""
Project Recovery System - Main Entry Point

Usage:
    python main.py pipeline          # Run full pipeline
    python main.py source <name>     # Run single source
    python main.py search            # Interactive search
    python main.py api               # Start API server
    python main.py dashboard         # Start dashboard
"""
import asyncio
import argparse
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()


async def run_pipeline():
    """Run the full recovery pipeline"""
    from orchestrator.pipeline import RecoveryPipeline
    
    console.print(Panel.fit(
        "[bold blue]🔍 Project Recovery Pipeline[/bold blue]\n"
        "Scanning all configured sources...",
        border_style="blue"
    ))
    
    pipeline = RecoveryPipeline()
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Running pipeline...", total=None)
        result = await pipeline.run_full_pipeline()
    
    # Display results
    table = Table(title="Pipeline Results")
    table.add_column("Source", style="cyan")
    table.add_column("Items Found", style="green")
    table.add_column("Errors", style="red")
    
    for source, data in result.get("sources", {}).items():
        table.add_row(
            source,
            str(data.get("items_found", 0)),
            str(len(data.get("errors", [])))
        )
    
    console.print(table)
    
    console.print(f"\n[bold green]Total Items:[/bold green] {result['total_items']}")
    console.print(f"[bold green]Total Processed:[/bold green] {result['total_processed']}")
    console.print(f"[bold green]Total Stored:[/bold green] {result['total_stored']}")
    
    if result.get("errors"):
        console.print(f"\n[yellow]Errors ({len(result['errors'])}):[/yellow]")
        for err in result["errors"][:5]:
            console.print(f"  - {err}")


async def run_source(source_name: str):
    """Run a single source"""
    from orchestrator.pipeline import RecoveryPipeline
    
    console.print(f"[bold blue]Running source: {source_name}[/bold blue]")
    
    pipeline = RecoveryPipeline()
    result = await pipeline.run_single_source(source_name)
    
    console.print(f"\n[green]Results:[/green]")
    console.print(f"  Items found: {result.get('items_found', 0)}")
    console.print(f"  Items processed: {result.get('items_processed', 0)}")
    console.print(f"  Items stored: {result.get('items_stored', 0)}")
    
    if result.get('errors'):
        console.print(f"[yellow]  Errors: {len(result['errors'])}[/yellow]")


async def interactive_search():
    """Interactive search"""
    from orchestrator.pipeline import RecoveryPipeline
    
    console.print(Panel.fit(
        "[bold blue]🔍 Interactive Search[/bold blue]",
        border_style="blue"
    ))
    
    pipeline = RecoveryPipeline()
    
    while True:
        query = console.input("\n[cyan]Search query[/cyan] (or 'quit'): ")
        
        if query.lower() in ['quit', 'exit', 'q']:
            break
        
        results = pipeline.search(query, limit=10)
        
        if not results:
            console.print("[yellow]No results found[/yellow]")
            continue
        
        console.print(f"\n[green]Found {len(results)} results:[/green]\n")
        
        for i, result in enumerate(results, 1):
            console.print(Panel(
                f"[bold]{result.get('filename', 'Unknown')}[/bold]\n"
                f"Score: {result.get('score', 0):.3f} | Source: {result.get('source_type', 'unknown')}\n\n"
                f"{result.get('content', '')[:400]}...",
                title=f"Result {i}",
                border_style="blue"
            ))


def run_api():
    """Run API server"""
    import uvicorn
    console.print("[bold blue]Starting API server on http://localhost:8000[/bold blue]")
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=True)


def run_dashboard():
    """Run Streamlit dashboard"""
    import subprocess
    console.print("[bold blue]Starting dashboard on http://localhost:8501[/bold blue]")
    subprocess.run(["streamlit", "run", "ui/dashboard.py", "--server.port", "8501"])


def main():
    parser = argparse.ArgumentParser(
        description="Project Recovery System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python main.py pipeline              Run full pipeline
    python main.py source lmarena        Scrape LM Arena chats
    python main.py source wsl            Scrape WSL filesystem
    python main.py source files          Scrape OneDrive/Restored/Local
    python main.py search                Interactive search
    python main.py api                   Start API server
    python main.py dashboard             Start dashboard
        """
    )
    
    parser.add_argument(
        "command",
        choices=["pipeline", "source", "search", "api", "dashboard", "stats"],
        help="Command to run"
    )
    
    parser.add_argument(
        "source_name",
        nargs="?",
        default=None,
        help="Source name for 'source' command (lmarena, wsl, files, github)"
    )
    
    args = parser.parse_args()
    
    if args.command == "pipeline":
        asyncio.run(run_pipeline())
    elif args.command == "source":
        if not args.source_name:
            console.print("[red]Please specify a source name: lmarena, wsl, files, github[/red]")
            sys.exit(1)
        asyncio.run(run_source(args.source_name))
    elif args.command == "search":
        asyncio.run(interactive_search())
    elif args.command == "api":
        run_api()
    elif args.command == "dashboard":
        run_dashboard()
    elif args.command == "stats":
        from orchestrator.pipeline import RecoveryPipeline
        pipeline = RecoveryPipeline()
        stats = pipeline.get_stats()
        console.print(stats)


if __name__ == "__main__":
    main()

8. Requirements.txt

txt

# requirements.txt

# Core
argilla>=1.20.0
fastapi>=0.104.0
uvicorn>=0.24.0
pydantic>=2.0.0
pydantic-settings>=2.0.0

# Async
aiohttp>=3.9.0
aiofiles>=23.2.0
asyncio>=3.4.3

# Database & Storage
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
qdrant-client>=1.6.0
redis>=5.0.0

# ML/Embeddings
sentence-transformers>=2.2.0
torch>=2.0.0

# Web Scraping
beautifulsoup4>=4.12.0
httpx>=0.25.0

# GitHub
PyGithub>=2.1.0

# File Processing
chardet>=5.2.0
python-magic>=0.4.27
py7zr>=0.20.0
rarfile>=4.1

# Task Queue
celery>=5.3.0

# Configuration
python-dotenv>=1.0.0
pyyaml>=6.0.0

# CLI & UI
rich>=13.0.0
streamlit>=1.28.0
plotly>=5.18.0

# Utilities
pandas>=2.0.0
watchdog>=3.0.0

# Crypto (for secrets)
cryptography>=41.0.0

Quick Start

PowerShell

# PowerShell - Quick Setup

# 1. Create project and virtual environment
mkdir project-recovery
cd project-recovery
python -m venv venv
.\venv\Scripts\Activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Copy and edit .env file with your GitHub token

# 4. Start Docker services
docker-compose up -d

# 5. Run the pipeline
python main.py pipeline

# Or run specific sources:
python main.py source lmarena    # Scan LM Arena chats
python main.py source wsl        # Scan WSL filesystem
python main.py source files      # Scan OneDrive/Restored/Local

# 6. Search your data
python main.py search

# 7. Open Argilla to review data
# http://localhost:6900

This setup will scan:

    LM Arena - Your 11 specific chat URLs + browser cache/history
    WSL - \\wsl.localhost\* with all distros
    G:/restored - Your restored data drive
    OneDrive - Personal Vault, AppData, Desktop, drivers and apps, Pictures
    Local folders - Documents, Desktop, Downloads, etc.

Would you like me to add any additional features or modify any of the configurations?

https://lmarena.ai/c/019b364c-8fbd-722b-949d-9bb5c17a516f
https://lmarena.ai/c/019b352d-09a8-78de-9002-5d11440aac80
https://lmarena.ai/c/019b352d-09a8-78de-9002-5d11440aac80
https://lmarena.ai/c/019b352a-e9b8-7a99-8d3b-f7cfe5a7946e
https://lmarena.ai/c/019b3529-b512-701d-a054-bd7d1e4e6917
https://lmarena.ai/c/019b1ef3-a33d-7722-a2ea-c406c8d0a4d5
https://lmarena.ai/c/019b0a05-e1e5-7764-a9ff-94e74c1826a3
https://lmarena.ai/c/019b15a6-06aa-7090-b65f-f98510c2ad01
https://lmarena.ai/c/019b15a6-06aa-7090-b65f-f98510c2ad01
https://lmarena.ai/c/019b0e15-dc4e-714d-ac7b-04f592f66f8c
https://lmarena.ai/c/019b0e15-dc4e-714d-ac7b-04f592f66f8c
https://lmarena.ai/c/019b0e13-edfa-7e43-b8dd-8aa28d0b3eb3
https://lmarena.ai/c/019b0e3a-1787-7506-81cd-99d376b57b62https://lmarena.ai/c/019b0c74-9fbf-7c68-9521-aa4c67eb165b https://lmarena.ai/c/019b0c74-9fbf-7c68-9521-aa4c67eb165b
https://lmarena.ai/c/019b0c74-9fbf-7c68-9521-aa4c67eb165b
https://lmarena.ai/c/019b0c74-9fbf-7c68-9521-aa4c67eb165b
https://lmarena.ai/c/019b0c74-9fbf-7c68-9521-aa4c67eb165b

All in \wsl.localhost

//
"G:\restored"

"C:\Users\eguid\OneDrive\Personal Vault.lnk"
"C:\Users\eguid\OneDrive\AppData"
"C:\Users\eguid\OneDrive\Desktop"
"C:\Users\eguid\OneDrive\drivers and apps"
"C:\Users\eguid\OneDrive\Pictures" those are the locations that there will be some info
claude-opus-4-5-20251101-thinking-32k
Complete VS Code Setup with Secrets Management
Project Structure

text

project-recovery/
├── .vscode/
│   ├── settings.json
│   ├── launch.json
│   ├── tasks.json
│   └── extensions.json
├── .env                    # Your secrets (git-ignored)
├── .env.example           # Template (committed)
├── .gitignore
├── secrets/
│   ├── __init__.py
│   ├── manager.py
│   └── google_credentials.json  # (git-ignored)
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── sources.yaml
├── project-recovery.code-workspace
└── ... (rest of project)

1. VS Code Workspace File

JSON

// project-recovery.code-workspace
{
    "folders": [
        {
            "name": "🔍 Project Recovery",
            "path": "."
        }
    ],
    "settings": {
        // Python
        "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe",
        "python.terminal.activateEnvironment": true,
        "python.analysis.typeCheckingMode": "basic",
        "python.analysis.autoImportCompletions": true,
        
        // Editor
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        },
        
        // Files
        "files.exclude": {
            "**/__pycache__": true,
            "**/*.pyc": true,
            ".venv": true,
            "venv": true
        },
        
        // Terminal
        "terminal.integrated.env.windows": {
            "PYTHONPATH": "${workspaceFolder}"
        },
        "terminal.integrated.env.linux": {
            "PYTHONPATH": "${workspaceFolder}"
        },
        
        // Environment variables
        "python.envFile": "${workspaceFolder}/.env",
        
        // Search
        "search.exclude": {
            "**/node_modules": true,
            "**/venv": true,
            "**/.venv": true,
            "**/data": true
        }
    },
    "extensions": {
        "recommendations": [
            "ms-python.python",
            "ms-python.vscode-pylance",
            "ms-python.debugpy",
            "ms-toolsai.jupyter",
            "redhat.vscode-yaml",
            "tamasfe.even-better-toml",
            "mikestead.dotenv",
            "mechatroner.rainbow-csv",
            "ms-azuretools.vscode-docker",
            "eamodio.gitlens",
            "usernamehw.errorlens",
            "streetsidesoftware.code-spell-checker"
        ]
    },
    "launch": {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "🚀 Run Full Pipeline",
                "type": "debugpy",
                "request": "launch",
                "program": "${workspaceFolder}/main.py",
                "args": ["pipeline"],
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env",
                "justMyCode": false
            },
            {
                "name": "🌐 Run API Server",
                "type": "debugpy",
                "request": "launch",
                "module": "uvicorn",
                "args": ["api.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"],
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            },
            {
                "name": "📊 Run Dashboard",
                "type": "debugpy",
                "request": "launch",
                "module": "streamlit",
                "args": ["run", "ui/dashboard.py"],
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env"
            }
        ],
        "compounds": [
            {
                "name": "🔥 Full Stack",
                "configurations": ["🌐 Run API Server", "📊 Run Dashboard"]
            }
        ]
    },
    "tasks": {
        "version": "2.0.0",
        "tasks": [
            {
                "label": "🐳 Docker Up",
                "type": "shell",
                "command": "docker-compose up -d",
                "problemMatcher": []
            },
            {
                "label": "🛑 Docker Down",
                "type": "shell",
                "command": "docker-compose down",
                "problemMatcher": []
            },
            {
                "label": "📦 Install Dependencies",
                "type": "shell",
                "command": "pip install -r requirements.txt",
                "problemMatcher": []
            }
        ]
    }
}

2. VS Code Settings

JSON

// .vscode/settings.json
{
    // ===========================================
    // PYTHON CONFIGURATION
    // ===========================================
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/Scripts/python.exe",
    "python.terminal.activateEnvironment": true,
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.autoImportCompletions": true,
    "python.analysis.inlayHints.functionReturnTypes": true,
    "python.analysis.inlayHints.variableTypes": true,
    
    // Formatting
    "[python]": {
        "editor.defaultFormatter": "ms-python.python",
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        },
        "editor.rulers": [88, 120]
    },
    
    // ===========================================
    // ENVIRONMENT & SECRETS
    // ===========================================
    "python.envFile": "${workspaceFolder}/.env",
    "terminal.integrated.env.windows": {
        "PYTHONPATH": "${workspaceFolder}",
        "PYTHONDONTWRITEBYTECODE": "1"
    },
    "terminal.integrated.env.linux": {
        "PYTHONPATH": "${workspaceFolder}",
        "PYTHONDONTWRITEBYTECODE": "1"
    },
    
    // ===========================================
    // EDITOR
    // ===========================================
    "editor.fontSize": 14,
    "editor.tabSize": 4,
    "editor.insertSpaces": true,
    "editor.wordWrap": "on",
    "editor.minimap.enabled": true,
    "editor.bracketPairColorization.enabled": true,
    "editor.guides.bracketPairs": true,
    "editor.stickyScroll.enabled": true,
    
    // ===========================================
    // FILES
    // ===========================================
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,
    "files.exclude": {
        "**/__pycache__": true,
        "**/*.pyc": true,
        "**/.pytest_cache": true,
        "**/.mypy_cache": true,
        "**/venv": true,
        "**/.venv": true,
        "**/*.egg-info": true,
        "**/node_modules": true
    },
    "files.watcherExclude": {
        "**/venv/**": true,
        "**/.venv/**": true,
        "**/data/**": true
    },
    
    // ===========================================
    // SEARCH
    // ===========================================
    "search.exclude": {
        "**/venv": true,
        "**/.venv": true,
        "**/data": true,
        "**/exports": true,
        "**/.git": true
    },
    
    // ===========================================
    // YAML (for config files)
    // ===========================================
    "[yaml]": {
        "editor.defaultFormatter": "redhat.vscode-yaml",
        "editor.tabSize": 2
    },
    "yaml.schemas": {
        "${workspaceFolder}/config/sources.schema.json": "sources.yaml"
    },
    
    // ===========================================
    // JSON
    // ===========================================
    "[json]": {
        "editor.defaultFormatter": "vscode.json-language-features",
        "editor.tabSize": 2
    },
    "[jsonc]": {
        "editor.defaultFormatter": "vscode.json-language-features",
        "editor.tabSize": 2
    },
    
    // ===========================================
    // DOCKER
    // ===========================================
    "[dockerfile]": {
        "editor.defaultFormatter": "ms-azuretools.vscode-docker"
    },
    
    // ===========================================
    // GIT
    // ===========================================
    "git.autofetch": true,
    "git.confirmSync": false,
    "gitlens.hovers.currentLine.over": "line",
    
    // ===========================================
    // SECURITY - HIDE SECRETS IN EDITOR
    // ===========================================
    "editor.tokenColorCustomizations": {
        "textMateRules": [
            {
                "scope": "string.quoted.double.env",
                "settings": {
                    "foreground": "#569CD6"
                }
            }
        ]
    }
}

3. Launch Configurations (Debug)

JSON

// .vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
        // ===========================================
        // MAIN PIPELINE
        // ===========================================
        {
            "name": "🚀 Run Full Pipeline",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "args": ["pipeline"],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env",
            "justMyCode": false,
            "cwd": "${workspaceFolder}"
        },
        {
            "name": "🔍 Run Single Source - GitHub",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/run_source.py",
            "args": ["github"],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        {
            "name": "💾 Run Single Source - Local Drives",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/run_source.py",
            "args": ["local_drives"],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        {
            "name": "📊 Run Single Source - RStudio",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/run_source.py",
            "args": ["rstudio"],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        {
            "name": "🐧 Run Single Source - Linux",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/run_source.py",
            "args": ["linux_system"],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        {
            "name": "💬 Run Single Source - LM Arena",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/run_source.py",
            "args": ["lmarena"],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        
        // ===========================================
        // API SERVER
        // ===========================================
        {
            "name": "🌐 Run API Server",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "api.main:app",
                "--reload",
                "--host", "0.0.0.0",
                "--port", "8000"
            ],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env",
            "cwd": "${workspaceFolder}"
        },
        {
            "name": "🌐 API Server (Production)",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "api.main:app",
                "--host", "0.0.0.0",
                "--port", "8000",
                "--workers", "4"
            ],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        
        // ===========================================
        // DASHBOARD
        // ===========================================
        {
            "name": "📊 Run Dashboard",
            "type": "debugpy",
            "request": "launch",
            "module": "streamlit",
            "args": [
                "run",
                "ui/dashboard.py",
                "--server.port", "8501",
                "--server.headless", "true"
            ],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env",
            "cwd": "${workspaceFolder}"
        },
        
        // ===========================================
        // WORKERS
        // ===========================================
        {
            "name": "⚙️ Celery Worker",
            "type": "debugpy",
            "request": "launch",
            "module": "celery",
            "args": [
                "-A", "orchestrator.tasks",
                "worker",
                "--loglevel=info"
            ],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        {
            "name": "⏰ Celery Beat (Scheduler)",
            "type": "debugpy",
            "request": "launch",
            "module": "celery",
            "args": [
                "-A", "orchestrator.tasks",
                "beat",
                "--loglevel=info"
            ],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        
        // ===========================================
        // SETUP & UTILITIES
        // ===========================================
        {
            "name": "🔧 Setup Sources (Interactive)",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/setup_sources.py",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        {
            "name": "🔎 Search Data",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/search.py",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        {
            "name": "📤 Export Curated Data",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/export.py",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        {
            "name": "🧪 Run Tests",
            "type": "debugpy",
            "request": "launch",
            "module": "pytest",
            "args": [
                "tests/",
                "-v",
                "--tb=short"
            ],
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env"
        },
        
        // ===========================================
        // CURRENT FILE
        // ===========================================
        {
            "name": "▶️ Run Current File",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "envFile": "${workspaceFolder}/.env",
            "cwd": "${workspaceFolder}"
        }
    ],
    
    // ===========================================
    // COMPOUND CONFIGURATIONS
    // ===========================================
    "compounds": [
        {
            "name": "🔥 Full Stack (API + Dashboard)",
            "configurations": [
                "🌐 Run API Server",
                "📊 Run Dashboard"
            ],
            "stopAll": true
        },
        {
            "name": "🔥 Full Stack + Worker",
            "configurations": [
                "🌐 Run API Server",
                "📊 Run Dashboard",
                "⚙️ Celery Worker"
            ],
            "stopAll": true
        },
        {
            "name": "🔥 Complete System",
            "configurations": [
                "🌐 Run API Server",
                "📊 Run Dashboard",
                "⚙️ Celery Worker",
                "⏰ Celery Beat (Scheduler)"
            ],
            "stopAll": true
        }
    ]
}

4. Tasks Configuration

JSON

// .vscode/tasks.json
{
    "version": "2.0.0",
    "tasks": [
        // ===========================================
        // DOCKER
        // ===========================================
        {
            "label": "🐳 Docker: Start All Services",
            "type": "shell",
            "command": "docker-compose up -d",
            "problemMatcher": [],
            "group": "build",
            "presentation": {
                "reveal": "always",
                "panel": "new"
            }
        },
        {
            "label": "🐳 Docker: Stop All Services",
            "type": "shell",
            "command": "docker-compose down",
            "problemMatcher": []
        },
        {
            "label": "🐳 Docker: Restart",
            "type": "shell",
            "command": "docker-compose restart",
            "problemMatcher": []
        },
        {
            "label": "🐳 Docker: View Logs",
            "type": "shell",
            "command": "docker-compose logs -f",
            "problemMatcher": [],
            "presentation": {
                "reveal": "always",
                "panel": "dedicated"
            }
        },
        {
            "label": "🐳 Docker: Build",
            "type": "shell",
            "command": "docker-compose build",
            "problemMatcher": [],
            "group": "build"
        },
        
        // ===========================================
        // PYTHON ENVIRONMENT
        // ===========================================
        {
            "label": "🐍 Create Virtual Environment",
            "type": "shell",
            "command": "python -m venv venv",
            "problemMatcher": [],
            "windows": {
                "command": "python -m venv venv"
            }
        },
        {
            "label": "📦 Install Dependencies",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/pip install -r requirements.txt",
            "problemMatcher": [],
            "windows": {
                "command": ".\\venv\\Scripts\\pip install -r requirements.txt"
            },
            "linux": {
                "command": "./venv/bin/pip install -r requirements.txt"
            }
        },
        {
            "label": "📦 Install Dev Dependencies",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/pip install -r requirements-dev.txt",
            "problemMatcher": []
        },
        {
            "label": "📦 Freeze Requirements",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/pip freeze > requirements-lock.txt",
            "problemMatcher": []
        },
        
        // ===========================================
        // PIPELINE
        // ===========================================
        {
            "label": "🚀 Run Full Pipeline",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python main.py pipeline",
            "problemMatcher": [],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        },
        {
            "label": "🔍 Run GitHub Scraper",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python run_source.py github",
            "problemMatcher": []
        },
        {
            "label": "💾 Run Local Drives Scraper",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python run_source.py local_drives",
            "problemMatcher": []
        },
        {
            "label": "📊 Run RStudio Scraper",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python run_source.py rstudio",
            "problemMatcher": []
        },
        {
            "label": "🐧 Run Linux Scraper",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python run_source.py linux_system",
            "problemMatcher": []
        },
        {
            "label": "💬 Run LM Arena Scraper",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python run_source.py lmarena",
            "problemMatcher": []
        },
        
        // ===========================================
        // UTILITIES
        // ===========================================
        {
            "label": "🔧 Setup Sources (Interactive)",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python setup_sources.py",
            "problemMatcher": [],
            "presentation": {
                "reveal": "always",
                "focus": true
            }
        },
        {
            "label": "📤 Export Curated Data",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python export.py",
            "problemMatcher": []
        },
        {
            "label": "🔎 Search (Interactive)",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python search.py",
            "problemMatcher": [],
            "presentation": {
                "reveal": "always",
                "focus": true
            }
        },
        
        // ===========================================
        // TESTING & QUALITY
        // ===========================================
        {
            "label": "🧪 Run Tests",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/pytest tests/ -v",
            "problemMatcher": [],
            "group": {
                "kind": "test",
                "isDefault": true
            }
        },
        {
            "label": "🔍 Lint Code",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python -m flake8 .",
            "problemMatcher": []
        },
        {
            "label": "📝 Format Code",
            "type": "shell",
            "command": "${workspaceFolder}/venv/Scripts/python -m black .",
            "problemMatcher": []
        },
        
        // ===========================================
        // OPEN SERVICES
        // ===========================================
        {
            "label": "🌐 Open API Docs",
            "type": "shell",
            "command": "start http://localhost:8000/docs",
            "problemMatcher": [],
            "windows": {
                "command": "start http://localhost:8000/docs"
            },
            "linux": {
                "command": "xdg-open http://localhost:8000/docs"
            }
        },
        {
            "label": "📊 Open Dashboard",
            "type": "shell",
            "command": "start http://localhost:8501",
            "problemMatcher": [],
            "windows": {
                "command": "start http://localhost:8501"
            },
            "linux": {
                "command": "xdg-open http://localhost:8501"
            }
        },
        {
            "label": "🏷️ Open Argilla",
            "type": "shell",
            "command": "start http://localhost:6900",
            "problemMatcher": [],
            "windows": {
                "command": "start http://localhost:6900"
            },
            "linux": {
                "command": "xdg-open http://localhost:6900"
            }
        }
    ]
}

5. Extensions Recommendations

JSON

// .vscode/extensions.json
{
    "recommendations": [
        // Python
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.debugpy",
        "ms-python.black-formatter",
        "ms-python.isort",
        
        // Jupyter/Data
        "ms-toolsai.jupyter",
        "ms-toolsai.jupyter-keymap",
        "ms-toolsai.jupyter-renderers",
        
        // Configuration files
        "redhat.vscode-yaml",
        "tamasfe.even-better-toml",
        "mikestead.dotenv",
        
        // Docker
        "ms-azuretools.vscode-docker",
        
        // Git
        "eamodio.gitlens",
        "mhutchie.git-graph",
        
        // Data/CSV
        "mechatroner.rainbow-csv",
        "GrapeCity.gc-excelviewer",
        
        // Utilities
        "usernamehw.errorlens",
        "streetsidesoftware.code-spell-checker",
        "gruntfuggly.todo-tree",
        "wayou.vscode-todo-highlight",
        "christian-kohler.path-intellisense",
        
        // REST API testing
        "humao.rest-client",
        "rangav.vscode-thunder-client",
        
        // Markdown
        "yzhang.markdown-all-in-one",
        "bierner.markdown-mermaid",
        
        // Remote development
        "ms-vscode-remote.remote-wsl",
        "ms-vscode-remote.remote-containers",
        
        // Database
        "cweijan.vscode-postgresql-client2"
    ],
    "unwantedRecommendations": []
}

6. Environment Files (Secrets)

Bash

# .env.example - Template file (commit this)
# ============================================
# PROJECT RECOVERY SYSTEM - CONFIGURATION
# ============================================
# Copy this file to .env and fill in your values
# NEVER commit .env to version control!

# ============================================
# GITHUB
# ============================================
# Get token from: https://github.com/settings/tokens
# Required scopes: repo, gist, read:user
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GITHUB_USERNAME=your_github_username

# ============================================
# ARGILLA (Data Labeling Platform)
# ============================================
ARGILLA_API_URL=http://localhost:6900
ARGILLA_API_KEY=admin.apikey
ARGILLA_WORKSPACE=project_recovery

# ============================================
# DATABASE
# ============================================
DATABASE_URL=postgresql://recovery:recovery_pass@localhost:5432/project_recovery
POSTGRES_USER=recovery
POSTGRES_PASSWORD=recovery_pass
POSTGRES_DB=project_recovery

# ============================================
# VECTOR STORE (Qdrant)
# ============================================
QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION=project_fragments

# ============================================
# REDIS (Task Queue)
# ============================================
REDIS_URL=redis://localhost:6379

# ============================================
# USER PATHS - WINDOWS
# ============================================
# Your Windows username (for path resolution)
WINDOWS_USERNAME=YourWindowsUsername

# ============================================
# USER PATHS - LINUX/WSL
# ============================================
LINUX_USERNAME=your_linux_username

# ============================================
# GOOGLE DRIVE (Optional)
# ============================================
# Path to Google service account JSON
GOOGLE_CREDENTIALS_PATH=./secrets/google_credentials.json
# Or use OAuth
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=

# ============================================
# EMAIL/IMAP (Optional)
# ============================================
IMAP_SERVER=imap.gmail.com
IMAP_PORT=993
EMAIL_ADDRESS=your.email@gmail.com
# For Gmail, use App Password: https://myaccount.google.com/apppasswords
EMAIL_PASSWORD=xxxx xxxx xxxx xxxx

# ============================================
# LM ARENA / OPENAI (Optional)
# ============================================
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ============================================
# EMBEDDING MODEL
# ============================================
EMBEDDING_MODEL=all-MiniLM-L6-v2

# ============================================
# PROCESSING
# ============================================
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
SCRAPE_INTERVAL_HOURS=6

# ============================================
# LOGGING
# ============================================
LOG_LEVEL=INFO
LOG_FILE=./logs/recovery.log

Bash

# .env - Your actual secrets (DO NOT COMMIT)
# ============================================
# PROJECT RECOVERY SYSTEM - YOUR SECRETS
# ============================================

# ============================================
# GITHUB - FILL THESE IN!
# ============================================
GITHUB_TOKEN=ghp_YOUR_ACTUAL_TOKEN_HERE
GITHUB_USERNAME=YOUR_ACTUAL_USERNAME

# ============================================
# ARGILLA
# ============================================
ARGILLA_API_URL=http://localhost:6900
ARGILLA_API_KEY=admin.apikey
ARGILLA_WORKSPACE=project_recovery

# ============================================
# DATABASE
# ============================================
DATABASE_URL=postgresql://recovery:your_secure_password@localhost:5432/project_recovery
POSTGRES_USER=recovery
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=project_recovery

# ============================================
# VECTOR STORE
# ============================================
QDRANT_URL=http://localhost:6333
QDRANT_COLLECTION=project_fragments

# ============================================
# REDIS
# ============================================
REDIS_URL=redis://localhost:6379

# ============================================
# YOUR PATHS - UPDATE THESE!
# ============================================
WINDOWS_USERNAME=YourActualWindowsUsername
LINUX_USERNAME=your_actual_linux_username

# ============================================
# GOOGLE (if using)
# ============================================
GOOGLE_CREDENTIALS_PATH=./secrets/google_credentials.json

# ============================================
# EMAIL (if using)
# ============================================
IMAP_SERVER=imap.gmail.com
EMAIL_ADDRESS=your.actual.email@gmail.com
EMAIL_PASSWORD=your_app_password_here

# ============================================
# PROCESSING
# ============================================
EMBEDDING_MODEL=all-MiniLM-L6-v2
CHUNK_SIZE=1000
CHUNK_OVERLAP=200
SCRAPE_INTERVAL_HOURS=6
LOG_LEVEL=INFO

7. Secrets Manager Module

Python

# secrets/__init__.py
"""
Secrets management for Project Recovery System
"""
from .manager import SecretsManager, get_secret, load_all_secrets

__all__ = ['SecretsManager', 'get_secret', 'load_all_secrets']

Python

# secrets/manager.py
"""
Secure secrets management
"""
import os
import json
from pathlib import Path
from typing import Optional, Dict, Any
from dataclasses import dataclass, field
from functools import lru_cache
import base64
from cryptography.fernet import Fernet
from dotenv import load_dotenv


@dataclass
class SecretsManager:
    """
    Manages secrets from multiple sources:
    1. Environment variables
    2. .env file
    3. Encrypted secrets file
    4. Cloud secret managers (optional)
    """
    env_file: str = ".env"
    secrets_dir: str = "./secrets"
    encryption_key: Optional[str] = None
    _secrets: Dict[str, Any] = field(default_factory=dict)
    _loaded: bool = False
    
    def __post_init__(self):
        self.secrets_path = Path(self.secrets_dir)
        self.secrets_path.mkdir(exist_ok=True)
        self._load_secrets()
    
    def _load_secrets(self):
        """Load secrets from all sources"""
        if self._loaded:
            return
        
        # 1. Load from .env file
        env_path = Path(self.env_file)
        if env_path.exists():
            load_dotenv(env_path)
        
        # 2. Load all environment variables
        self._secrets.update(os.environ)
        
        # 3. Load from encrypted file if exists
        encrypted_path = self.secrets_path / "secrets.encrypted"
        if encrypted_path.exists() and self.encryption_key:
            self._load_encrypted_secrets(encrypted_path)
        
        # 4. Load Google credentials if exists
        google_creds = self.secrets_path / "google_credentials.json"
        if google_creds.exists():
            self._secrets['GOOGLE_CREDENTIALS'] = json.loads(google_creds.read_text())
        
        self._loaded = True
    
    def _load_encrypted_secrets(self, path: Path):
        """Load and decrypt secrets file"""
        try:
            fernet = Fernet(self.encryption_key.encode())
            encrypted_data = path.read_bytes()
            decrypted_data = fernet.decrypt(encrypted_data)
            secrets = json.loads(decrypted_data)
            self._secrets.update(secrets)
        except Exception as e:
            print(f"Warning: Could not load encrypted secrets: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a secret value"""
        return self._secrets.get(key, os.environ.get(key, default))
    
    def set(self, key: str, value: Any):
        """Set a secret value (in memory only)"""
        self._secrets[key] = value
        os.environ[key] = str(value)
    
    def get_all(self) -> Dict[str, Any]:
        """Get all non-sensitive secrets (for debugging)"""
        sensitive_keys = {
            'TOKEN', 'PASSWORD', 'SECRET', 'KEY', 'CREDENTIAL', 'API_KEY'
        }
        return {
            k: ('*' * 8 if any(s in k.upper() for s in sensitive_keys) else v)
            for k, v in self._secrets.items()
            if not k.startswith('_')
        }
    
    def save_encrypted(self, secrets: Dict[str, str], path: Optional[Path] = None):
        """Save secrets to encrypted file"""
        if not self.encryption_key:
            # Generate a new key
            self.encryption_key = Fernet.generate_key().decode()
            key_path = self.secrets_path / "encryption.key"
            key_path.write_text(self.encryption_key)
            print(f"Encryption key saved to {key_path}")
            print("IMPORTANT: Back up this key securely!")
        
        fernet = Fernet(self.encryption_key.encode())
        encrypted_data = fernet.encrypt(json.dumps(secrets).encode())
        
        save_path = path or (self.secrets_path / "secrets.encrypted")
        save_path.write_bytes(encrypted_data)
        print(f"Encrypted secrets saved to {save_path}")
    
    @property
    def github_token(self) -> Optional[str]:
        return self.get('GITHUB_TOKEN')
    
    @property
    def github_username(self) -> Optional[str]:
        return self.get('GITHUB_USERNAME')
    
    @property
    def database_url(self) -> str:
        return self.get('DATABASE_URL', 'postgresql://recovery:recovery_pass@localhost:5432/project_recovery')
    
    @property
    def argilla_api_url(self) -> str:
        return self.get('ARGILLA_API_URL', 'http://localhost:6900')
    
    @property
    def argilla_api_key(self) -> str:
        return self.get('ARGILLA_API_KEY', 'admin.apikey')
    
    @property
    def qdrant_url(self) -> str:
        return self.get('QDRANT_URL', 'http://localhost:6333')
    
    @property
    def redis_url(self) -> str:
        return self.get('REDIS_URL', 'redis://localhost:6379')
    
    @property
    def windows_username(self) -> str:
        return self.get('WINDOWS_USERNAME', os.environ.get('USERNAME', 'user'))
    
    @property
    def linux_username(self) -> str:
        return self.get('LINUX_USERNAME', os.environ.get('USER', 'user'))
    
    @property
    def google_credentials(self) -> Optional[Dict]:
        return self._secrets.get('GOOGLE_CREDENTIALS')


# Global instance
_secrets_manager: Optional[SecretsManager] = None


def get_secrets_manager() -> SecretsManager:
    """Get the global secrets manager instance"""
    global _secrets_manager
    if _secrets_manager is None:
        _secrets_manager = SecretsManager()
    return _secrets_manager


def get_secret(key: str, default: Any = None) -> Any:
    """Convenience function to get a secret"""
    return get_secrets_manager().get(key, default)


def load_all_secrets() -> Dict[str, Any]:
    """Load and return all secrets"""
    return get_secrets_manager().get_all()

Python

# secrets/setup_secrets.py
"""
Interactive script to set up secrets
"""
import os
import sys
from pathlib import Path
from getpass import getpass

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich.table import Table

console = Console()


def setup_secrets():
    """Interactive secrets setup"""
    console.print(Panel.fit(
        "[bold blue]🔐 Project Recovery - Secrets Setup[/bold blue]\n"
        "This will help you configure all required secrets",
        border_style="blue"
    ))
    
    secrets = {}
    env_lines = []
    
    # GitHub
    console.print("\n[bold cyan]1. GitHub Configuration[/bold cyan]")
    console.print("Get your token from: https://github.com/settings/tokens")
    console.print("Required scopes: repo, gist, read:user\n")
    
    secrets['GITHUB_TOKEN'] = getpass("GitHub Token: ")
    secrets['GITHUB_USERNAME'] = Prompt.ask("GitHub Username")
    
    # Windows/Linux usernames
    console.print("\n[bold cyan]2. System Usernames[/bold cyan]")
    default_win = os.environ.get('USERNAME', 'user')
    default_linux = os.environ.get('USER', 'user')
    
    secrets['WINDOWS_USERNAME'] = Prompt.ask("Windows Username", default=default_win)
    secrets['LINUX_USERNAME'] = Prompt.ask("Linux Username", default=default_linux)
    
    # Database
    console.print("\n[bold cyan]3. Database Configuration[/bold cyan]")
    if Confirm.ask("Use default database settings?", default=True):
        secrets['POSTGRES_USER'] = 'recovery'
        secrets['POSTGRES_PASSWORD'] = 'recovery_pass'
        secrets['POSTGRES_DB'] = 'project_recovery'
    else:
        secrets['POSTGRES_USER'] = Prompt.ask("Postgres User", default="recovery")
        secrets['POSTGRES_PASSWORD'] = getpass("Postgres Password: ")
        secrets['POSTGRES_DB'] = Prompt.ask("Database Name", default="project_recovery")
    
    secrets['DATABASE_URL'] = f"postgresql://{secrets['POSTGRES_USER']}:{secrets['POSTGRES_PASSWORD']}@localhost:5432/{secrets['POSTGRES_DB']}"
    
    # Google Drive (optional)
    console.print("\n[bold cyan]4. Google Drive (Optional)[/bold cyan]")
    if Confirm.ask("Configure Google Drive access?", default=False):
        console.print("Place your google_credentials.json in ./secrets/")
        secrets['GOOGLE_CREDENTIALS_PATH'] = './secrets/google_credentials.json'
    
    # Email (optional)
    console.print("\n[bold cyan]5. Email/IMAP (Optional)[/bold cyan]")
    if Confirm.ask("Configure email access for attachment scanning?", default=False):
        secrets['EMAIL_ADDRESS'] = Prompt.ask("Email Address")
        secrets['EMAIL_PASSWORD'] = getpass("Email Password/App Password: ")
        secrets['IMAP_SERVER'] = Prompt.ask("IMAP Server", default="imap.gmail.com")
    
    # Default services
    secrets['ARGILLA_API_URL'] = 'http://localhost:6900'
    secrets['ARGILLA_API_KEY'] = 'admin.apikey'
    secrets['ARGILLA_WORKSPACE'] = 'project_recovery'
    secrets['QDRANT_URL'] = 'http://localhost:6333'
    secrets['QDRANT_COLLECTION'] = 'project_fragments'
    secrets['REDIS_URL'] = 'redis://localhost:6379'
    secrets['EMBEDDING_MODEL'] = 'all-MiniLM-L6-v2'
    secrets['CHUNK_SIZE'] = '1000'
    secrets['CHUNK_OVERLAP'] = '200'
    secrets['SCRAPE_INTERVAL_HOURS'] = '6'
    secrets['LOG_LEVEL'] = 'INFO'
    
    # Generate .env file
    console.print("\n[bold green]Generating .env file...[/bold green]")
    
    env_content = """# ============================================
# PROJECT RECOVERY SYSTEM - SECRETS
# Generated by setup_secrets.py
# ============================================

# GitHub
GITHUB_TOKEN={GITHUB_TOKEN}
GITHUB_USERNAME={GITHUB_USERNAME}

# System Users
WINDOWS_USERNAME={WINDOWS_USERNAME}
LINUX_USERNAME={LINUX_USERNAME}

# Database
DATABASE_URL={DATABASE_URL}
POSTGRES_USER={POSTGRES_USER}
POSTGRES_PASSWORD={POSTGRES_PASSWORD}
POSTGRES_DB={POSTGRES_DB}

# Argilla
ARGILLA_API_URL={ARGILLA_API_URL}
ARGILLA_API_KEY={ARGILLA_API_KEY}
ARGILLA_WORKSPACE={ARGILLA_WORKSPACE}

# Vector Store
QDRANT_URL={QDRANT_URL}
QDRANT_COLLECTION={QDRANT_COLLECTION}

# Redis
REDIS_URL={REDIS_URL}

# Processing
EMBEDDING_MODEL={EMBEDDING_MODEL}
CHUNK_SIZE={CHUNK_SIZE}
CHUNK_OVERLAP={CHUNK_OVERLAP}
SCRAPE_INTERVAL_HOURS={SCRAPE_INTERVAL_HOURS}
LOG_LEVEL={LOG_LEVEL}
""".format(**secrets)
    
    # Add optional configs
    if 'GOOGLE_CREDENTIALS_PATH' in secrets:
        env_content += f"\n# Google Drive\nGOOGLE_CREDENTIALS_PATH={secrets['GOOGLE_CREDENTIALS_PATH']}\n"
    
    if 'EMAIL_ADDRESS' in secrets:
        env_content += f"""
# Email
EMAIL_ADDRESS={secrets['EMAIL_ADDRESS']}
EMAIL_PASSWORD={secrets['EMAIL_PASSWORD']}
IMAP_SERVER={secrets['IMAP_SERVER']}
"""
    
    # Write .env file
    env_path = Path('.env')
    env_path.write_text(env_content)
    
    console.print(f"\n[green]✓ Secrets saved to {env_path}[/green]")
    
    # Show summary
    table = Table(title="Configuration Summary")
    table.add_column("Setting", style="cyan")
    table.add_column("Value", style="green")
    
    for key, value in secrets.items():
        if 'PASSWORD' in key or 'TOKEN' in key or 'SECRET' in key:
            display_value = '*' * 8
        else:
            display_value = str(value)[:50]
        table.add_row(key, display_value)
    
    console.print(table)
    
    console.print("\n[yellow]⚠️  IMPORTANT:[/yellow]")
    console.print("  1. Never commit .env to version control")
    console.print("  2. Back up your secrets securely")
    console.print("  3. Add .env to .gitignore")
    
    return secrets


if __name__ == "__main__":
    setup_secrets()

8. Git Ignore

gitignore

# .gitignore

# ============================================
# SECRETS - NEVER COMMIT THESE
# ============================================
.env
.env.local
.env.*.local
secrets/
!secrets/.gitkeep
*.pem
*.key
*credentials*.json
*secret*
!.env.example

# ============================================
# PYTHON
# ============================================
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
.venv/
ENV/
env/

# ============================================
# IDE
# ============================================
.idea/
*.swp
*.swo
*~
.project
.pydevproject
.settings/
*.sublime-workspace

# VS Code - keep settings but not personal
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json

# ============================================
# DATA & OUTPUTS
# ============================================
data/
exports/
logs/
*.log
*.csv
*.sqlite
*.db

# ============================================
# CACHE
# ============================================
.cache/
.pytest_cache/
.mypy_cache/
.ruff_cache/
*.pyc
htmlcov/
.coverage
.coverage.*
coverage.xml
*.cover

# ============================================
# OS
# ============================================
.DS_Store
Thumbs.db
desktop.ini
*.lnk

# ============================================
# DOCKER
# ============================================
docker-compose.override.yml

# ============================================
# MISC
# ============================================
*.bak
*.tmp
*.temp

9. Helper Scripts

Python

# run_source.py
"""
Run a single source scraper
Usage: python run_source.py <source_name>
"""
import sys
import asyncio
from rich.console import Console
from orchestrator.pipeline import RecoveryPipeline

console = Console()


async def main():
    if len(sys.argv) < 2:
        console.print("[red]Usage: python run_source.py <source_name>[/red]")
        console.print("Available sources: github, local_drives, rstudio, linux_system, lmarena")
        sys.exit(1)
    
    source_name = sys.argv[1]
    
    console.print(f"[bold blue]Running source: {source_name}[/bold blue]")
    
    pipeline = RecoveryPipeline()
    result = await pipeline.run_single_source(source_name)
    
    console.print(f"\n[green]Results:[/green]")
    console.print(f"  Items found: {result.get('items_found', 0)}")
    console.print(f"  Items processed: {result.get('items_processed', 0)}")
    
    if result.get('errors'):
        console.print(f"[yellow]  Errors: {len(result['errors'])}[/yellow]")
        for err in result['errors']:
            console.print(f"    - {err}")


if __name__ == "__main__":
    asyncio.run(main())

Python

# search.py
"""
Interactive search through recovered data
"""
import asyncio
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from orchestrator.pipeline import RecoveryPipeline

console = Console()


async def main():
    console.print(Panel.fit(
        "[bold blue]🔍 Project Recovery Search[/bold blue]",
        border_style="blue"
    ))
    
    pipeline = RecoveryPipeline()
    
    while True:
        query = Prompt.ask("\n[cyan]Search query[/cyan] (or 'quit' to exit)")
        
        if query.lower() in ['quit', 'exit', 'q']:
            break
        
        results = pipeline.search(query, limit=10)
        
        if not results:
            console.print("[yellow]No results found[/yellow]")
            continue
        
        console.print(f"\n[green]Found {len(results)} results:[/green]\n")
        
        for i, result in enumerate(results, 1):
            score = result.get('score', 0)
            filename = result.get('filename', 'Unknown')
            source = result.get('source_type', 'unknown')
            language = result.get('language', 'text')
            content = result.get('content', '')[:500]
            
            console.print(Panel(
                f"[bold]{filename}[/bold] ({source})\n"
                f"Score: {score:.3f} | Language: {language}\n\n"
                f"{content}{'...' if len(result.get('content', '')) > 500 else ''}",
                title=f"Result {i}",
                border_style="blue"
            ))
            console.print()


if __name__ == "__main__":
    asyncio.run(main())

Python

# export.py
"""
Export curated data from Argilla
"""
import asyncio
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt, Confirm
from argilla_integration.datasets import ArgillaManager
from config.settings import settings

console = Console()


async def main():
    console.print("[bold blue]📤 Export Curated Data[/bold blue]\n")
    
    argilla = ArgillaManager(
        api_url=settings.argilla_api_url,
        api_key=settings.argilla_api_key,
        workspace=settings.argilla_workspace
    )
    
    # Get dataset name
    dataset_name = Prompt.ask("Dataset name", default="recovery_latest")
    
    # Get export path
    default_path = f"./exports/{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    export_path = Prompt.ask("Export path", default=default_path)
    
    # Get filter
    actions = ['include_as_is', 'needs_update', 'reference_only']
    console.print("\nAvailable actions:", actions)
    selected = Prompt.ask(
        "Filter by action (comma-separated)", 
        default="include_as_is,needs_update"
    )
    filter_actions = [a.strip() for a in selected.split(',')]
    
    try:
        count = argilla.export_curated_data(
            dataset_name,
            export_path,
            filter_actions
        )
        console.print(f"\n[green]✓ Exported {count} items to {export_path}[/green]")
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")


if __name__ == "__main__":
    asyncio.run(main())

Quick Setup Commands

PowerShell

# PowerShell - Windows Setup

# 1. Create project directory
mkdir project-recovery
cd project-recovery

# 2. Create virtual environment
python -m venv venv
.\venv\Scripts\Activate

# 3. Create directory structure
mkdir .vscode, config, scrapers, processors, storage, argilla_integration, orchestrator, api, ui, secrets, tests, logs, data, exports

# 4. Create placeholder files
New-Item -ItemType File -Path "secrets\.gitkeep"
New-Item -ItemType File -Path "logs\.gitkeep"
New-Item -ItemType File -Path "data\.gitkeep"
New-Item -ItemType File -Path "exports\.gitkeep"

# 5. Install dependencies
pip install -r requirements.txt

# 6. Run secrets setup
python secrets/setup_secrets.py

# 7. Run source configuration
python setup_sources.py

# 8. Start Docker services
docker-compose up -d

# 9. Open VS Code
code project-recovery.code-workspace

Now open VS Code, and you'll have:

    F5 - Run the debugger with various configurations
    Ctrl+Shift+P → "Tasks: Run Task" - Quick access to all tasks
    Ctrl+Shift+D - Debug panel with all launch configurations
    All secrets in .env file (ignored by git)
    Interactive setup scripts for configuration

Would you like me to add anything else to the VS Code setup?

wrire me a visual studio cote and will put all secrets inside
claude-opus-4-5-20251101-thinking-32k
Complete Configuration for Your Specific Sources

Let me set up scrapers for all your specific locations:
1. Updated Sources Configuration

YAML

# config/sources.yaml
# ============================================
# PROJECT RECOVERY - YOUR SPECIFIC SOURCES
# ============================================

project_info:
  name: "Your Lost Project"
  description: "Recovering project data from multiple sources"
  
# Keywords and patterns to identify YOUR project
project_keywords:
  # Add your specific project identifiers
  - "your_project_name"
  - "your_unique_function_names"
  - "your_package_name"
  - "specific_variable_names"
  - "your_username"
  # Add any unique strings from your code
  
file_signatures:
  - pattern: "# Your Copyright Header"
    type: source_code
    weight: 2.0
  - pattern: "your.email@domain.com"
    type: any
    weight: 1.5
  # Add unique patterns from your files

# ============================================
# SOURCE CONFIGURATIONS
# ============================================

sources:
  # ------------------------------------------
  # 1. GITHUB
  # ------------------------------------------
  github:
    enabled: true
    
    # Your specific repositories
    repositories:
      - owner: "YOUR_GITHUB_USERNAME"
        repo: "repo-name-1"
      - owner: "YOUR_GITHUB_USERNAME"
        repo: "repo-name-2"
      # Add all your repos
      
    # Search for your code across GitHub
    search_queries:
      - "user:YOUR_GITHUB_USERNAME"
      - "your_unique_function_name"
      - "your_project_identifier"
      
    # Include your gists
    include_gists: true
    
    # Include forked repos
    include_forks: true
    
    # Also check starred repos (might have forked your own)
    include_starred: true
    
    # Check organizations you belong to
    organizations:
      - "your-org-name"
      
  # ------------------------------------------
  # 2. LOCAL DRIVES (Windows)
  # ------------------------------------------
  local_drives:
    enabled: true
    
    # Windows drives to scan
    windows_paths:
      # Main drives
      - "C:/Users/YOUR_USERNAME/Documents"
      - "C:/Users/YOUR_USERNAME/Desktop"
      - "C:/Users/YOUR_USERNAME/Downloads"
      - "C:/Users/YOUR_USERNAME/Projects"
      - "C:/Users/YOUR_USERNAME/Code"
      - "C:/Users/YOUR_USERNAME/dev"
      - "C:/Users/YOUR_USERNAME/workspace"
      
      # Other drives
      - "D:/"
      - "E:/"
      - "F:/"
      
      # Common development locations
      - "C:/dev"
      - "C:/projects"
      - "C:/code"
      - "C:/repos"
      - "C:/git"
      
      # AppData locations (IDE settings, cached data)
      - "C:/Users/YOUR_USERNAME/AppData/Local"
      - "C:/Users/YOUR_USERNAME/AppData/Roaming"
      
      # VSCode workspace storage
      - "C:/Users/YOUR_USERNAME/AppData/Roaming/Code/User/workspaceStorage"
      
      # Temp and recovery locations
      - "C:/Users/YOUR_USERNAME/AppData/Local/Temp"
      - "C:/Recovery"
      
    # File patterns to include
    include_patterns:
      # Source code
      - "*.py"
      - "*.r"
      - "*.R"
      - "*.Rmd"
      - "*.rmd"
      - "*.js"
      - "*.ts"
      - "*.jsx"
      - "*.tsx"
      - "*.java"
      - "*.cpp"
      - "*.c"
      - "*.h"
      - "*.go"
      - "*.rs"
      - "*.rb"
      - "*.php"
      - "*.swift"
      - "*.kt"
      - "*.scala"
      - "*.sh"
      - "*.bash"
      - "*.zsh"
      - "*.ps1"
      - "*.sql"
      
      # Web
      - "*.html"
      - "*.htm"
      - "*.css"
      - "*.scss"
      - "*.sass"
      - "*.vue"
      - "*.svelte"
      
      # Config
      - "*.json"
      - "*.yaml"
      - "*.yml"
      - "*.toml"
      - "*.ini"
      - "*.cfg"
      - "*.conf"
      - "*.env"
      - "*.env.*"
      - ".env*"
      - "*.xml"
      
      # Documentation
      - "*.md"
      - "*.rst"
      - "*.txt"
      - "*.doc"
      - "*.docx"
      - "*.pdf"
      - "README*"
      - "CHANGELOG*"
      - "LICENSE*"
      
      # Data
      - "*.csv"
      - "*.tsv"
      - "*.parquet"
      
      # Notebooks
      - "*.ipynb"
      
      # Project files
      - "*.Rproj"
      - "*.sln"
      - "*.csproj"
      - "Makefile"
      - "Dockerfile"
      - "docker-compose*.yml"
      - "package.json"
      - "requirements.txt"
      - "Pipfile"
      - "pyproject.toml"
      - "Cargo.toml"
      - "go.mod"
      
    # Patterns to exclude
    exclude_patterns:
      - "node_modules/*"
      - "__pycache__/*"
      - ".git/objects/*"
      - "*.pyc"
      - "*.pyo"
      - ".venv/*"
      - "venv/*"
      - "env/*"
      - ".env/*"
      - "vendor/*"
      - "dist/*"
      - "build/*"
      - "target/*"
      - "*.min.js"
      - "*.min.css"
      - "*.map"
      - "*.lock"
      - "package-lock.json"
      - "yarn.lock"
      - "*.log"
      - "*.tmp"
      - "*.temp"
      - "*.cache"
      - "Windows/*"
      - "Program Files/*"
      - "Program Files (x86)/*"
      - "$Recycle.Bin/*"
      - "System Volume Information/*"
      
  # ------------------------------------------
  # 3. R STUDIO RESTORED DATA
  # ------------------------------------------
  rstudio_restored:
    enabled: true
    
    # Specify your R Studio restored data folder
    paths:
      - "C:/Users/YOUR_USERNAME/RStudio-Restored"
      - "D:/RStudio-Backup"
      - "E:/Recovered/RStudio"
      # Add your actual path here
      
    # R-specific file patterns
    include_patterns:
      - "*.R"
      - "*.r"
      - "*.Rmd"
      - "*.rmd"
      - "*.Rnw"
      - "*.Rproj"
      - "*.RData"
      - "*.rda"
      - "*.rds"
      - "*.Rhistory"
      - ".Rprofile"
      - ".Renviron"
      - "*.Rproj.user/*"
      - "DESCRIPTION"
      - "NAMESPACE"
      - "*.Rd"
      
    # Also capture related files
    related_patterns:
      - "*.csv"
      - "*.xlsx"
      - "*.xls"
      - "*.sav"  # SPSS
      - "*.dta"  # Stata
      - "*.sas7bdat"  # SAS
      - "*.json"
      - "*.yaml"
      - "*.md"
      
    # RStudio specific locations
    rstudio_config_paths:
      - "C:/Users/YOUR_USERNAME/AppData/Local/RStudio"
      - "C:/Users/YOUR_USERNAME/AppData/Roaming/RStudio"
      - "C:/Users/YOUR_USERNAME/.rstudio-desktop"
      - "~/.local/share/rstudio"
      
  # ------------------------------------------
  # 4. LINUX SYSTEM ON DRIVE
  # ------------------------------------------
  linux_system:
    enabled: true
    
    # Linux partition paths (when mounted on Windows)
    # Using WSL or mounted Linux partition
    mounted_paths:
      # WSL paths
      - "\\\\wsl$\\Ubuntu\\home\\YOUR_LINUX_USERNAME"
      - "\\\\wsl.localhost\\Ubuntu\\home\\YOUR_LINUX_USERNAME"
      
      # Or if you have a mounted Linux partition
      - "L:/"  # If mounted as L: drive
      - "X:/home/YOUR_USERNAME"
      
      # Or direct Linux paths if running on Linux
      - "/home/YOUR_LINUX_USERNAME"
      - "/home/YOUR_LINUX_USERNAME/projects"
      - "/home/YOUR_LINUX_USERNAME/code"
      - "/home/YOUR_LINUX_USERNAME/dev"
      - "/home/YOUR_LINUX_USERNAME/Documents"
      - "/home/YOUR_LINUX_USERNAME/.config"
      - "/home/YOUR_LINUX_USERNAME/.local/share"
      - "/opt/projects"
      - "/var/www"
      - "/srv"
      
    # Linux-specific config locations to check
    config_locations:
      - "/home/YOUR_LINUX_USERNAME/.bashrc"
      - "/home/YOUR_LINUX_USERNAME/.zshrc"
      - "/home/YOUR_LINUX_USERNAME/.profile"
      - "/home/YOUR_LINUX_USERNAME/.gitconfig"
      - "/home/YOUR_LINUX_USERNAME/.ssh/config"
      - "/home/YOUR_LINUX_USERNAME/.config"
      
    # Check these directories for project data
    deep_scan_paths:
      - "/home/YOUR_LINUX_USERNAME/projects"
      - "/home/YOUR_LINUX_USERNAME/workspace"
      - "/home/YOUR_LINUX_USERNAME/repos"
      - "/home/YOUR_LINUX_USERNAME/git"
      
  # ------------------------------------------
  # 5. LM ARENA CHAT LOGS
  # ------------------------------------------
  lmarena_chatlogs:
    enabled: true
    
    # Browser storage locations
    browser_data_paths:
      # Chrome
      - "C:/Users/YOUR_USERNAME/AppData/Local/Google/Chrome/User Data/Default/Local Storage"
      - "C:/Users/YOUR_USERNAME/AppData/Local/Google/Chrome/User Data/Default/IndexedDB"
      - "C:/Users/YOUR_USERNAME/AppData/Local/Google/Chrome/User Data/Default/Session Storage"
      
      # Firefox
      - "C:/Users/YOUR_USERNAME/AppData/Roaming/Mozilla/Firefox/Profiles"
      
      # Edge
      - "C:/Users/YOUR_USERNAME/AppData/Local/Microsoft/Edge/User Data/Default/Local Storage"
      
      # Linux browsers
      - "/home/YOUR_LINUX_USERNAME/.config/google-chrome/Default/Local Storage"
      - "/home/YOUR_LINUX_USERNAME/.mozilla/firefox"
      
    # If you exported chat logs, specify location
    exported_chats_path:
      - "C:/Users/YOUR_USERNAME/Downloads"
      - "C:/Users/YOUR_USERNAME/Documents/LMArena"
      - "D:/Backups/ChatLogs"
      
    # File patterns for chat exports
    chat_patterns:
      - "*lmarena*"
      - "*chatbot-arena*"
      - "*chat*.json"
      - "*conversation*.json"
      - "*chat*.txt"
      - "*chat*.md"
      - "*llm-chat*"
      
    # LM Arena specific
    lmarena_domains:
      - "chat.lmsys.org"
      - "arena.lmsys.org"
      - "lmarena.ai"

2. Enhanced Scrapers for Your Sources

Python

# scrapers/local_drives_scraper.py
"""
Enhanced scraper for local drives with deep scanning
"""
import asyncio
import aiofiles
import os
import platform
from pathlib import Path
from datetime import datetime
from typing import AsyncIterator, Dict, Any, List, Set
import fnmatch
import chardet
import subprocess
from .base import BaseScraper, ScrapedItem, SourceType, ContentType


class LocalDrivesScraper(BaseScraper):
    """Comprehensive local drives scraper"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.is_windows = platform.system() == "Windows"
        self.scanned_paths: Set[str] = set()
        self.max_file_size = 10 * 1024 * 1024  # 10MB max
        
    @property
    def source_type(self) -> SourceType:
        return SourceType.LOCAL_FILESYSTEM
    
    async def validate_connection(self) -> bool:
        return True
    
    def get_all_drives(self) -> List[str]:
        """Get all available drives on Windows"""
        drives = []
        if self.is_windows:
            import string
            for letter in string.ascii_uppercase:
                drive = f"{letter}:/"
                if os.path.exists(drive):
                    drives.append(drive)
        else:
            drives = ["/"]
        return drives
    
    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        """Scrape all configured local drive locations"""
        config = self.config.get("sources", {}).get("local_drives", {})
        
        if not config.get("enabled", False):
            return
        
        paths = config.get("windows_paths", []) if self.is_windows else config.get("linux_paths", [])
        include_patterns = config.get("include_patterns", ["*"])
        exclude_patterns = config.get("exclude_patterns", [])
        
        for base_path in paths:
            # Handle Windows path conversion
            if self.is_windows and base_path.startswith("/"):
                continue
            if not self.is_windows and base_path[1:3] == ":/":
                continue
                
            path = Path(base_path)
            
            if not path.exists():
                print(f"[LocalDrives] Path does not exist: {base_path}")
                continue
            
            print(f"[LocalDrives] Scanning: {base_path}")
            
            async for item in self._scan_directory(path, include_patterns, exclude_patterns):
                yield item
    
    async def _scan_directory(
        self,
        base_path: Path,
        include_patterns: List[str],
        exclude_patterns: List[str]
    ) -> AsyncIterator[ScrapedItem]:
        """Recursively scan a directory"""
        try:
            for root, dirs, files in os.walk(base_path, followlinks=False):
                # Skip if we've seen this path (handle symlinks)
                real_root = os.path.realpath(root)
                if real_root in self.scanned_paths:
                    continue
                self.scanned_paths.add(real_root)
                
                # Filter directories
                dirs[:] = [d for d in dirs if not self._should_exclude_dir(d, exclude_patterns)]
                
                for filename in files:
                    filepath = Path(root) / filename
                    
                    # Check patterns
                    if not self._matches_patterns(filename, include_patterns):
                        continue
                    
                    if self._should_exclude(filepath, base_path, exclude_patterns):
                        continue
                    
                    try:
                        item = await self._process_file(filepath)
                        if item:
                            yield item
                    except Exception as e:
                        print(f"[LocalDrives] Error processing {filepath}: {e}")
                        
                # Yield control periodically
                await asyncio.sleep(0)
                
        except PermissionError:
            print(f"[LocalDrives] Permission denied: {base_path}")
        except Exception as e:
            print(f"[LocalDrives] Error scanning {base_path}: {e}")
    
    def _should_exclude_dir(self, dirname: str, exclude_patterns: List[str]) -> bool:
        """Check if directory should be excluded"""
        # Always skip these
        skip_dirs = {
            'node_modules', '__pycache__', '.git', '.svn', '.hg',
            'venv', '.venv', 'env', '.env', 'virtualenv',
            'vendor', 'dist', 'build', 'target', 'bin', 'obj',
            '.idea', '.vscode', '.vs',
            'Windows', 'Program Files', 'Program Files (x86)',
            '$Recycle.Bin', 'System Volume Information', 'Recovery',
            'ProgramData', 'AppData'  # We scan AppData selectively
        }
        
        if dirname in skip_dirs:
            return True
        
        if dirname.startswith('.') and dirname not in ['.config', '.local', '.rstudio-desktop']:
            return True
            
        for pattern in exclude_patterns:
            if fnmatch.fnmatch(dirname, pattern.rstrip('/*')):
                return True
                
        return False
    
    def _matches_patterns(self, filename: str, patterns: List[str]) -> bool:
        """Check if filename matches any include pattern"""
        return any(fnmatch.fnmatch(filename.lower(), p.lower()) for p in patterns)
    
    def _should_exclude(self, filepath: Path, base_path: Path, exclude_patterns: List[str]) -> bool:
        """Check if file should be excluded"""
        try:
            rel_path = str(filepath.relative_to(base_path))
            return any(fnmatch.fnmatch(rel_path, p) for p in exclude_patterns)
        except ValueError:
            return False
    
    async def _process_file(self, filepath: Path) -> ScrapedItem | None:
        """Process a single file"""
        try:
            stat = filepath.stat()
            
            # Skip files that are too large
            if stat.st_size > self.max_file_size:
                return None
            
            # Skip empty files
            if stat.st_size == 0:
                return None
            
            # Read file
            async with aiofiles.open(filepath, 'rb') as f:
                raw_content = await f.read()
            
            # Skip binary files
            if b'\x00' in raw_content[:8192]:
                return None
            
            # Detect encoding
            detected = chardet.detect(raw_content[:10000])
            encoding = detected.get('encoding', 'utf-8') or 'utf-8'
            
            try:
                content = raw_content.decode(encoding)
            except (UnicodeDecodeError, LookupError):
                content = raw_content.decode('utf-8', errors='ignore')
            
            # Check relevance
            is_relevant, confidence = self.is_relevant(content, filepath.name)
            
            # Lower threshold for local files since they're more likely relevant
            if not is_relevant and confidence < 0.05:
                return None
            
            return ScrapedItem(
                id=f"local:{filepath.as_posix()}",
                source_type=self.source_type,
                source_path=str(filepath.absolute()),
                content=content,
                content_type=self.detect_content_type(content, filepath.name),
                file_extension=filepath.suffix.lstrip('.') if filepath.suffix else None,
                filename=filepath.name,
                metadata={
                    "absolute_path": str(filepath.absolute()),
                    "drive": str(filepath.drive) if self.is_windows else "/",
                    "encoding": encoding,
                    "size_bytes": stat.st_size
                },
                created_at=datetime.fromtimestamp(stat.st_ctime),
                modified_at=datetime.fromtimestamp(stat.st_mtime),
                size_bytes=stat.st_size,
                language=self.detect_language(content, filepath.name),
                confidence_score=confidence if is_relevant else confidence + 0.1
            )
            
        except Exception as e:
            return None

Python

# scrapers/rstudio_scraper.py
"""
R Studio specific data scraper
"""
import asyncio
import aiofiles
import json
import os
from pathlib import Path
from datetime import datetime
from typing import AsyncIterator, Dict, Any, List
import re
from .base import BaseScraper, ScrapedItem, SourceType, ContentType


class RStudioScraper(BaseScraper):
    """Specialized scraper for R Studio projects and data"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        
    @property
    def source_type(self) -> SourceType:
        return SourceType.LOCAL_FILESYSTEM
    
    async def validate_connection(self) -> bool:
        return True
    
    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        """Scrape R Studio data"""
        config = self.config.get("sources", {}).get("rstudio_restored", {})
        
        if not config.get("enabled", False):
            return
        
        # Main restored data paths
        for path in config.get("paths", []):
            if Path(path).exists():
                print(f"[RStudio] Scanning restored data: {path}")
                async for item in self._scan_rstudio_folder(Path(path)):
                    yield item
        
        # RStudio config paths
        for path in config.get("rstudio_config_paths", []):
            expanded = os.path.expanduser(path)
            if Path(expanded).exists():
                print(f"[RStudio] Scanning config: {expanded}")
                async for item in self._scan_rstudio_config(Path(expanded)):
                    yield item
    
    async def _scan_rstudio_folder(self, base_path: Path) -> AsyncIterator[ScrapedItem]:
        """Scan R Studio project folder"""
        r_patterns = {
            '*.R', '*.r', '*.Rmd', '*.rmd', '*.Rnw',
            '*.Rproj', 'DESCRIPTION', 'NAMESPACE', '*.Rd',
            '.Rprofile', '.Renviron', '*.Rhistory'
        }
        
        data_patterns = {'*.RData', '*.rda', '*.rds'}
        
        for root, dirs, files in os.walk(base_path):
            # Skip hidden and system directories, but not .Rproj.user
            dirs[:] = [d for d in dirs if not d.startswith('.') or d == '.Rproj.user']
            
            for filename in files:
                filepath = Path(root) / filename
                
                # Check if it's an R file
                is_r_file = any(filepath.match(p) for p in r_patterns)
                is_data_file = any(filepath.match(p) for p in data_patterns)
                
                if is_r_file:
                    item = await self._process_r_file(filepath)
                    if item:
                        yield item
                elif is_data_file:
                    item = await self._process_rdata_file(filepath)
                    if item:
                        yield item
                        
            await asyncio.sleep(0)
    
    async def _process_r_file(self, filepath: Path) -> ScrapedItem | None:
        """Process an R source file"""
        try:
            async with aiofiles.open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = await f.read()
            
            stat = filepath.stat()
            
            # Extract R-specific metadata
            metadata = self._extract_r_metadata(content, filepath.name)
            
            # Check relevance
            is_relevant, confidence = self.is_relevant(content, filepath.name)
            
            return ScrapedItem(
                id=f"rstudio:{filepath.as_posix()}",
                source_type=self.source_type,
                source_path=str(filepath.absolute()),
                content=content,
                content_type=ContentType.SOURCE_CODE,
                file_extension=filepath.suffix.lstrip('.'),
                filename=filepath.name,
                metadata={
                    **metadata,
                    "is_rmarkdown": filepath.suffix.lower() in ['.rmd', '.rnw'],
                    "is_package_file": filepath.name in ['DESCRIPTION', 'NAMESPACE'],
                    "absolute_path": str(filepath.absolute())
                },
                created_at=datetime.fromtimestamp(stat.st_ctime),
                modified_at=datetime.fromtimestamp(stat.st_mtime),
                language="r",
                confidence_score=confidence if is_relevant else 0.5  # R files are valuable
            )
            
        except Exception as e:
            print(f"[RStudio] Error processing {filepath}: {e}")
            return None
    
    async def _process_rdata_file(self, filepath: Path) -> ScrapedItem | None:
        """Process RData/RDS files - extract metadata without full loading"""
        try:
            stat = filepath.stat()
            
            # We can't easily read RData in Python, but we can record its existence
            content = f"""# R Data File: {filepath.name}
# Size: {stat.st_size} bytes
# Modified: {datetime.fromtimestamp(stat.st_mtime)}
# Path: {filepath.absolute()}

# To load this file in R:
# load("{filepath.absolute()}")  # for .RData/.rda
# readRDS("{filepath.absolute()}")  # for .rds
"""
            
            return ScrapedItem(
                id=f"rstudio:data:{filepath.as_posix()}",
                source_type=self.source_type,
                source_path=str(filepath.absolute()),
                content=content,
                content_type=ContentType.DATA,
                file_extension=filepath.suffix.lstrip('.'),
                filename=filepath.name,
                metadata={
                    "is_rdata": True,
                    "size_bytes": stat.st_size,
                    "absolute_path": str(filepath.absolute())
                },
                created_at=datetime.fromtimestamp(stat.st_ctime),
                modified_at=datetime.fromtimestamp(stat.st_mtime),
                language="r",
                confidence_score=0.7
            )
            
        except Exception as e:
            return None
    
    def _extract_r_metadata(self, content: str, filename: str) -> Dict[str, Any]:
        """Extract metadata from R code"""
        metadata = {
            "libraries": [],
            "functions_defined": [],
            "data_files_referenced": []
        }
        
        # Find library/require calls
        lib_pattern = r'(?:library|require)\s*\(\s*["\']?(\w+)["\']?\s*\)'
        metadata["libraries"] = list(set(re.findall(lib_pattern, content)))
        
        # Find function definitions
        func_pattern = r'^(\w+)\s*<-\s*function\s*\('
        metadata["functions_defined"] = re.findall(func_pattern, content, re.MULTILINE)
        
        # Find data file references
        file_pattern = r'["\']([^"\']+\.(?:csv|xlsx?|rds|RData|rda|sav|dta|json))["\']'
        metadata["data_files_referenced"] = list(set(re.findall(file_pattern, content, re.IGNORECASE)))
        
        # Check for Shiny
        if 'shinyApp' in content or 'shinyServer' in content or 'shinyUI' in content:
            metadata["is_shiny_app"] = True
            
        # Check for package development
        if filename == "DESCRIPTION":
            metadata["is_package"] = True
            # Parse DESCRIPTION
            for line in content.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[f"pkg_{key.strip().lower()}"] = value.strip()
        
        return metadata
    
    async def _scan_rstudio_config(self, config_path: Path) -> AsyncIterator[ScrapedItem]:
        """Scan RStudio configuration for project references"""
        try:
            # Look for project history and recent files
            interesting_files = [
                'rstudio-prefs.json',
                'monitored/lists/project_mru',
                'monitored/lists/file_mru'
            ]
            
            for rel_path in interesting_files:
                filepath = config_path / rel_path
                if filepath.exists():
                    async with aiofiles.open(filepath, 'r', errors='ignore') as f:
                        content = await f.read()
                    
                    yield ScrapedItem(
                        id=f"rstudio:config:{filepath.as_posix()}",
                        source_type=self.source_type,
                        source_path=str(filepath.absolute()),
                        content=content,
                        content_type=ContentType.CONFIGURATION,
                        filename=filepath.name,
                        metadata={
                            "config_type": "rstudio_settings",
                            "absolute_path": str(filepath.absolute())
                        },
                        language=None,
                        confidence_score=0.9
                    )
                    
        except Exception as e:
            print(f"[RStudio] Error scanning config: {e}")

Python

# scrapers/linux_system_scraper.py
"""
Linux system scraper - handles mounted Linux partitions and WSL
"""
import asyncio
import aiofiles
import os
import platform
from pathlib import Path, PureWindowsPath, PurePosixPath
from datetime import datetime
from typing import AsyncIterator, Dict, Any, List
import subprocess
from .base import BaseScraper, ScrapedItem, SourceType, ContentType


class LinuxSystemScraper(BaseScraper):
    """Scraper for Linux systems (including WSL and mounted partitions)"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.is_windows = platform.system() == "Windows"
        
    @property
    def source_type(self) -> SourceType:
        return SourceType.LOCAL_FILESYSTEM
    
    async def validate_connection(self) -> bool:
        """Check if Linux system is accessible"""
        config = self.config.get("sources", {}).get("linux_system", {})
        
        if self.is_windows:
            # Check WSL
            try:
                result = subprocess.run(
                    ['wsl', '--list', '--quiet'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                if result.returncode == 0 and result.stdout.strip():
                    return True
            except:
                pass
            
            # Check mounted paths
            for path in config.get("mounted_paths", []):
                if Path(path).exists():
                    return True
        else:
            # Native Linux
            return True
            
        return False
    
    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        """Scrape Linux system data"""
        config = self.config.get("sources", {}).get("linux_system", {})
        
        if not config.get("enabled", False):
            return
        
        if self.is_windows:
            # Try WSL first
            async for item in self._scrape_wsl(config):
                yield item
            
            # Then try mounted paths
            for mount_path in config.get("mounted_paths", []):
                if Path(mount_path).exists():
                    print(f"[Linux] Scanning mounted path: {mount_path}")
                    async for item in self._scan_linux_path(Path(mount_path)):
                        yield item
        else:
            # Native Linux
            for path in config.get("mounted_paths", []) + config.get("deep_scan_paths", []):
                expanded = os.path.expanduser(path)
                if Path(expanded).exists():
                    print(f"[Linux] Scanning: {expanded}")
                    async for item in self._scan_linux_path(Path(expanded)):
                        yield item
    
    async def _scrape_wsl(self, config: Dict) -> AsyncIterator[ScrapedItem]:
        """Scrape from WSL"""
        try:
            # Get list of WSL distributions
            result = subprocess.run(
                ['wsl', '--list', '--quiet'],
                capture_output=True,
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                return
            
            distros = [d.strip() for d in result.stdout.strip().split('\n') if d.strip()]
            
            for distro in distros:
                # Common paths to check in WSL
                wsl_paths = [
                    f"\\\\wsl$\\{distro}\\home",
                    f"\\\\wsl.localhost\\{distro}\\home",
                ]
                
                for wsl_path in wsl_paths:
                    path = Path(wsl_path)
                    if path.exists():
                        print(f"[Linux] Scanning WSL ({distro}): {wsl_path}")
                        async for item in self._scan_linux_path(path):
                            yield item
                        break
                        
        except subprocess.TimeoutExpired:
            print("[Linux] WSL command timed out")
        except FileNotFoundError:
            print("[Linux] WSL not available")
        except Exception as e:
            print(f"[Linux] WSL error: {e}")
    
    async def _scan_linux_path(self, base_path: Path) -> AsyncIterator[ScrapedItem]:
        """Scan a Linux path for project files"""
        include_patterns = [
            '*.py', '*.r', '*.R', '*.Rmd', '*.js', '*.ts', '*.go', '*.rs',
            '*.java', '*.cpp', '*.c', '*.h', '*.sh', '*.bash', '*.zsh',
            '*.md', '*.txt', '*.json', '*.yaml', '*.yml', '*.toml',
            '*.sql', '*.html', '*.css', 'Makefile', 'Dockerfile',
            '.bashrc', '.zshrc', '.profile', '.gitconfig',
            'requirements.txt', 'package.json', 'Cargo.toml', 'go.mod'
        ]
        
        exclude_dirs = {
            '.git', 'node_modules', '__pycache__', '.cache', '.local/share/Trash',
            'snap', '.npm', '.cargo/registry', '.rustup', 'go/pkg'
        }
        
        try:
            for root, dirs, files in os.walk(base_path, followlinks=False):
                # Filter directories
                dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith('.cache')]
                
                for filename in files:
                    filepath = Path(root) / filename
                    
                    # Check patterns
                    matches = any(
                        filepath.match(p) or filename == p.lstrip('*.')
                        for p in include_patterns
                    )
                    
                    if not matches:
                        continue
                    
                    try:
                        item = await self._process_linux_file(filepath)
                        if item:
                            yield item
                    except Exception as e:
                        pass
                        
                await asyncio.sleep(0)
                
        except PermissionError:
            print(f"[Linux] Permission denied: {base_path}")
        except Exception as e:
            print(f"[Linux] Error scanning {base_path}: {e}")
    
    async def _process_linux_file(self, filepath: Path) -> ScrapedItem | None:
        """Process a file from Linux system"""
        try:
            stat = filepath.stat()
            
            if stat.st_size > 5 * 1024 * 1024:  # 5MB limit
                return None
            
            if stat.st_size == 0:
                return None
            
            async with aiofiles.open(filepath, 'rb') as f:
                raw = await f.read()
            
            if b'\x00' in raw[:4096]:
                return None
            
            try:
                content = raw.decode('utf-8')
            except UnicodeDecodeError:
                content = raw.decode('utf-8', errors='ignore')
            
            is_relevant, confidence = self.is_relevant(content, filepath.name)
            
            # Linux config files are valuable
            is_config = filepath.name.startswith('.') or filepath.name in [
                'Makefile', 'Dockerfile', 'docker-compose.yml'
            ]
            
            if not is_relevant and confidence < 0.05 and not is_config:
                return None
            
            return ScrapedItem(
                id=f"linux:{filepath.as_posix()}",
                source_type=self.source_type,
                source_path=str(filepath),
                content=content,
                content_type=ContentType.CONFIGURATION if is_config else self.detect_content_type(content, filepath.name),
                file_extension=filepath.suffix.lstrip('.') if filepath.suffix else None,
                filename=filepath.name,
                metadata={
                    "linux_path": str(filepath),
                    "is_config_file": is_config,
                    "is_wsl": "wsl" in str(filepath).lower()
                },
                created_at=datetime.fromtimestamp(stat.st_ctime),
                modified_at=datetime.fromtimestamp(stat.st_mtime),
                language=self.detect_language(content, filepath.name),
                confidence_score=confidence if is_relevant else 0.3
            )
            
        except Exception as e:
            return None

Python

# scrapers/lmarena_scraper.py
"""
LM Arena chat logs scraper
"""
import asyncio
import aiofiles
import json
import os
import sqlite3
import re
from pathlib import Path
from datetime import datetime
from typing import AsyncIterator, Dict, Any, List, Optional
from .base import BaseScraper, ScrapedItem, SourceType, ContentType


class LMArenaLogsScraper(BaseScraper):
    """Scraper for LM Arena (LMSYS Chatbot Arena) chat logs"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        
    @property
    def source_type(self) -> SourceType:
        return SourceType.LOCAL_FILESYSTEM  # We'll use a custom sub-type in metadata
    
    async def validate_connection(self) -> bool:
        return True
    
    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        """Scrape LM Arena chat logs from various sources"""
        config = self.config.get("sources", {}).get("lmarena_chatlogs", {})
        
        if not config.get("enabled", False):
            return
        
        # 1. Check browser local storage
        for browser_path in config.get("browser_data_paths", []):
            expanded = os.path.expanduser(browser_path)
            if Path(expanded).exists():
                print(f"[LMArena] Scanning browser data: {expanded}")
                async for item in self._scan_browser_storage(Path(expanded)):
                    yield item
        
        # 2. Check exported chat files
        for export_path in config.get("exported_chats_path", []):
            expanded = os.path.expanduser(export_path)
            if Path(expanded).exists():
                print(f"[LMArena] Scanning exports: {expanded}")
                async for item in self._scan_exported_chats(Path(expanded), config):
                    yield item
        
        # 3. Try to parse browser history for LM Arena URLs
        async for item in self._scan_browser_history(config):
            yield item
    
    async def _scan_browser_storage(self, storage_path: Path) -> AsyncIterator[ScrapedItem]:
        """Scan browser local/session storage for chat data"""
        try:
            # Chrome/Edge LocalStorage is in LevelDB format
            # We'll look for relevant files
            for root, dirs, files in os.walk(storage_path):
                for filename in files:
                    filepath = Path(root) / filename
                    
                    # Look for LM Arena related storage
                    if any(domain in str(filepath).lower() for domain in ['lmsys', 'arena', 'chatbot']):
                        try:
                            item = await self._process_storage_file(filepath)
                            if item:
                                yield item
                        except:
                            pass
                            
                    # Also check log files
                    if filename.endswith('.log') or filename.endswith('.json'):
                        content = None
                        try:
                            async with aiofiles.open(filepath, 'r', errors='ignore') as f:
                                content = await f.read()
                        except:
                            continue
                        
                        if content and ('lmsys' in content.lower() or 'arena' in content.lower()):
                            yield ScrapedItem(
                                id=f"lmarena:browser:{filepath.name}",
                                source_type=self.source_type,
                                source_path=str(filepath),
                                content=content,
                                content_type=ContentType.DATA,
                                filename=filepath.name,
                                metadata={
                                    "source": "browser_storage",
                                    "browser_path": str(filepath)
                                },
                                confidence_score=0.8
                            )
                            
        except Exception as e:
            print(f"[LMArena] Error scanning browser storage: {e}")
    
    async def _scan_exported_chats(
        self, 
        export_path: Path,
        config: Dict
    ) -> AsyncIterator[ScrapedItem]:
        """Scan for exported chat files"""
        patterns = config.get("chat_patterns", [
            "*lmarena*", "*chat*.json", "*conversation*.json",
            "*chatbot-arena*", "*llm-chat*"
        ])
        
        try:
            for root, dirs, files in os.walk(export_path):
                for filename in files:
                    filepath = Path(root) / filename
                    
                    # Check if matches patterns
                    matches = any(
                        filepath.match(p) for p in patterns
                    ) or any(
                        term in filename.lower() 
                        for term in ['chat', 'conversation', 'lmarena', 'lmsys', 'arena']
                    )
                    
                    if not matches:
                        continue
                    
                    try:
                        async with aiofiles.open(filepath, 'r', errors='ignore') as f:
                            content = await f.read()
                        
                        # Try to parse as JSON
                        chat_data = None
                        try:
                            chat_data = json.loads(content)
                        except:
                            pass
                        
                        if chat_data:
                            # Format chat data nicely
                            formatted = self._format_chat_data(chat_data)
                            if formatted:
                                content = formatted
                        
                        # Check for code blocks in chat
                        code_blocks = self._extract_code_blocks(content)
                        
                        yield ScrapedItem(
                            id=f"lmarena:export:{filepath.name}",
                            source_type=self.source_type,
                            source_path=str(filepath),
                            content=content,
                            content_type=ContentType.DATA,
                            filename=filepath.name,
                            metadata={
                                "source": "exported_chat",
                                "has_code_blocks": len(code_blocks) > 0,
                                "code_block_count": len(code_blocks),
                                "code_languages": list(set(
                                    cb.get('language', 'unknown') 
                                    for cb in code_blocks
                                ))
                            },
                            confidence_score=0.9
                        )
                        
                        # Also yield individual code blocks as separate items
                        for i, block in enumerate(code_blocks):
                            yield ScrapedItem(
                                id=f"lmarena:code:{filepath.name}:{i}",
                                source_type=self.source_type,
                                source_path=f"{filepath}#code-block-{i}",
                                content=block['code'],
                                content_type=ContentType.SOURCE_CODE,
                                filename=f"{filepath.stem}_code_{i}.{block.get('extension', 'txt')}",
                                metadata={
                                    "source": "chat_code_block",
                                    "original_file": str(filepath),
                                    "block_index": i,
                                    "language": block.get('language')
                                },
                                language=block.get('language'),
                                confidence_score=1.0
                            )
                            
                    except Exception as e:
                        print(f"[LMArena] Error processing {filepath}: {e}")
                        
        except Exception as e:
            print(f"[LMArena] Error scanning exports: {e}")
    
    def _format_chat_data(self, data: Any) -> Optional[str]:
        """Format chat data into readable text"""
        try:
            if isinstance(data, list):
                # List of messages
                formatted = []
                for msg in data:
                    if isinstance(msg, dict):
                        role = msg.get('role', msg.get('sender', 'unknown'))
                        content = msg.get('content', msg.get('message', msg.get('text', '')))
                        formatted.append(f"## {role.upper()}\n\n{content}\n")
                return '\n---\n'.join(formatted)
            elif isinstance(data, dict):
                # Single conversation object
                if 'messages' in data:
                    return self._format_chat_data(data['messages'])
                elif 'conversation' in data:
                    return self._format_chat_data(data['conversation'])
                else:
                    return json.dumps(data, indent=2)
            return None
        except:
            return None
    
    def _extract_code_blocks(self, content: str) -> List[Dict[str, Any]]:
        """Extract code blocks from chat content"""
        blocks = []
        
        # Match markdown code blocks
        pattern = r'```(\w*)\n(.*?)```'
        matches = re.findall(pattern, content, re.DOTALL)
        
        lang_to_ext = {
            'python': 'py', 'javascript': 'js', 'typescript': 'ts',
            'java': 'java', 'cpp': 'cpp', 'c': 'c', 'go': 'go',
            'rust': 'rs', 'ruby': 'rb', 'r': 'R', 'sql': 'sql',
            'bash': 'sh', 'shell': 'sh', 'html': 'html', 'css': 'css',
            'json': 'json', 'yaml': 'yaml', 'yml': 'yaml'
        }
        
        for lang, code in matches:
            lang = lang.lower().strip() if lang else 'text'
            blocks.append({
                'language': lang,
                'extension': lang_to_ext.get(lang, 'txt'),
                'code': code.strip()
            })
        
        return blocks
    
    async def _scan_browser_history(self, config: Dict) -> AsyncIterator[ScrapedItem]:
        """Try to extract LM Arena URLs from browser history"""
        history_paths = {
            'chrome': Path.home() / 'AppData/Local/Google/Chrome/User Data/Default/History',
            'firefox': Path.home() / 'AppData/Roaming/Mozilla/Firefox/Profiles',
            'edge': Path.home() / 'AppData/Local/Microsoft/Edge/User Data/Default/History'
        }
        
        domains = config.get("lmarena_domains", [
            'chat.lmsys.org', 'arena.lmsys.org', 'lmarena.ai'
        ])
        
        for browser, history_path in history_paths.items():
            if not history_path.exists():
                continue
            
            # For Firefox, we need to find the profile
            if browser == 'firefox':
                for profile in history_path.iterdir():
                    if profile.is_dir():
                        places_db = profile / 'places.sqlite'
                        if places_db.exists():
                            async for item in self._query_firefox_history(places_db, domains):
                                yield item
            else:
                # Chrome/Edge use SQLite
                async for item in self._query_chromium_history(history_path, domains, browser):
                    yield item
    
    async def _query_chromium_history(
        self, 
        history_path: Path,
        domains: List[str],
        browser: str
    ) -> AsyncIterator[ScrapedItem]:
        """Query Chrome/Edge history for LM Arena URLs"""
        import shutil
        import tempfile
        
        try:
            # Copy database to temp location (it might be locked)
            with tempfile.NamedTemporaryFile(delete=False, suffix='.db') as tmp:
                tmp_path = tmp.name
            
            shutil.copy2(history_path, tmp_path)
            
            conn = sqlite3.connect(tmp_path)
            cursor = conn.cursor()
            
            # Build query for domains
            domain_conditions = ' OR '.join(f"url LIKE '%{d}%'" for d in domains)
            
            cursor.execute(f"""
                SELECT url, title, last_visit_time 
                FROM urls 
                WHERE {domain_conditions}
                ORDER BY last_visit_time DESC
            """)
            
            urls = cursor.fetchall()
            conn.close()
            os.unlink(tmp_path)
            
            if urls:
                content = f"# LM Arena URLs from {browser}\n\n"
                for url, title, visit_time in urls:
                    content += f"- [{title or 'Untitled'}]({url})\n"
                
                yield ScrapedItem(
                    id=f"lmarena:history:{browser}",
                    source_type=self.source_type,
                    source_path=f"browser:{browser}:history",
                    content=content,
                    content_type=ContentType.DATA,
                    filename=f"lmarena_{browser}_history.md",
                    metadata={
                        "source": "browser_history",
                        "browser": browser,
                        "url_count": len(urls)
                    },
                    confidence_score=0.7
                )
                
        except Exception as e:
            print(f"[LMArena] Error querying {browser} history: {e}")
    
    async def _query_firefox_history(
        self, 
        places_db: Path,
        domains: List[str]
    ) -> AsyncIterator[ScrapedItem]:
        """Query Firefox history"""
        try:
            import shutil
            import tempfile
            
            with tempfile.NamedTemporaryFile(delete=False, suffix='.db') as tmp:
                tmp_path = tmp.name
            
            shutil.copy2(places_db, tmp_path)
            
            conn = sqlite3.connect(tmp_path)
            cursor = conn.cursor()
            
            domain_conditions = ' OR '.join(f"url LIKE '%{d}%'" for d in domains)
            
            cursor.execute(f"""
                SELECT url, title, last_visit_date 
                FROM moz_places 
                WHERE {domain_conditions}
                ORDER BY last_visit_date DESC
            """)
            
            urls = cursor.fetchall()
            conn.close()
            os.unlink(tmp_path)
            
            if urls:
                content = f"# LM Arena URLs from Firefox\n\n"
                for url, title, visit_time in urls:
                    content += f"- [{title or 'Untitled'}]({url})\n"
                
                yield ScrapedItem(
                    id=f"lmarena:history:firefox",
                    source_type=self.source_type,
                    source_path="browser:firefox:history",
                    content=content,
                    content_type=ContentType.DATA,
                    filename="lmarena_firefox_history.md",
                    metadata={
                        "source": "browser_history",
                        "browser": "firefox",
                        "url_count": len(urls)
                    },
                    confidence_score=0.7
                )
                
        except Exception as e:
            print(f"[LMArena] Error querying Firefox history: {e}")

3. Updated Pipeline with All Scrapers

Python

# orchestrator/pipeline.py (updated)
"""
Updated pipeline with all your specific scrapers
"""
import asyncio
from typing import List, Dict, Any, Optional
from datetime import datetime
from dataclasses import dataclass
import logging

from scrapers.base import ScrapedItem, SourceType
from scrapers.github_scraper import GitHubScraper
from scrapers.local_drives_scraper import LocalDrivesScraper
from scrapers.rstudio_scraper import RStudioScraper
from scrapers.linux_system_scraper import LinuxSystemScraper
from scrapers.lmarena_scraper import LMArenaLogsScraper
from processors.processor import DataProcessor
from storage.vector_store import VectorStore
from argilla_integration.datasets import ArgillaManager
from config.settings import settings, load_sources_config


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RecoveryPipeline:
    """Main pipeline for recovering and organizing project data"""
    
    def __init__(self):
        self.config = load_sources_config()
        
        # Add project keywords to config if not present
        if "project_keywords" not in self.config:
            self.config["project_keywords"] = []
        
        self.processor = DataProcessor(
            embedding_model=settings.embedding_model,
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )
        self.vector_store = VectorStore(
            url=settings.qdrant_url,
            collection_name=settings.qdrant_collection
        )
        self.argilla = ArgillaManager(
            api_url=settings.argilla_api_url,
            api_key=settings.argilla_api_key,
            workspace=settings.argilla_workspace
        )
        
        # Initialize all scrapers
        self.scrapers = self._init_scrapers()
        
        # State
        self.status = "idle"
        self.current_run = None
        self.runs_history = []
        self.item_buffer = []
        self.buffer_size = 50
        
    def _init_scrapers(self) -> Dict[str, Any]:
        """Initialize all scrapers for your specific sources"""
        scrapers = {}
        
        # 1. GitHub Scraper
        logger.info("Initializing GitHub scraper...")
        scrapers['github'] = GitHubScraper(
            self.config,
            token=settings.github_token
        )
        
        # 2. Local Drives Scraper
        logger.info("Initializing Local Drives scraper...")
        scrapers['local_drives'] = LocalDrivesScraper(self.config)
        
        # 3. RStudio Scraper
        logger.info("Initializing RStudio scraper...")
        scrapers['rstudio'] = RStudioScraper(self.config)
        
        # 4. Linux System Scraper
        logger.info("Initializing Linux System scraper...")
        scrapers['linux_system'] = LinuxSystemScraper(self.config)
        
        # 5. LM Arena Logs Scraper
        logger.info("Initializing LM Arena scraper...")
        scrapers['lmarena'] = LMArenaLogsScraper(self.config)
        
        return scrapers
    
    async def run_full_pipeline(self) -> Dict:
        """Run the complete recovery pipeline"""
        run_id = f"run_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}"
        
        result = {
            "run_id": run_id,
            "started_at": datetime.utcnow().isoformat(),
            "status": "running",
            "sources": {},
            "total_items": 0,
            "total_processed": 0,
            "total_stored": 0,
            "errors": []
        }
        
        self.status = "running"
        logger.info(f"Starting pipeline run: {run_id}")
        
        try:
            # Create Argilla dataset
            dataset = self.argilla.create_recovery_dataset(
                name=f"recovery_{run_id}"
            )
            
            # Run each scraper
            for source_name, scraper in self.scrapers.items():
                source_result = {
                    "items_found": 0,
                    "items_processed": 0,
                    "errors": []
                }
                
                logger.info(f"Running scraper: {source_name}")
                
                try:
                    if await scraper.validate_connection():
                        async for item in scraper.scrape():
                            source_result["items_found"] += 1
                            result["total_items"] += 1
                            
                            await self._process_item(item, dataset, result)
                            
                            if result["total_items"] % 100 == 0:
                                logger.info(f"Progress: {result['total_items']} items scraped")
                    else:
                        logger.warning(f"Could not connect to {source_name}")
                        source_result["errors"].append("Connection validation failed")
                        
                except Exception as e:
                    error_msg = f"Error in {source_name}: {str(e)}"
                    logger.error(error_msg)
                    source_result["errors"].append(error_msg)
                    result["errors"].append(error_msg)
                
                result["sources"][source_name] = source_result
            
            # Flush remaining buffer
            await self._flush_buffer(dataset, result)
            
            result["status"] = "completed"
            
        except Exception as e:
            result["status"] = "error"
            result["errors"].append(f"Pipeline error: {str(e)}")
            logger.error(f"Pipeline failed: {e}")
            
        finally:
            result["ended_at"] = datetime.utcnow().isoformat()
            self.status = "idle"
            self.runs_history.append(result)
        
        # Log summary
        logger.info(f"""
Pipeline Complete:
  - Total Items: {result['total_items']}
  - Processed: {result['total_processed']}  
  - Stored: {result['total_stored']}
  - Errors: {len(result['errors'])}
        """)
        
        return result
    
    async def run_single_source(self, source_name: str) -> Dict:
        """Run only a specific source scraper"""
        if source_name not in self.scrapers:
            return {"error": f"Unknown source: {source_name}"}
        
        scraper = self.scrapers[source_name]
        
        result = {
            "source": source_name,
            "items_found": 0,
            "items_processed": 0,
            "errors": []
        }
        
        logger.info(f"Running single source: {source_name}")
        
        try:
            if await scraper.validate_connection():
                async for item in scraper.scrape():
                    result["items_found"] += 1
                    
                    # Process immediately
                    chunks = self.processor.process(item)
                    if chunks:
                        self.vector_store.upsert_chunks(chunks)
                        result["items_processed"] += 1
            else:
                result["errors"].append("Connection validation failed")
                
        except Exception as e:
            result["errors"].append(str(e))
        
        return result
    
    async def _process_item(self, item: ScrapedItem, dataset, result: Dict):
        """Process a single item"""
        self.item_buffer.append(item)
        
        if len(self.item_buffer) >= self.buffer_size:
            await self._flush_buffer(dataset, result)
    
    async def _flush_buffer(self, dataset, result: Dict):
        """Flush buffer to storage"""
        if not self.item_buffer:
            return
        
        for item in self.item_buffer:
            chunks = self.processor.process(item)
            if chunks:
                stored = self.vector_store.upsert_chunks(chunks)
                result["total_stored"] += stored
            result["total_processed"] += 1
        
        # Add to Argilla
        self.argilla.add_items_to_dataset(dataset, self.item_buffer)
        
        self.item_buffer.clear()
    
    def search(self, query: str, limit: int = 10, filters: Dict = None) -> List[Dict]:
        """Search recovered data"""
        return self.vector_store.search_by_text(
            query,
            self.processor.embedding_model,
            limit,
            filters
        )
    
    def get_stats(self) -> Dict:
        """Get system statistics"""
        return {
            "status": self.status,
            "vector_store": self.vector_store.get_statistics(),
            "total_runs": len(self.runs_history),
            "scrapers": list(self.scrapers.keys())
        }

4. Interactive Setup Script

Python

# setup_sources.py
"""
Interactive setup script to configure your specific sources
"""
import os
import yaml
from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt, Confirm
from rich.panel import Panel

console = Console()


def setup_sources():
    """Interactive setup for source configuration"""
    console.print(Panel.fit(
        "[bold blue]Project Recovery System Setup[/bold blue]\n"
        "Let's configure your data sources",
        border_style="blue"
    ))
    
    config = {
        "project_info": {},
        "project_keywords": [],
        "file_signatures": [],
        "sources": {}
    }
    
    # Project info
    console.print("\n[bold]1. Project Information[/bold]")
    config["project_info"]["name"] = Prompt.ask("Project name")
    config["project_info"]["description"] = Prompt.ask("Brief description", default="")
    
    # Keywords
    console.print("\n[bold]2. Project Keywords[/bold]")
    console.print("Enter keywords that uniquely identify your project (one per line, empty to finish):")
    while True:
        keyword = Prompt.ask("Keyword", default="")
        if not keyword:
            break
        config["project_keywords"].append(keyword)
    
    # GitHub
    console.print("\n[bold]3. GitHub Configuration[/bold]")
    if Confirm.ask("Enable GitHub scraping?"):
        config["sources"]["github"] = {
            "enabled": True,
            "repositories": [],
            "search_queries": [],
            "include_gists": True,
            "include_forks": True
        }
        
        username = Prompt.ask("GitHub username")
        
        console.print("Enter repository names (one per line, empty to finish):")
        while True:
            repo = Prompt.ask("Repository", default="")
            if not repo:
                break
            config["sources"]["github"]["repositories"].append({
                "owner": username,
                "repo": repo
            })
        
        config["sources"]["github"]["search_queries"].append(f"user:{username}")
    else:
        config["sources"]["github"] = {"enabled": False}
    
    # Local Drives
    console.print("\n[bold]4. Local Drives Configuration[/bold]")
    if Confirm.ask("Enable local drives scanning?"):
        config["sources"]["local_drives"] = {
            "enabled": True,
            "windows_paths": [],
            "include_patterns": [
                "*.py", "*.r", "*.R", "*.Rmd", "*.js", "*.ts",
                "*.md", "*.json", "*.yaml", "*.yml", "*.sql",
                "*.html", "*.css", "Dockerfile", "Makefile"
            ],
            "exclude_patterns": [
                "node_modules/*", "__pycache__/*", ".git/*",
                "Windows/*", "Program Files/*"
            ]
        }
        
        # Get Windows username
        win_user = os.environ.get('USERNAME', os.environ.get('USER', 'user'))
        
        # Default paths
        default_paths = [
            f"C:/Users/{win_user}/Documents",
            f"C:/Users/{win_user}/Desktop",
            f"C:/Users/{win_user}/Projects",
        ]
        
        for path in default_paths:
            if Confirm.ask(f"Include {path}?", default=True):
                config["sources"]["local_drives"]["windows_paths"].append(path)
        
        console.print("Enter additional paths (empty to finish):")
        while True:
            path = Prompt.ask("Path", default="")
            if not path:
                break
            config["sources"]["local_drives"]["windows_paths"].append(path)
    else:
        config["sources"]["local_drives"] = {"enabled": False}
    
    # RStudio
    console.print("\n[bold]5. RStudio Restored Data[/bold]")
    if Confirm.ask("Enable RStudio data scanning?"):
        config["sources"]["rstudio_restored"] = {
            "enabled": True,
            "paths": [],
            "include_patterns": [
                "*.R", "*.r", "*.Rmd", "*.rmd", "*.Rproj",
                "*.RData", "*.rda", "*.rds", "DESCRIPTION"
            ],
            "rstudio_config_paths": []
        }
        
        console.print("Enter paths to RStudio restored data (empty to finish):")
        while True:
            path = Prompt.ask("RStudio data path", default="")
            if not path:
                break
            config["sources"]["rstudio_restored"]["paths"].append(path)
        
        # Default RStudio config paths
        win_user = os.environ.get('USERNAME', 'user')
        config["sources"]["rstudio_restored"]["rstudio_config_paths"] = [
            f"C:/Users/{win_user}/AppData/Local/RStudio",
            f"C:/Users/{win_user}/AppData/Roaming/RStudio"
        ]
    else:
        config["sources"]["rstudio_restored"] = {"enabled": False}
    
    # Linux System
    console.print("\n[bold]6. Linux System[/bold]")
    if Confirm.ask("Enable Linux system scanning?"):
        config["sources"]["linux_system"] = {
            "enabled": True,
            "mounted_paths": [],
            "deep_scan_paths": []
        }
        
        # Check for WSL
        console.print("Checking for WSL...")
        try:
            import subprocess
            result = subprocess.run(['wsl', '--list', '--quiet'], 
                                   capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                distros = [d.strip() for d in result.stdout.strip().split('\n') if d.strip()]
                if distros:
                    console.print(f"Found WSL distros: {distros}")
                    for distro in distros:
                        if Confirm.ask(f"Include WSL: {distro}?"):
                            config["sources"]["linux_system"]["mounted_paths"].append(
                                f"\\\\wsl$\\{distro}\\home"
                            )
        except:
            console.print("[yellow]WSL not detected[/yellow]")
        
        linux_user = Prompt.ask("Linux username", default="")
        if linux_user:
            config["sources"]["linux_system"]["deep_scan_paths"].extend([
                f"/home/{linux_user}/projects",
                f"/home/{linux_user}/code",
                f"/home/{linux_user}/Documents"
            ])
        
        console.print("Enter additional Linux paths (empty to finish):")
        while True:
            path = Prompt.ask("Linux path", default="")
            if not path:
                break
            config["sources"]["linux_system"]["mounted_paths"].append(path)
    else:
        config["sources"]["linux_system"] = {"enabled": False}
    
    # LM Arena
    console.print("\n[bold]7. LM Arena Chat Logs[/bold]")
    if Confirm.ask("Enable LM Arena chat log scanning?"):
        win_user = os.environ.get('USERNAME', 'user')
        
        config["sources"]["lmarena_chatlogs"] = {
            "enabled": True,
            "browser_data_paths": [
                f"C:/Users/{win_user}/AppData/Local/Google/Chrome/User Data/Default",
                f"C:/Users/{win_user}/AppData/Local/Microsoft/Edge/User Data/Default"
            ],
            "exported_chats_path": [
                f"C:/Users/{win_user}/Downloads",
                f"C:/Users/{win_user}/Documents"
            ],
            "chat_patterns": [
                "*lmarena*", "*chat*.json", "*conversation*.json"
            ],
            "lmarena_domains": [
                "chat.lmsys.org", "arena.lmsys.org", "lmarena.ai"
            ]
        }
        
        console.print("Enter paths where you might have exported chats (empty to finish):")
        while True:
            path = Prompt.ask("Chat export path", default="")
            if not path:
                break
            config["sources"]["lmarena_chatlogs"]["exported_chats_path"].append(path)
    else:
        config["sources"]["lmarena_chatlogs"] = {"enabled": False}
    
    # Save configuration
    config_dir = Path("config")
    config_dir.mkdir(exist_ok=True)
    
    config_path = config_dir / "sources.yaml"
    
    with open(config_path, 'w') as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)
    
    console.print(f"\n[green]Configuration saved to {config_path}[/green]")
    console.print("\nYou can edit this file manually to fine-tune settings.")
    
    return config


if __name__ == "__main__":
    setup_sources()

5. Quick Start Commands

Bash

# Create project directory
mkdir project-recovery && cd project-recovery

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or: .\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run interactive setup
python setup_sources.py

# Start the services
docker-compose up -d

# Run the pipeline
python main.py pipeline

# Or run specific sources
python -c "
import asyncio
from orchestrator.pipeline import RecoveryPipeline

async def main():
    pipeline = RecoveryPipeline()
    
    # Run specific sources
    print('Scanning GitHub...')
    await pipeline.run_single_source('github')
    
    print('Scanning Local Drives...')
    await pipeline.run_single_source('local_drives')
    
    print('Scanning RStudio...')
    await pipeline.run_single_source('rstudio')
    
    print('Scanning Linux System...')
    await pipeline.run_single_source('linux_system')
    
    print('Scanning LM Arena logs...')
    await pipeline.run_single_source('lmarena')

asyncio.run(main())
"

# Access the dashboard
# http://localhost:8501 - Streamlit Dashboard
# http://localhost:6900 - Argilla UI (for labeling)
# http://localhost:8000/docs - API Documentation

6. Example .env File

Bash

# .env - Fill in your actual values

# GitHub
GITHUB_TOKEN=ghp_your_token_here
GITHUB_USERNAME=your_username

# Argilla
ARGILLA_API_URL=http://localhost:6900
ARGILLA_API_KEY=admin.apikey

# Database
DATABASE_URL=postgresql://recovery:recovery_pass@localhost:5432/project_recovery

# Vector Store
QDRANT_URL=http://localhost:6333

# Your Windows username (for path resolution)
WINDOWS_USERNAME=YourWindowsUsername

# Your Linux username (for WSL/Linux paths)
LINUX_USERNAME=your_linux_user

This setup will:

    GitHub: Scan your repos, gists, and search for your code
    Local Drives: Deep scan your Windows drives for project files
    RStudio: Specifically target R/RStudio project files and data
    Linux System: Access WSL or mounted Linux partitions
    LM Arena: Extract chat logs and code blocks from your conversations

Would you like me to add any additional sources or customize any of these scrapers further?

i need those locations to be checked
github, my local drives , folder with r studio restored data, linux system on my drive ,, my lmarena chat logs
claude-opus-4-5-20251101-thinking-32k
Self-Sustaining Data Recovery & Organization System

I can't access that specific GitHub repo directly, but I'll help you build a comprehensive system using Argilla and related tools for recovering and organizing your lost project data.
System Architecture

text

┌─────────────────────────────────────────────────────────────────────┐
│                    PROJECT DATA RECOVERY SYSTEM                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐          │
│  │   SCRAPERS   │───▶│  PROCESSORS  │───▶│   ARGILLA    │          │
│  │              │    │              │    │   (Label &   │          │
│  │ • GitHub     │    │ • Normalize  │    │   Curate)    │          │
│  │ • Local FS   │    │ • Dedupe     │    │              │          │
│  │ • Cloud      │    │ • Classify   │    └──────┬───────┘          │
│  │ • Email      │    │ • Chunk      │           │                   │
│  │ • Web Cache  │    └──────────────┘           ▼                   │
│  └──────────────┘                      ┌──────────────┐             │
│                                        │   STORAGE    │             │
│  ┌──────────────┐                      │              │             │
│  │  SCHEDULER   │◀────────────────────▶│ • Vector DB  │             │
│  │  (Celery/    │                      │ • PostgreSQL │             │
│  │   APScheduler)                      │ • File Store │             │
│  └──────────────┘                      └──────────────┘             │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘

Project Structure

text

project_recovery_system/
├── docker-compose.yml
├── requirements.txt
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── sources.yaml
├── scrapers/
│   ├── __init__.py
│   ├── base.py
│   ├── github_scraper.py
│   ├── filesystem_scraper.py
│   ├── cloud_scraper.py
│   ├── email_scraper.py
│   └── web_cache_scraper.py
├── processors/
│   ├── __init__.py
│   ├── normalizer.py
│   ├── deduplicator.py
│   ├── classifier.py
│   └── chunker.py
├── storage/
│   ├── __init__.py
│   ├── vector_store.py
│   ├── database.py
│   └── file_store.py
├── argilla_integration/
│   ├── __init__.py
│   ├── datasets.py
│   ├── labeling.py
│   └── feedback.py
├── orchestrator/
│   ├── __init__.py
│   ├── scheduler.py
│   ├── pipeline.py
│   └── tasks.py
├── api/
│   ├── __init__.py
│   ├── main.py
│   └── routes.py
├── ui/
│   └── dashboard.py
└── main.py

Core Implementation
1. Docker Setup

YAML

# docker-compose.yml
version: '3.8'

services:
  argilla:
    image: argilla/argilla-server:latest
    ports:
      - "6900:6900"
    environment:
      - ARGILLA_ELASTICSEARCH=http://elasticsearch:9200
      - ARGILLA_AUTH_SECRET_KEY=your-secret-key
      - ARGILLA_API_KEY=admin.apikey
    depends_on:
      - elasticsearch
    volumes:
      - argilla_data:/var/lib/argilla

  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.5.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    volumes:
      - es_data:/usr/share/elasticsearch/data
    ports:
      - "9200:9200"

  postgres:
    image: postgres:15
    environment:
      - POSTGRES_USER=recovery
      - POSTGRES_PASSWORD=recovery_pass
      - POSTGRES_DB=project_recovery
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  qdrant:
    image: qdrant/qdrant:latest
    ports:
      - "6333:6333"
    volumes:
      - qdrant_data:/qdrant/storage

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  recovery_system:
    build: .
    depends_on:
      - argilla
      - postgres
      - qdrant
      - redis
    volumes:
      - ./:/app
      - ./data:/app/data
    environment:
      - ARGILLA_API_URL=http://argilla:6900
      - ARGILLA_API_KEY=admin.apikey
      - DATABASE_URL=postgresql://recovery:recovery_pass@postgres:5432/project_recovery
      - QDRANT_URL=http://qdrant:6333
      - REDIS_URL=redis://redis:6379
    ports:
      - "8000:8000"

  celery_worker:
    build: .
    command: celery -A orchestrator.tasks worker --loglevel=info
    depends_on:
      - redis
      - recovery_system
    volumes:
      - ./:/app
      - ./data:/app/data
    environment:
      - REDIS_URL=redis://redis:6379

  celery_beat:
    build: .
    command: celery -A orchestrator.tasks beat --loglevel=info
    depends_on:
      - redis
      - celery_worker
    volumes:
      - ./:/app

volumes:
  argilla_data:
  es_data:
  postgres_data:
  qdrant_data:
  redis_data:

2. Requirements

txt

# requirements.txt
argilla>=1.20.0
fastapi>=0.104.0
uvicorn>=0.24.0
celery>=5.3.0
redis>=5.0.0
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
qdrant-client>=1.6.0
sentence-transformers>=2.2.0
beautifulsoup4>=4.12.0
aiohttp>=3.9.0
aiofiles>=23.2.0
PyGithub>=2.1.0
google-api-python-client>=2.100.0
python-dotenv>=1.0.0
pyyaml>=6.0.0
rich>=13.0.0
httpx>=0.25.0
pandas>=2.0.0
watchdog>=3.0.0
streamlit>=1.28.0
plotly>=5.18.0
python-magic>=0.4.27
chardet>=5.2.0

3. Configuration

Python

# config/settings.py
from pydantic_settings import BaseSettings
from typing import Optional, List
from pathlib import Path
import yaml


class Settings(BaseSettings):
    # Argilla
    argilla_api_url: str = "http://localhost:6900"
    argilla_api_key: str = "admin.apikey"
    argilla_workspace: str = "project_recovery"
    
    # Database
    database_url: str = "postgresql://recovery:recovery_pass@localhost:5432/project_recovery"
    
    # Vector Store
    qdrant_url: str = "http://localhost:6333"
    qdrant_collection: str = "project_fragments"
    
    # Redis
    redis_url: str = "redis://localhost:6379"
    
    # Scraping
    scan_directories: List[str] = []
    github_token: Optional[str] = None
    github_username: Optional[str] = None
    google_credentials_path: Optional[str] = None
    
    # Processing
    embedding_model: str = "all-MiniLM-L6-v2"
    chunk_size: int = 1000
    chunk_overlap: int = 200
    
    # Scheduling
    scrape_interval_hours: int = 6
    
    class Config:
        env_file = ".env"


settings = Settings()


def load_sources_config() -> dict:
    """Load sources configuration from YAML"""
    config_path = Path(__file__).parent / "sources.yaml"
    if config_path.exists():
        with open(config_path) as f:
            return yaml.safe_load(f)
    return {}

YAML

# config/sources.yaml
sources:
  github:
    enabled: true
    repositories:
      - owner: your-username
        repo: lost-project-1
      - owner: your-username
        repo: lost-project-2
    search_queries:
      - "your project keywords"
    include_forks: true
    include_gists: true
    
  filesystem:
    enabled: true
    paths:
      - /home/user/old_projects
      - /home/user/backups
      - /mnt/external_drive/code
    patterns:
      - "*.py"
      - "*.js"
      - "*.ts"
      - "*.md"
      - "*.json"
      - "*.yaml"
      - "*.yml"
      - "*.txt"
      - "*.sql"
      - "*.html"
      - "*.css"
    exclude_patterns:
      - "node_modules/*"
      - "__pycache__/*"
      - ".git/*"
      - "*.pyc"
      
  cloud:
    google_drive:
      enabled: true
      folder_ids:
        - "your-folder-id-1"
      search_queries:
        - "project documentation"
    dropbox:
      enabled: false
      
  email:
    enabled: true
    imap_server: imap.gmail.com
    search_folders:
      - INBOX
      - "[Gmail]/Sent Mail"
    search_queries:
      - "project attachment"
      - "code review"
    date_range:
      start: "2020-01-01"
      end: null
      
  web_cache:
    enabled: true
    sources:
      - wayback_machine
      - google_cache
    urls:
      - "https://your-old-website.com"
      - "https://old-docs.project.com"

project_keywords:
  - "your_project_name"
  - "specific_function_names"
  - "unique_identifiers"
  
file_signatures:
  - pattern: "# Your Project Header"
    type: source_code
  - pattern: "Copyright Your Name"
    type: documentation

4. Base Scraper

Python

# scrapers/base.py
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional, Dict, Any, AsyncIterator
from enum import Enum
import hashlib
import asyncio
from pathlib import Path


class ContentType(Enum):
    SOURCE_CODE = "source_code"
    DOCUMENTATION = "documentation"
    CONFIGURATION = "configuration"
    DATA = "data"
    BINARY = "binary"
    UNKNOWN = "unknown"


class SourceType(Enum):
    GITHUB = "github"
    LOCAL_FILESYSTEM = "local_filesystem"
    GOOGLE_DRIVE = "google_drive"
    DROPBOX = "dropbox"
    EMAIL = "email"
    WEB_CACHE = "web_cache"
    MANUAL = "manual"


@dataclass
class ScrapedItem:
    """Represents a single piece of recovered data"""
    id: str
    source_type: SourceType
    source_path: str
    content: str
    content_type: ContentType
    file_extension: Optional[str] = None
    filename: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: Optional[datetime] = None
    modified_at: Optional[datetime] = None
    scraped_at: datetime = field(default_factory=datetime.utcnow)
    content_hash: str = ""
    size_bytes: int = 0
    language: Optional[str] = None
    confidence_score: float = 1.0
    
    def __post_init__(self):
        if not self.content_hash and self.content:
            self.content_hash = hashlib.sha256(self.content.encode()).hexdigest()
        if not self.size_bytes and self.content:
            self.size_bytes = len(self.content.encode())
        if not self.id:
            self.id = f"{self.source_type.value}:{self.content_hash[:16]}"


@dataclass
class ScrapeResult:
    """Result of a scraping operation"""
    source_type: SourceType
    items: List[ScrapedItem]
    success: bool
    error_message: Optional[str] = None
    total_found: int = 0
    total_processed: int = 0
    duration_seconds: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)


class BaseScraper(ABC):
    """Base class for all scrapers"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.keywords = config.get("project_keywords", [])
        self.file_signatures = config.get("file_signatures", [])
        
    @property
    @abstractmethod
    def source_type(self) -> SourceType:
        pass
    
    @abstractmethod
    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        """Scrape and yield items one at a time"""
        pass
    
    @abstractmethod
    async def validate_connection(self) -> bool:
        """Validate that the scraper can connect to its source"""
        pass
    
    def is_relevant(self, content: str, filename: str = "") -> tuple[bool, float]:
        """Check if content is relevant to the project"""
        score = 0.0
        max_score = len(self.keywords) + len(self.file_signatures)
        
        if max_score == 0:
            return True, 1.0
        
        content_lower = content.lower()
        filename_lower = filename.lower()
        
        # Check keywords
        for keyword in self.keywords:
            if keyword.lower() in content_lower or keyword.lower() in filename_lower:
                score += 1.0
                
        # Check file signatures
        for sig in self.file_signatures:
            if sig["pattern"] in content:
                score += 1.5  # Signatures are weighted higher
                
        confidence = min(score / max_score, 1.0) if max_score > 0 else 1.0
        return score > 0, confidence
    
    def detect_content_type(self, content: str, filename: str = "") -> ContentType:
        """Detect the type of content"""
        ext = Path(filename).suffix.lower() if filename else ""
        
        code_extensions = {'.py', '.js', '.ts', '.java', '.cpp', '.c', '.go', '.rs', '.rb'}
        doc_extensions = {'.md', '.rst', '.txt', '.doc', '.docx', '.pdf'}
        config_extensions = {'.json', '.yaml', '.yml', '.toml', '.ini', '.env'}
        data_extensions = {'.csv', '.sql', '.xml'}
        
        if ext in code_extensions:
            return ContentType.SOURCE_CODE
        elif ext in doc_extensions:
            return ContentType.DOCUMENTATION
        elif ext in config_extensions:
            return ContentType.CONFIGURATION
        elif ext in data_extensions:
            return ContentType.DATA
        
        # Content-based detection
        if any(kw in content[:500] for kw in ['def ', 'function ', 'class ', 'import ', 'const ', 'let ']):
            return ContentType.SOURCE_CODE
        elif content.startswith('#') or '##' in content[:200]:
            return ContentType.DOCUMENTATION
            
        return ContentType.UNKNOWN
    
    def detect_language(self, content: str, filename: str = "") -> Optional[str]:
        """Detect programming language"""
        ext = Path(filename).suffix.lower() if filename else ""
        
        ext_to_lang = {
            '.py': 'python', '.js': 'javascript', '.ts': 'typescript',
            '.java': 'java', '.cpp': 'cpp', '.c': 'c', '.go': 'go',
            '.rs': 'rust', '.rb': 'ruby', '.php': 'php', '.swift': 'swift',
            '.kt': 'kotlin', '.scala': 'scala', '.r': 'r', '.jl': 'julia',
            '.sql': 'sql', '.html': 'html', '.css': 'css', '.sh': 'bash'
        }
        
        if ext in ext_to_lang:
            return ext_to_lang[ext]
        
        # Content-based detection
        if 'def ' in content and 'import ' in content:
            return 'python'
        elif 'function' in content and ('const ' in content or 'let ' in content):
            return 'javascript'
            
        return None

5. GitHub Scraper

Python

# scrapers/github_scraper.py
import asyncio
import aiohttp
from datetime import datetime
from typing import AsyncIterator, Dict, Any, Optional, List
import base64
from github import Github, GithubException
from .base import BaseScraper, ScrapedItem, SourceType, ContentType


class GitHubScraper(BaseScraper):
    """Scraper for GitHub repositories, gists, and search results"""
    
    def __init__(self, config: Dict[str, Any], token: Optional[str] = None):
        super().__init__(config)
        self.token = token
        self.github = Github(token) if token else Github()
        self.rate_limit_delay = 1.0
        
    @property
    def source_type(self) -> SourceType:
        return SourceType.GITHUB
    
    async def validate_connection(self) -> bool:
        try:
            rate_limit = self.github.get_rate_limit()
            return rate_limit.core.remaining > 0
        except GithubException:
            return False
    
    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        """Scrape all configured GitHub sources"""
        github_config = self.config.get("sources", {}).get("github", {})
        
        if not github_config.get("enabled", False):
            return
            
        # Scrape specific repositories
        for repo_config in github_config.get("repositories", []):
            async for item in self._scrape_repository(
                repo_config["owner"], 
                repo_config["repo"]
            ):
                yield item
                
        # Search for code
        for query in github_config.get("search_queries", []):
            async for item in self._search_code(query):
                yield item
                
        # Scrape gists if enabled
        if github_config.get("include_gists", False):
            async for item in self._scrape_gists():
                yield item
    
    async def _scrape_repository(
        self, 
        owner: str, 
        repo_name: str,
        branch: str = None
    ) -> AsyncIterator[ScrapedItem]:
        """Scrape all files from a repository"""
        try:
            repo = self.github.get_repo(f"{owner}/{repo_name}")
            default_branch = branch or repo.default_branch
            
            # Get all contents recursively
            contents = repo.get_contents("", ref=default_branch)
            
            while contents:
                file_content = contents.pop(0)
                
                if file_content.type == "dir":
                    contents.extend(repo.get_contents(file_content.path, ref=default_branch))
                else:
                    try:
                        # Decode content
                        if file_content.encoding == "base64":
                            content = base64.b64decode(file_content.content).decode('utf-8', errors='ignore')
                        else:
                            content = file_content.content or ""
                        
                        # Check relevance
                        is_relevant, confidence = self.is_relevant(content, file_content.name)
                        
                        if is_relevant or confidence > 0.3:
                            yield ScrapedItem(
                                id=f"github:{owner}/{repo_name}:{file_content.sha[:8]}",
                                source_type=self.source_type,
                                source_path=f"github.com/{owner}/{repo_name}/{file_content.path}",
                                content=content,
                                content_type=self.detect_content_type(content, file_content.name),
                                file_extension=file_content.name.split('.')[-1] if '.' in file_content.name else None,
                                filename=file_content.name,
                                metadata={
                                    "repo": f"{owner}/{repo_name}",
                                    "branch": default_branch,
                                    "sha": file_content.sha,
                                    "url": file_content.html_url,
                                    "size": file_content.size
                                },
                                language=self.detect_language(content, file_content.name),
                                confidence_score=confidence
                            )
                    except Exception as e:
                        print(f"Error processing {file_content.path}: {e}")
                        
                await asyncio.sleep(self.rate_limit_delay)
                
        except GithubException as e:
            print(f"GitHub error for {owner}/{repo_name}: {e}")
    
    async def _search_code(self, query: str) -> AsyncIterator[ScrapedItem]:
        """Search GitHub for code matching query"""
        try:
            # Add user filter if configured
            username = self.config.get("github_username")
            if username:
                query = f"{query} user:{username}"
            
            results = self.github.search_code(query)
            
            for result in results:
                try:
                    content = base64.b64decode(result.content).decode('utf-8', errors='ignore')
                    
                    yield ScrapedItem(
                        id=f"github:search:{result.sha[:8]}",
                        source_type=self.source_type,
                        source_path=result.html_url,
                        content=content,
                        content_type=self.detect_content_type(content, result.name),
                        filename=result.name,
                        metadata={
                            "repo": result.repository.full_name,
                            "search_query": query,
                            "sha": result.sha
                        },
                        language=self.detect_language(content, result.name),
                        confidence_score=1.0
                    )
                    
                    await asyncio.sleep(self.rate_limit_delay * 2)
                    
                except Exception as e:
                    print(f"Error processing search result: {e}")
                    
        except GithubException as e:
            print(f"GitHub search error: {e}")
    
    async def _scrape_gists(self) -> AsyncIterator[ScrapedItem]:
        """Scrape user's gists"""
        try:
            user = self.github.get_user()
            
            for gist in user.get_gists():
                for filename, file_info in gist.files.items():
                    content = file_info.content or ""
                    
                    is_relevant, confidence = self.is_relevant(content, filename)
                    
                    if is_relevant or confidence > 0.2:
                        yield ScrapedItem(
                            id=f"github:gist:{gist.id}:{filename}",
                            source_type=self.source_type,
                            source_path=gist.html_url,
                            content=content,
                            content_type=self.detect_content_type(content, filename),
                            filename=filename,
                            metadata={
                                "gist_id": gist.id,
                                "description": gist.description,
                                "public": gist.public,
                                "created_at": gist.created_at.isoformat() if gist.created_at else None
                            },
                            created_at=gist.created_at,
                            modified_at=gist.updated_at,
                            language=file_info.language,
                            confidence_score=confidence
                        )
                        
                await asyncio.sleep(self.rate_limit_delay)
                
        except GithubException as e:
            print(f"Error scraping gists: {e}")

6. Filesystem Scraper

Python

# scrapers/filesystem_scraper.py
import asyncio
import aiofiles
import os
from pathlib import Path
from datetime import datetime
from typing import AsyncIterator, Dict, Any, Set
import fnmatch
import chardet
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .base import BaseScraper, ScrapedItem, SourceType


class FileChangeHandler(FileSystemEventHandler):
    """Handle filesystem changes for live monitoring"""
    
    def __init__(self, callback):
        self.callback = callback
        
    def on_created(self, event):
        if not event.is_directory:
            asyncio.create_task(self.callback(event.src_path, "created"))
            
    def on_modified(self, event):
        if not event.is_directory:
            asyncio.create_task(self.callback(event.src_path, "modified"))


class FilesystemScraper(BaseScraper):
    """Scraper for local filesystem with live monitoring support"""
    
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.observers: list[Observer] = []
        self.seen_hashes: Set[str] = set()
        
    @property
    def source_type(self) -> SourceType:
        return SourceType.LOCAL_FILESYSTEM
    
    async def validate_connection(self) -> bool:
        fs_config = self.config.get("sources", {}).get("filesystem", {})
        paths = fs_config.get("paths", [])
        return any(Path(p).exists() for p in paths)
    
    async def scrape(self) -> AsyncIterator[ScrapedItem]:
        """Scrape configured filesystem paths"""
        fs_config = self.config.get("sources", {}).get("filesystem", {})
        
        if not fs_config.get("enabled", False):
            return
            
        paths = fs_config.get("paths", [])
        patterns = fs_config.get("patterns", ["*"])
        exclude_patterns = fs_config.get("exclude_patterns", [])
        
        for base_path in paths:
            base = Path(base_path)
            if not base.exists():
                print(f"Path does not exist: {base_path}")
                continue
                
            async for item in self._scan_directory(base, patterns, exclude_patterns):
                yield item
    
    async def _scan_directory(
        self, 
        base_path: Path, 
        patterns: list, 
        exclude_patterns: list
    ) -> AsyncIterator[ScrapedItem]:
        """Recursively scan a directory"""
        try:
            for root, dirs, files in os.walk(base_path):
                # Filter excluded directories
                dirs[:] = [d for d in dirs if not any(
                    fnmatch.fnmatch(d, excl.rstrip('/*')) 
                    for excl in exclude_patterns
                )]
                
                for filename in files:
                    filepath = Path(root) / filename
                    
                    # Check if matches any pattern
                    if not any(fnmatch.fnmatch(filename, pat) for pat in patterns):
                        continue
                        
                    # Check if excluded
                    rel_path = str(filepath.relative_to(base_path))
                    if any(fnmatch.fnmatch(rel_path, excl) for excl in exclude_patterns):
                        continue
                    
                    item = await self._process_file(filepath)
                    if item:
                        yield item
                        
        except PermissionError as e:
            print(f"Permission denied: {e}")
    
    async def _process_file(self, filepath: Path) -> ScrapedItem | None:
        """Process a single file"""
        try:
            # Read file with encoding detection
            async with aiofiles.open(filepath, 'rb') as f:
                raw_content = await f.read()
            
            # Skip binary files
            if b'\x00' in raw_content[:1024]:
                return None
                
            # Detect encoding
            detected = chardet.detect(raw_content)
            encoding = detected.get('encoding', 'utf-8') or 'utf-8'
            
            try:
                content = raw_content.decode(encoding)
            except (UnicodeDecodeError, LookupError):
                content = raw_content.decode('utf-8', errors='ignore')
            
            # Check relevance
            is_relevant, confidence = self.is_relevant(content, filepath.name)
            
            if not is_relevant and confidence < 0.1:
                return None
            
            stat = filepath.stat()
            
            return ScrapedItem(
                id=f"local:{filepath.as_posix()}",
                source_type=self.source_type,
                source_path=str(filepath.absolute()),
                content=content,
                content_type=self.detect_content_type(content, filepath.name),
                file_extension=filepath.suffix.lstrip('.'),
                filename=filepath.name,
                metadata={
                    "absolute_path": str(filepath.absolute()),
                    "relative_path": str(filepath),
                    "encoding": encoding
                },
                created_at=datetime.fromtimestamp(stat.st_ctime),
                modified_at=datetime.fromtimestamp(stat.st_mtime),
                size_bytes=stat.st_size,
                language=self.detect_language(content, filepath.name),
                confidence_score=confidence
            )
            
        except Exception as e:
            print(f"Error processing {filepath}: {e}")
            return None
    
    def start_live_monitoring(self, callback):
        """Start monitoring filesystem for changes"""
        fs_config = self.config.get("sources", {}).get("filesystem", {})
        paths = fs_config.get("paths", [])
        
        handler = FileChangeHandler(callback)
        
        for path in paths:
            if Path(path).exists():
                observer = Observer()
                observer.schedule(handler, path, recursive=True)
                observer.start()
                self.observers.append(observer)
                
    def stop_live_monitoring(self):
        """Stop all filesystem monitors"""
        for observer in self.observers:
            observer.stop()
            observer.join()
        self.observers.clear()

7. Data Processor

Python

# processors/processor.py
import hashlib
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
from sentence_transformers import SentenceTransformer
import re
from scrapers.base import ScrapedItem, ContentType


@dataclass
class ProcessedChunk:
    """A processed chunk of content"""
    id: str
    parent_id: str
    content: str
    embedding: List[float]
    chunk_index: int
    total_chunks: int
    metadata: Dict[str, Any]


class DataProcessor:
    """Process and prepare scraped data for storage"""
    
    def __init__(
        self, 
        embedding_model: str = "all-MiniLM-L6-v2",
        chunk_size: int = 1000,
        chunk_overlap: int = 200
    ):
        self.embedding_model = SentenceTransformer(embedding_model)
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.seen_hashes: set = set()
    
    def process(self, item: ScrapedItem) -> List[ProcessedChunk]:
        """Process a scraped item into chunks with embeddings"""
        # Deduplicate
        if item.content_hash in self.seen_hashes:
            return []
        self.seen_hashes.add(item.content_hash)
        
        # Normalize content
        normalized = self._normalize_content(item.content, item.content_type)
        
        # Chunk content
        chunks = self._chunk_content(normalized, item.content_type)
        
        # Create embeddings and processed chunks
        processed = []
        for i, chunk_text in enumerate(chunks):
            embedding = self.embedding_model.encode(chunk_text).tolist()
            
            chunk_id = hashlib.sha256(f"{item.id}:{i}".encode()).hexdigest()[:16]
            
            processed.append(ProcessedChunk(
                id=chunk_id,
                parent_id=item.id,
                content=chunk_text,
                embedding=embedding,
                chunk_index=i,
                total_chunks=len(chunks),
                metadata={
                    "source_type": item.source_type.value,
                    "source_path": item.source_path,
                    "content_type": item.content_type.value,
                    "filename": item.filename,
                    "language": item.language,
                    "confidence_score": item.confidence_score,
                    "original_metadata": item.metadata
                }
            ))
            
        return processed
    
    def _normalize_content(self, content: str, content_type: ContentType) -> str:
        """Normalize content based on type"""
        # Remove excessive whitespace
        content = re.sub(r'\n{3,}', '\n\n', content)
        content = re.sub(r' {2,}', ' ', content)
        
        if content_type == ContentType.SOURCE_CODE:
            # Preserve code structure but normalize
            content = self._normalize_code(content)
        elif content_type == ContentType.DOCUMENTATION:
            # Clean up documentation
            content = self._normalize_docs(content)
            
        return content.strip()
    
    def _normalize_code(self, content: str) -> str:
        """Normalize source code"""
        lines = content.split('\n')
        normalized_lines = []
        
        for line in lines:
            # Remove trailing whitespace
            line = line.rstrip()
            normalized_lines.append(line)
            
        return '\n'.join(normalized_lines)
    
    def _normalize_docs(self, content: str) -> str:
        """Normalize documentation"""
        # Remove HTML tags if present
        content = re.sub(r'<[^>]+>', '', content)
        return content
    
    def _chunk_content(self, content: str, content_type: ContentType) -> List[str]:
        """Chunk content appropriately based on type"""
        if content_type == ContentType.SOURCE_CODE:
            return self._chunk_code(content)
        else:
            return self._chunk_text(content)
    
    def _chunk_code(self, content: str) -> List[str]:
        """Chunk source code by logical units"""
        chunks = []
        
        # Try to split by functions/classes first
        patterns = [
            r'((?:def|async def)\s+\w+[^:]*:.*?)(?=\n(?:def|async def|class)\s|\Z)',
            r'(class\s+\w+[^:]*:.*?)(?=\nclass\s|\Z)',
            r'(function\s+\w+[^{]*\{.*?\n\})',
        ]
        
        remaining = content
        
        for pattern in patterns:
            matches = re.findall(pattern, remaining, re.DOTALL)
            for match in matches:
                if len(match) <= self.chunk_size:
                    chunks.append(match)
                else:
                    # Further split large functions
                    chunks.extend(self._chunk_text(match))
                remaining = remaining.replace(match, '', 1)
        
        # Chunk any remaining content
        if remaining.strip():
            chunks.extend(self._chunk_text(remaining))
            
        return chunks if chunks else self._chunk_text(content)
    
    def _chunk_text(self, content: str) -> List[str]:
        """Chunk text with overlap"""
        if len(content) <= self.chunk_size:
            return [content]
            
        chunks = []
        start = 0
        
        while start < len(content):
            end = start + self.chunk_size
            
            # Try to break at sentence boundary
            if end < len(content):
                for sep in ['. ', '.\n', '\n\n', '\n', ' ']:
                    last_sep = content[start:end].rfind(sep)
                    if last_sep > self.chunk_size // 2:
                        end = start + last_sep + len(sep)
                        break
            
            chunks.append(content[start:end].strip())
            start = end - self.chunk_overlap
            
        return chunks
    
    def compute_similarity(self, text1: str, text2: str) -> float:
        """Compute similarity between two texts"""
        emb1 = self.embedding_model.encode(text1)
        emb2 = self.embedding_model.encode(text2)
        
        # Cosine similarity
        dot = sum(a * b for a, b in zip(emb1, emb2))
        norm1 = sum(a * a for a in emb1) ** 0.5
        norm2 = sum(a * a for a in emb2) ** 0.5
        
        return dot / (norm1 * norm2) if norm1 and norm2 else 0.0

8. Argilla Integration

Python

# argilla_integration/datasets.py
import argilla as rg
from typing import List, Dict, Any, Optional
from datetime import datetime
from processors.processor import ProcessedChunk
from scrapers.base import ScrapedItem


class ArgillaManager:
    """Manage Argilla datasets for data curation"""
    
    def __init__(
        self, 
        api_url: str, 
        api_key: str,
        workspace: str = "project_recovery"
    ):
        rg.init(api_url=api_url, api_key=api_key)
        self.workspace = workspace
        self._ensure_workspace()
        
    def _ensure_workspace(self):
        """Ensure workspace exists"""
        try:
            rg.Workspace.create(self.workspace)
        except Exception:
            pass  # Already exists
    
    def create_recovery_dataset(self, name: str = "recovered_data") -> rg.Dataset:
        """Create a dataset for recovered project data"""
        settings = rg.Settings(
            fields=[
                rg.TextField(name="content", title="Content"),
                rg.TextField(name="source_path", title="Source Path"),
                rg.TextField(name="filename", title="Filename", required=False),
            ],
            questions=[
                rg.LabelQuestion(
                    name="relevance",
                    title="Is this relevant to the project?",
                    labels=["relevant", "maybe_relevant", "not_relevant"],
                ),
                rg.LabelQuestion(
                    name="content_type",
                    title="Content Type",
                    labels=[
                        "core_code", 
                        "utility", 
                        "configuration", 
                        "documentation",
                        "test",
                        "data",
                        "other"
                    ],
                ),
                rg.LabelQuestion(
                    name="quality",
                    title="Code/Content Quality",
                    labels=["high", "medium", "low", "needs_review"],
                ),
                rg.TextQuestion(
                    name="notes",
                    title="Notes / What is this?",
                    required=False,
                ),
                rg.LabelQuestion(
                    name="action",
                    title="Recommended Action",
                    labels=[
                        "include_as_is",
                        "needs_update",
                        "reference_only",
                        "discard"
                    ],
                ),
            ],
            metadata=[
                rg.TermsMetadataProperty(name="source_type"),
                rg.TermsMetadataProperty(name="language"),
                rg.FloatMetadataProperty(name="confidence_score"),
                rg.TermsMetadataProperty(name="file_extension"),
            ],
        )
        
        dataset = rg.Dataset(
            name=name,
            workspace=self.workspace,
            settings=settings,
        )
        
        try:
            dataset.create()
        except Exception:
            # Dataset exists, get it
            dataset = rg.Dataset.from_argilla(name=name, workspace=self.workspace)
            
        return dataset
    
    def add_items_to_dataset(
        self, 
        dataset: rg.Dataset, 
        items: List[ScrapedItem]
    ) -> int:
        """Add scraped items to Argilla dataset"""
        records = []
        
        for item in items:
            record = rg.Record(
                fields={
                    "content": item.content[:10000],  # Limit content size
                    "source_path": item.source_path,
                    "filename": item.filename or "",
                },
                metadata={
                    "source_type": item.source_type.value,
                    "language": item.language or "unknown",
                    "confidence_score": item.confidence_score,
                    "file_extension": item.file_extension or "none",
                },
                id=item.id,
            )
            records.append(record)
        
        if records:
            dataset.records.log(records)
            
        return len(records)
    
    def get_labeled_data(
        self, 
        dataset_name: str,
        status: str = "completed"
    ) -> List[Dict[str, Any]]:
        """Get labeled data from Argilla"""
        dataset = rg.Dataset.from_argilla(name=dataset_name, workspace=self.workspace)
        
        labeled_items = []
        
        for record in dataset.records:
            if record.status == status:
                responses = {}
                for response in record.responses:
                    responses.update(response.values)
                    
                labeled_items.append({
                    "id": record.id,
                    "content": record.fields.get("content"),
                    "source_path": record.fields.get("source_path"),
                    "filename": record.fields.get("filename"),
                    "metadata": record.metadata,
                    "labels": responses
                })
                
        return labeled_items
    
    def export_curated_data(
        self, 
        dataset_name: str,
        output_path: str,
        filter_action: List[str] = None
    ) -> int:
        """Export curated data to files"""
        import json
        from pathlib import Path
        
        filter_action = filter_action or ["include_as_is", "needs_update"]
        
        labeled = self.get_labeled_data(dataset_name)
        
        filtered = [
            item for item in labeled 
            if item.get("labels", {}).get("action") in filter_action
        ]
        
        output = Path(output_path)
        output.mkdir(parents=True, exist_ok=True)
        
        # Export as JSON
        with open(output / "curated_data.json", "w") as f:
            json.dump(filtered, f, indent=2, default=str)
            
        # Also export individual files
        for item in filtered:
            filename = item.get("filename") or f"{item['id']}.txt"
            file_path = output / "files" / filename
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, "w") as f:
                f.write(item["content"])
                
        return len(filtered)

9. Vector Storage

Python

# storage/vector_store.py
from qdrant_client import QdrantClient
from qdrant_client.http import models
from typing import List, Dict, Any, Optional
from processors.processor import ProcessedChunk


class VectorStore:
    """Vector database for semantic search over recovered data"""
    
    def __init__(
        self, 
        url: str = "http://localhost:6333",
        collection_name: str = "project_fragments"
    ):
        self.client = QdrantClient(url=url)
        self.collection_name = collection_name
        self._ensure_collection()
    
    def _ensure_collection(self, vector_size: int = 384):
        """Ensure collection exists"""
        collections = self.client.get_collections().collections
        exists = any(c.name == self.collection_name for c in collections)
        
        if not exists:
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=vector_size,
                    distance=models.Distance.COSINE
                )
            )
            
            # Create payload indexes
            self.client.create_payload_index(
                collection_name=self.collection_name,
                field_name="source_type",
                field_schema=models.PayloadSchemaType.KEYWORD
            )
            self.client.create_payload_index(
                collection_name=self.collection_name,
                field_name="content_type",
                field_schema=models.PayloadSchemaType.KEYWORD
            )
            self.client.create_payload_index(
                collection_name=self.collection_name,
                field_name="language",
                field_schema=models.PayloadSchemaType.KEYWORD
            )
    
    def upsert_chunks(self, chunks: List[ProcessedChunk]) -> int:
        """Insert or update chunks in vector store"""
        if not chunks:
            return 0
            
        points = [
            models.PointStruct(
                id=hash(chunk.id) % (2**63),  # Convert to int
                vector=chunk.embedding,
                payload={
                    "chunk_id": chunk.id,
                    "parent_id": chunk.parent_id,
                    "content": chunk.content,
                    "chunk_index": chunk.chunk_index,
                    "total_chunks": chunk.total_chunks,
                    **chunk.metadata
                }
            )
            for chunk in chunks
        ]
        
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
        
        return len(points)
    
    def search(
        self, 
        query_vector: List[float],
        limit: int = 10,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Semantic search over stored chunks"""
        filter_conditions = []
        
        if filters:
            for key, value in filters.items():
                if isinstance(value, list):
                    filter_conditions.append(
                        models.FieldCondition(
                            key=key,
                            match=models.MatchAny(any=value)
                        )
                    )
                else:
                    filter_conditions.append(
                        models.FieldCondition(
                            key=key,
                            match=models.MatchValue(value=value)
                        )
                    )
        
        query_filter = models.Filter(must=filter_conditions) if filter_conditions else None
        
        results = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            query_filter=query_filter,
            limit=limit,
            with_payload=True
        )
        
        return [
            {
                "score": hit.score,
                **hit.payload
            }
            for hit in results
        ]
    
    def search_by_text(
        self, 
        query: str,
        embedding_model,
        limit: int = 10,
        filters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Search using text query"""
        query_vector = embedding_model.encode(query).tolist()
        return self.search(query_vector, limit, filters)
    
    def find_similar(
        self, 
        content: str,
        embedding_model,
        threshold: float = 0.8,
        limit: int = 5
    ) -> List[Dict[str, Any]]:
        """Find similar content (for deduplication)"""
        results = self.search_by_text(content, embedding_model, limit)
        return [r for r in results if r["score"] >= threshold]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get collection statistics"""
        info = self.client.get_collection(self.collection_name)
        
        return {
            "total_points": info.points_count,
            "vectors_count": info.vectors_count,
            "indexed_points": info.indexed_vectors_count
        }
    
    def delete_by_source(self, source_type: str):
        """Delete all chunks from a specific source"""
        self.client.delete(
            collection_name=self.collection_name,
            points_selector=models.FilterSelector(
                filter=models.Filter(
                    must=[
                        models.FieldCondition(
                            key="source_type",
                            match=models.MatchValue(value=source_type)
                        )
                    ]
                )
            )
        )

10. Pipeline Orchestrator

Python

# orchestrator/pipeline.py
import asyncio
from typing import List, Dict, Any, Optional
from datetime import datetime
from dataclasses import dataclass
from enum import Enum
import logging

from scrapers.base import ScrapedItem, SourceType
from scrapers.github_scraper import GitHubScraper
from scrapers.filesystem_scraper import FilesystemScraper
from processors.processor import DataProcessor
from storage.vector_store import VectorStore
from argilla_integration.datasets import ArgillaManager
from config.settings import settings, load_sources_config


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PipelineStatus(Enum):
    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"
    ERROR = "error"


@dataclass
class PipelineRun:
    id: str
    started_at: datetime
    ended_at: Optional[datetime] = None
    status: PipelineStatus = PipelineStatus.RUNNING
    items_scraped: int = 0
    items_processed: int = 0
    items_stored: int = 0
    errors: List[str] = None
    
    def __post_init__(self):
        if self.errors is None:
            self.errors = []


class RecoveryPipeline:
    """Main pipeline for recovering and organizing project data"""
    
    def __init__(self):
        self.config = load_sources_config()
        self.processor = DataProcessor(
            embedding_model=settings.embedding_model,
            chunk_size=settings.chunk_size,
            chunk_overlap=settings.chunk_overlap
        )
        self.vector_store = VectorStore(
            url=settings.qdrant_url,
            collection_name=settings.qdrant_collection
        )
        self.argilla = ArgillaManager(
            api_url=settings.argilla_api_url,
            api_key=settings.argilla_api_key,
            workspace=settings.argilla_workspace
        )
        
        # Initialize scrapers
        self.scrapers = self._init_scrapers()
        
        # State
        self.status = PipelineStatus.IDLE
        self.current_run: Optional[PipelineRun] = None
        self.runs_history: List[PipelineRun] = []
        
        # Buffers
        self.item_buffer: List[ScrapedItem] = []
        self.buffer_size = 50
        
    def _init_scrapers(self) -> Dict[SourceType, Any]:
        """Initialize all configured scrapers"""
        scrapers = {}
        
        # GitHub scraper
        scrapers[SourceType.GITHUB] = GitHubScraper(
            self.config,
            token=settings.github_token
        )
        
        # Filesystem scraper
        scrapers[SourceType.LOCAL_FILESYSTEM] = FilesystemScraper(self.config)
        
        # Add more scrapers as needed
        
        return scrapers
    
    async def run_full_pipeline(self) -> PipelineRun:
        """Run the complete recovery pipeline"""
        run = PipelineRun(
            id=f"run_{datetime.utcnow().strftime('%Y%m%d_%H%M%S')}",
            started_at=datetime.utcnow()
        )
        self.current_run = run
        self.status = PipelineStatus.RUNNING
        
        logger.info(f"Starting pipeline run: {run.id}")
        
        try:
            # Create Argilla dataset for this run
            dataset = self.argilla.create_recovery_dataset(
                name=f"recovery_{run.id}"
            )
            
            # Run all scrapers
            for source_type, scraper in self.scrapers.items():
                logger.info(f"Running scraper: {source_type.value}")
                
                try:
                    if await scraper.validate_connection():
                        async for item in scraper.scrape():
                            run.items_scraped += 1
                            await self._process_item(item, dataset, run)
                            
                            if run.items_scraped % 100 == 0:
                                logger.info(f"Scraped {run.items_scraped} items...")
                    else:
                        logger.warning(f"Could not connect to {source_type.value}")
                        
                except Exception as e:
                    error_msg = f"Error in {source_type.value}: {str(e)}"
                    logger.error(error_msg)
                    run.errors.append(error_msg)
            
            # Flush remaining buffer
            await self._flush_buffer(dataset, run)
            
            run.status = PipelineStatus.IDLE
            
        except Exception as e:
            run.status = PipelineStatus.ERROR
            run.errors.append(f"Pipeline error: {str(e)}")
            logger.error(f"Pipeline failed: {e}")
            
        finally:
            run.ended_at = datetime.utcnow()
            self.runs_history.append(run)
            self.status = PipelineStatus.IDLE
            self.current_run = None
            
        logger.info(f"Pipeline complete. Scraped: {run.items_scraped}, "
                   f"Processed: {run.items_processed}, Stored: {run.items_stored}")
        
        return run
    
    async def _process_item(
        self, 
        item: ScrapedItem, 
        dataset,
        run: PipelineRun
    ):
        """Process a single scraped item"""
        self.item_buffer.append(item)
        
        if len(self.item_buffer) >= self.buffer_size:
            await self._flush_buffer(dataset, run)
    
    async def _flush_buffer(self, dataset, run: PipelineRun):
        """Flush item buffer to storage"""
        if not self.item_buffer:
            return
            
        # Process items
        all_chunks = []
        for item in self.item_buffer:
            chunks = self.processor.process(item)
            all_chunks.extend(chunks)
            run.items_processed += 1
        
        # Store in vector DB
        if all_chunks:
            stored = self.vector_store.upsert_chunks(all_chunks)
            run.items_stored += stored
        
        # Add to Argilla for labeling
        self.argilla.add_items_to_dataset(dataset, self.item_buffer)
        
        # Clear buffer
        self.item_buffer.clear()
    
    def search_recovered_data(
        self, 
        query: str,
        limit: int = 10,
        filters: Optional[Dict] = None
    ) -> List[Dict[str, Any]]:
        """Search through recovered data"""
        return self.vector_store.search_by_text(
            query,
            self.processor.embedding_model,
            limit,
            filters
        )
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get current system statistics"""
        vector_stats = self.vector_store.get_statistics()
        
        return {
            "status": self.status.value,
            "vector_store": vector_stats,
            "total_runs": len(self.runs_history),
            "last_run": self.runs_history[-1] if self.runs_history else None
        }

11. Celery Tasks (Self-Sustaining Scheduler)

Python

# orchestrator/tasks.py
from celery import Celery
from celery.schedules import crontab
import asyncio
from datetime import datetime
from config.settings import settings

# Initialize Celery
app = Celery(
    'recovery_tasks',
    broker=settings.redis_url,
    backend=settings.redis_url
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)

# Scheduled tasks
app.conf.beat_schedule = {
    # Run full pipeline every 6 hours
    'run-full-recovery': {
        'task': 'orchestrator.tasks.run_recovery_pipeline',
        'schedule': crontab(minute=0, hour=f'*/{settings.scrape_interval_hours}'),
    },
    # Quick filesystem scan every hour
    'quick-filesystem-scan': {
        'task': 'orchestrator.tasks.run_filesystem_scan',
        'schedule': crontab(minute=0),
    },
    # Cleanup old data weekly
    'weekly-cleanup': {
        'task': 'orchestrator.tasks.cleanup_old_runs',
        'schedule': crontab(day_of_week=0, hour=3, minute=0),
    },
    # Export curated data daily
    'daily-export': {
        'task': 'orchestrator.tasks.export_curated_data',
        'schedule': crontab(hour=2, minute=0),
    },
}


def run_async(coro):
    """Helper to run async functions in Celery tasks"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        return loop.run_until_complete(coro)
    finally:
        loop.close()


@app.task(bind=True, max_retries=3)
def run_recovery_pipeline(self):
    """Run the full recovery pipeline"""
    from orchestrator.pipeline import RecoveryPipeline
    
    try:
        pipeline = RecoveryPipeline()
        result = run_async(pipeline.run_full_pipeline())
        
        return {
            "run_id": result.id,
            "status": result.status.value,
            "items_scraped": result.items_scraped,
            "items_processed": result.items_processed,
            "items_stored": result.items_stored,
            "errors": result.errors
        }
        
    except Exception as e:
        self.retry(exc=e, countdown=60 * 5)  # Retry in 5 minutes


@app.task
def run_filesystem_scan():
    """Quick filesystem scan for new/modified files"""
    from orchestrator.pipeline import RecoveryPipeline
    from scrapers.base import SourceType
    
    pipeline = RecoveryPipeline()
    scraper = pipeline.scrapers[SourceType.LOCAL_FILESYSTEM]
    
    items_found = 0
    
    async def scan():
        nonlocal items_found
        async for item in scraper.scrape():
            chunks = pipeline.processor.process(item)
            if chunks:
                pipeline.vector_store.upsert_chunks(chunks)
                items_found += 1
    
    run_async(scan())
    
    return {"items_found": items_found, "timestamp": datetime.utcnow().isoformat()}


@app.task
def cleanup_old_runs(days: int = 30):
    """Clean up old pipeline runs and temporary data"""
    import shutil
    from pathlib import Path
    
    # Clean up old temporary files
    temp_dir = Path("/app/data/temp")
    if temp_dir.exists():
        for item in temp_dir.iterdir():
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()
    
    return {"status": "cleaned", "timestamp": datetime.utcnow().isoformat()}


@app.task
def export_curated_data():
    """Export curated data from Argilla"""
    from orchestrator.pipeline import RecoveryPipeline
    from pathlib import Path
    from datetime import datetime
    
    pipeline = RecoveryPipeline()
    
    export_dir = Path("/app/data/exports") / datetime.utcnow().strftime("%Y%m%d")
    
    # Find the latest dataset
    # This is simplified - you'd want to track dataset names
    try:
        count = pipeline.argilla.export_curated_data(
            "recovery_latest",
            str(export_dir)
        )
        return {"exported": count, "path": str(export_dir)}
    except Exception as e:
        return {"error": str(e)}


@app.task
def process_single_file(file_path: str):
    """Process a single file on demand"""
    from orchestrator.pipeline import RecoveryPipeline
    from scrapers.filesystem_scraper import FilesystemScraper
    from pathlib import Path
    
    pipeline = RecoveryPipeline()
    scraper = pipeline.scrapers.get(SourceType.LOCAL_FILESYSTEM)
    
    if scraper:
        item = run_async(scraper._process_file(Path(file_path)))
        if item:
            chunks = pipeline.processor.process(item)
            if chunks:
                pipeline.vector_store.upsert_chunks(chunks)
                return {"status": "processed", "chunks": len(chunks)}
    
    return {"status": "skipped"}

12. FastAPI Interface

Python

# api/main.py
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import asyncio

from orchestrator.pipeline import RecoveryPipeline
from orchestrator.tasks import run_recovery_pipeline, process_single_file

app = FastAPI(
    title="Project Recovery System",
    description="Self-sustaining system for recovering and organizing lost project data"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global pipeline instance
pipeline = None


@app.on_event("startup")
async def startup():
    global pipeline
    pipeline = RecoveryPipeline()


# Request/Response Models
class SearchQuery(BaseModel):
    query: str
    limit: int = 10
    filters: Optional[Dict[str, Any]] = None


class SearchResult(BaseModel):
    score: float
    content: str
    source_path: str
    source_type: str
    filename: Optional[str]
    language: Optional[str]


class PipelineRunResponse(BaseModel):
    run_id: str
    status: str
    items_scraped: int
    items_processed: int
    items_stored: int


class FileProcessRequest(BaseModel):
    file_path: str


# Endpoints
@app.get("/health")
async def health_check():
    return {"status": "healthy", "pipeline_status": pipeline.status.value if pipeline else "not_initialized"}


@app.get("/stats")
async def get_statistics():
    """Get system statistics"""
    return pipeline.get_statistics()


@app.post("/search", response_model=List[SearchResult])
async def search(query: SearchQuery):
    """Search through recovered data"""
    results = pipeline.search_recovered_data(
        query.query,
        query.limit,
        query.filters
    )
    
    return [
        SearchResult(
            score=r["score"],
            content=r["content"],
            source_path=r.get("source_path", ""),
            source_type=r.get("source_type", "unknown"),
            filename=r.get("filename"),
            language=r.get("language")
        )
        for r in results
    ]


@app.post("/run", response_model=PipelineRunResponse)
async def run_pipeline(background_tasks: BackgroundTasks):
    """Trigger a full pipeline run"""
    if pipeline.status.value == "running":
        raise HTTPException(status_code=409, detail="Pipeline already running")
    
    # Queue the task
    task = run_recovery_pipeline.delay()
    
    return PipelineRunResponse(
        run_id=task.id,
        status="queued",
        items_scraped=0,
        items_processed=0,
        items_stored=0
    )


@app.post("/process-file")
async def process_file(request: FileProcessRequest, background_tasks: BackgroundTasks):
    """Process a single file"""
    task = process_single_file.delay(request.file_path)
    return {"task_id": task.id, "status": "queued"}


@app.get("/runs")
async def get_runs():
    """Get pipeline run history"""
    return [
        {
            "id": run.id,
            "started_at": run.started_at.isoformat(),
            "ended_at": run.ended_at.isoformat() if run.ended_at else None,
            "status": run.status.value,
            "items_scraped": run.items_scraped,
            "items_processed": run.items_processed,
            "items_stored": run.items_stored,
            "errors": run.errors
        }
        for run in pipeline.runs_history
    ]


@app.get("/sources")
async def get_sources():
    """Get configured sources"""
    from config.settings import load_sources_config
    return load_sources_config()


@app.post("/sources/{source_type}/rescan")
async def rescan_source(source_type: str, background_tasks: BackgroundTasks):
    """Trigger rescan of a specific source"""
    # Implementation would trigger source-specific scraping
    return {"status": "queued", "source": source_type}

13. Dashboard UI

Python

# ui/dashboard.py
import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="Project Recovery Dashboard",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Project Recovery System")

# Sidebar
with st.sidebar:
    st.header("Controls")
    
    if st.button("🚀 Run Full Pipeline", type="primary"):
        response = requests.post(f"{API_URL}/run")
        if response.ok:
            st.success("Pipeline started!")
        else:
            st.error("Failed to start pipeline")
    
    st.divider()
    
    # Stats
    try:
        stats = requests.get(f"{API_URL}/stats").json()
        st.metric("Status", stats.get("status", "unknown"))
        st.metric("Total Items", stats.get("vector_store", {}).get("total_points", 0))
        st.metric("Total Runs", stats.get("total_runs", 0))
    except:
        st.warning("Could not fetch stats")

# Main content
tab1, tab2, tab3, tab4 = st.tabs(["Search", "Runs", "Sources", "Export"])

with tab1:
    st.header("Search Recovered Data")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        query = st.text_input("Search query", placeholder="Enter keywords...")
    
    with col2:
        limit = st.number_input("Results", min_value=1, max_value=50, value=10)
    
    # Filters
    with st.expander("Filters"):
        col1, col2, col3 = st.columns(3)
        with col1:
            source_filter = st.multiselect(
                "Source Type",
                ["github", "local_filesystem", "google_drive", "email"]
            )
        with col2:
            content_filter = st.multiselect(
                "Content Type",
                ["source_code", "documentation", "configuration", "data"]
            )
        with col3:
            lang_filter = st.multiselect(
                "Language",
                ["python", "javascript", "typescript", "rust", "go"]
            )
    
    if query:
        filters = {}
        if source_filter:
            filters["source_type"] = source_filter
        if content_filter:
            filters["content_type"] = content_filter
        if lang_filter:
            filters["language"] = lang_filter
        
        try:
            response = requests.post(
                f"{API_URL}/search",
                json={"query": query, "limit": limit, "filters": filters if filters else None}
            )
            results = response.json()
            
            if results:
                st.success(f"Found {len(results)} results")
                
                for i, result in enumerate(results):
                    with st.expander(
                        f"[{result['score']:.2f}] {result.get('filename', 'Unknown')} - {result['source_type']}"
                    ):
                        st.caption(f"Source: {result['source_path']}")
                        if result.get('language'):
                            st.caption(f"Language: {result['language']}")
                        st.code(result['content'][:2000], language=result.get('language'))
            else:
                st.info("No results found")
                
        except Exception as e:
            st.error(f"Search failed: {e}")

with tab2:
    st.header("Pipeline Runs")
    
    if st.button("🔄 Refresh"):
        st.rerun()
    
    try:
        runs = requests.get(f"{API_URL}/runs").json()
        
        if runs:
            df = pd.DataFrame(runs)
            
            # Summary chart
            fig = px.bar(
                df,
                x="id",
                y=["items_scraped", "items_processed", "items_stored"],
                title="Items per Run",
                barmode="group"
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Runs table
            st.dataframe(
                df[["id", "status", "items_scraped", "items_processed", "started_at"]],
                use_container_width=True
            )
        else:
            st.info("No runs yet")
            
    except Exception as e:
        st.error(f"Could not fetch runs: {e}")

with tab3:
    st.header("Configured Sources")
    
    try:
        sources = requests.get(f"{API_URL}/sources").json()
        
        for source_name, config in sources.get("sources", {}).items():
            with st.expander(f"📂 {source_name.upper()}", expanded=config.get("enabled", False)):
                st.json(config)
                
                if st.button(f"Rescan {source_name}", key=f"rescan_{source_name}"):
                    requests.post(f"{API_URL}/sources/{source_name}/rescan")
                    st.success(f"Rescan queued for {source_name}")
                    
    except Exception as e:
        st.error(f"Could not fetch sources: {e}")

with tab4:
    st.header("Export Curated Data")
    
    st.write("Export data that has been reviewed and labeled in Argilla.")
    
    export_path = st.text_input("Export path", value="./exports")
    
    col1, col2 = st.columns(2)
    
    with col1:
        include_actions = st.multiselect(
            "Include items with action",
            ["include_as_is", "needs_update", "reference_only"],
            default=["include_as_is", "needs_update"]
        )
    
    with col2:
        export_format = st.selectbox(
            "Format",
            ["JSON", "Individual Files", "Both"]
        )
    
    if st.button("📦 Export", type="primary"):
        st.info("Export functionality would be triggered here")
        # Would call export endpoint

# Footer
st.divider()
st.caption("Project Recovery System v1.0 | Built with Argilla, Qdrant, and FastAPI")

14. Main Entry Point

Python

# main.py
import asyncio
import argparse
import uvicorn
from rich.console import Console
from rich.table import Table

console = Console()


def run_api():
    """Run the FastAPI server"""
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )


def run_dashboard():
    """Run the Streamlit dashboard"""
    import subprocess
    subprocess.run(["streamlit", "run", "ui/dashboard.py", "--server.port", "8501"])


async def run_pipeline_once():
    """Run the pipeline once"""
    from orchestrator.pipeline import RecoveryPipeline
    
    console.print("[bold blue]Starting Project Recovery Pipeline[/bold blue]")
    
    pipeline = RecoveryPipeline()
    result = await pipeline.run_full_pipeline()
    
    # Display results
    table = Table(title="Pipeline Run Results")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Run ID", result.id)
    table.add_row("Status", result.status.value)
    table.add_row("Items Scraped", str(result.items_scraped))
    table.add_row("Items Processed", str(result.items_processed))
    table.add_row("Items Stored", str(result.items_stored))
    table.add_row("Errors", str(len(result.errors)))
    
    console.print(table)
    
    if result.errors:
        console.print("[yellow]Errors:[/yellow]")
        for error in result.errors:
            console.print(f"  - {error}")


def run_worker():
    """Run Celery worker"""
    from orchestrator.tasks import app
    app.worker_main(['worker', '--loglevel=info'])


def run_beat():
    """Run Celery beat scheduler"""
    from orchestrator.tasks import app
    app.worker_main(['beat', '--loglevel=info'])


def main():
    parser = argparse.ArgumentParser(description="Project Recovery System")
    parser.add_argument(
        "command",
        choices=["api", "dashboard", "pipeline", "worker", "beat", "all"],
        help="Command to run"
    )
    
    args = parser.parse_args()
    
    if args.command == "api":
        run_api()
    elif args.command == "dashboard":
        run_dashboard()
    elif args.command == "pipeline":
        asyncio.run(run_pipeline_once())
    elif args.command == "worker":
        run_worker()
    elif args.command == "beat":
        run_beat()
    elif args.command == "all":
        console.print("[bold]Use docker-compose to run all services[/bold]")


if __name__ == "__main__":
    main()

Quick Start

Bash

# 1. Clone and setup
mkdir project-recovery && cd project-recovery

# 2. Create .env file
cat > .env << EOF
GITHUB_TOKEN=your_github_token
ARGILLA_API_KEY=admin.apikey
EOF

# 3. Configure sources (edit config/sources.yaml)

# 4. Start all services
docker-compose up -d

# 5. Access services
# - API: http://localhost:8000
# - Argilla UI: http://localhost:6900
# - Dashboard: http://localhost:8501

# 6. Run pipeline manually (optional)
docker-compose exec recovery_system python main.py pipeline

Workflow

text

1. SCRAPE ──────────────────────────────────────────────┐
   │                                                     │
   ├─► GitHub (repos, gists, search)                    │
   ├─► Local filesystem (with patterns)                 │
   ├─► Cloud storage (GDrive, Dropbox)                  │
   └─► Email attachments                                │
                                                        ▼
2. PROCESS ─────────────────────────────────────────────┐
   │                                                     │
   ├─► Normalize content                                │
   ├─► Detect language/type                             │
   ├─► Chunk for embeddings                             │
   ├─► Generate embeddings                              │
   └─► Deduplicate                                      │
                                                        ▼
3. STORE ───────────────────────────────────────────────┐
   │                                                     │
   ├─► Vector DB (Qdrant) - for semantic search         │
   ├─► PostgreSQL - metadata and relationships          │
   └─► Argilla - for human review/labeling              │
                                                        ▼
4. CURATE (in Argilla) ─────────────────────────────────┐
   │                                                     │
   ├─► Label relevance                                  │
   ├─► Categorize content type                          │
   ├─► Add notes/context                                │
   └─► Mark actions (include/update/discard)            │
                                                        ▼
5. EXPORT ──────────────────────────────────────────────┐
   │                                                     │
   └─► Reconstructed project files                      │

This system will continuously scan your configured sources, process and organize the data, and present it in Argilla for you to review and curate. The labeled data can then be exported to reconstruct your project!

    i need to make a use https://github.com/namurokuro/argilla-cookbook to make a self sustaining scraping and ingesting unit to help me collect and organize my lost project data in order to rebuild it

Something went wrong while generating the response. Please try again.

Inputs are processed by third-party AI and responses    \Ида заппоччваяме да да строим тук  D:\LaLaLand
https://github.com/MAGArENKO/LaLaland

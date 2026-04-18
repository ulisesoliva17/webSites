import re

css_path = '/Users/ulisesoliva/Desktop/WEB/webSites/frontend/css/style.css'
with open(css_path, 'r') as f:
    content = f.read()

# The new CSS to insert
new_css = """/* =========================================
   INTERACTIVE 3D SCENE
   ========================================= */
.scene-3d {
    width: 100%;
    height: 450px;
    perspective: 1200px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.grid-3d {
    position: relative;
    width: 240px;
    height: 240px;
    transform-style: preserve-3d;
    transform: rotateX(55deg) rotateZ(-45deg);
    animation: floatScene 6s ease-in-out infinite;
}

@keyframes floatScene {
    0% { transform: rotateX(55deg) rotateZ(-45deg) translateZ(0px); }
    50% { transform: rotateX(55deg) rotateZ(-45deg) translateZ(15px); }
    100% { transform: rotateX(55deg) rotateZ(-45deg) translateZ(0px); }
}

.cube-sector {
    position: absolute;
    width: 100px;
    height: 100px;
    transform-style: preserve-3d;
    transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    cursor: pointer;
}

.cube-sector:hover {
    transform: translateZ(40px);
}

.sector-1 { top: 10px; left: 10px; }
.sector-2 { top: 10px; left: 130px; }
.sector-3 { top: 130px; left: 10px; }
.sector-4 { top: 130px; left: 130px; }

.face {
    position: absolute;
    top: 50%; left: 50%;
    transform-style: preserve-3d;
    background: #111116;
    border: 1px solid rgba(255, 255, 255, 0.1);
    transition: all 0.4s ease;
}

.face.top {
    width: 100px; height: 100px;
    transform: translate(-50%, -50%) translateZ(20px);
    background: #16161e;
}
.face.bottom {
    width: 100px; height: 100px;
    transform: translate(-50%, -50%) translateZ(-20px) rotateX(180deg);
}
.face.front {
    width: 100px; height: 40px;
    transform: translate(-50%, -50%) translateY(50px) rotateX(-90deg);
}
.face.back {
    width: 100px; height: 40px;
    transform: translate(-50%, -50%) translateY(-50px) rotateX(90deg);
}
.face.left {
    width: 40px; height: 100px;
    transform: translate(-50%, -50%) translateX(-50px) rotateY(-90deg);
}
.face.right {
    width: 40px; height: 100px;
    transform: translate(-50%, -50%) translateX(50px) rotateY(90deg);
}

/* TECH DETAILS ON TOP FACE */
.tech-pattern {
    width: 100%; height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 8px;
    background-image: 
        linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px);
    background-size: 10px 10px;
    opacity: 0.6;
    transition: all 0.5s ease;
}

/* Base style for specific tech nodes */
.server-node { width: 60%; height: 10px; background: #222; border: 1px solid #444; border-radius: 2px; }
.core-chip { width: 30px; height: 30px; background: #222; border: 2px solid #444; border-radius: 4px; position: relative; }
.core-chip::before { content: ''; position: absolute; width: 50px; height: 2px; background: #333; top: 12px; left: -12px; z-index: -1; }
.core-chip::after { content: ''; position: absolute; width: 2px; height: 50px; background: #333; top: -12px; left: 12px; z-index: -1; }
.net-circle { width: 15px; height: 15px; border-radius: 50%; background: #333; border: 2px solid #444; position: absolute; }
.sector-3 .c1 { top: 20px; left: 20px; }
.sector-3 .c2 { top: 60px; left: 60px; }
.sector-3 .c3 { top: 20px; left: 60px; }
.line-link { position: absolute; background: #333; }
.sector-3 .l1 { top: 26px; left: 35px; width: 25px; height: 2px; }
.sector-3 .l2 { top: 35px; left: 66px; width: 2px; height: 25px; }
.sector-3 .l3 { top: 30px; left: 30px; width: 40px; height: 2px; transform: rotate(45deg); transform-origin: left; }
.db-ring { width: 40px; height: 15px; border: 2px solid #444; border-radius: 50%; margin-bottom: -5px; background: #222;}

/* SECTOR 1 HOVER (Green) */
.sector-1:hover .face { border-color: #00ff64; background: #112218; box-shadow: inset 0 0 20px rgba(0, 255, 100, 0.2); }
.sector-1:hover .face.top { background: #153322; }
.sector-1:hover .tech-pattern { opacity: 1; filter: drop-shadow(0 0 10px #00ff64); }
.sector-1:hover .server-node { background: #00ff64; border-color: #fff; animation: pulseLight 1s infinite alternate; }
.sector-1:hover .delay-a { animation-delay: 0.2s; }
.sector-1:hover .delay-b { animation-delay: 0.4s; }
.sector-1:hover .delay-c { animation-delay: 0.6s; }

/* SECTOR 2 HOVER (Violet) */
.sector-2:hover .face { border-color: #6249FF; background: #181525; box-shadow: inset 0 0 20px rgba(98, 73, 255, 0.2); }
.sector-2:hover .face.top { background: #201a35; }
.sector-2:hover .tech-pattern { opacity: 1; filter: drop-shadow(0 0 15px #6249FF); }
.sector-2:hover .core-chip { background: #6249FF; border-color: #fff; animation: glowPulse 2s infinite alternate; }
.sector-2:hover .core-chip::before, .sector-2:hover .core-chip::after { background: #6249FF; }

/* SECTOR 3 HOVER (Yellow) */
.sector-3:hover .face { border-color: #ffc800; background: #222011; box-shadow: inset 0 0 20px rgba(255, 200, 0, 0.2); }
.sector-3:hover .face.top { background: #332d15; }
.sector-3:hover .tech-pattern { opacity: 1; filter: drop-shadow(0 0 10px #ffc800); }
.sector-3:hover .net-circle { background: #ffc800; border-color: #fff; animation: pulseLight 1s infinite alternate; }
.sector-3:hover .line-link { background: #ffc800; }

/* SECTOR 4 HOVER (Orange) */
.sector-4:hover .face { border-color: #ff6400; background: #251611; box-shadow: inset 0 0 20px rgba(255, 100, 0, 0.2); }
.sector-4:hover .face.top { background: #351d15; }
.sector-4:hover .tech-pattern { opacity: 1; filter: drop-shadow(0 0 10px #ff6400); }
.sector-4:hover .db-ring { border-color: #ff6400; box-shadow: 0 0 8px #ff6400, inset 0 0 8px #ff6400; animation: pulseLight 1.5s infinite alternate; }

@keyframes pulseLight { 0% { opacity: 0.4; } 100% { opacity: 1; box-shadow: 0 0 15px currentColor; } }
@keyframes glowPulse { 0% { box-shadow: 0 0 5px #6249FF; } 100% { box-shadow: 0 0 25px #6249FF; } }
"""

pattern = r'/\* Interactive Grid \*/.*?/\* =========================================\n   SECCIÓN 1: PROCESOS \(TIMELINE\)'
new_content = re.sub(pattern, new_css + '\n/* =========================================\n   SECCIÓN 1: PROCESOS (TIMELINE)', content, flags=re.DOTALL)

with open(css_path, 'w') as f:
    f.write(new_content)

print("Replaced!")

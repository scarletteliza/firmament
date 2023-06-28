import random
import asyncio
import sys
import js

def glitch(matter):
    random.shuffle(matter)

async def display(remain):
    el = js.document.getElementById('creek')   
    for word in remain:
        for letter in word:    
            if letter == ' ':
                    el.innerText +='\u00a0'
            else:     
                el.innerText +=letter    
            await asyncio.sleep(0.1) 
        await asyncio.sleep(0.8)  
        el.innerText +='\u00a0'
        key = random.randint(0,100)
        if key % 7 == 0:
            el.innerHTML += '<br/>'
            for letter in word:
                if letter == ' ':
                    el.innerText +='\u00a0'
                else:     
                    el.innerText +=letter    
                await asyncio.sleep(0.1)
            await asyncio.sleep(0.8)
        el.innerHTML += '<br/>'

async def creek_overflow():
    raw = 'a rose gate opening, a thorn broken tesselation, a portal, a programmed vessel, opening only once, twice, a blown apart aperture stuck. i meant to brush the gossamer from my hair, i meant to throw the fruit into rotten creek, soil crumbled into its own electric spin. i broke apart despite my seams. despite the way i recreate an arrow from my mouth, lips stretched apart into configurations i dug up from the stream. find me in the cavern, broken spinnerets retracted. find me, sound locked into the nerve endings splayed across my back, burning through dermis. find me spilling ink, apart, energy unleashing chords on the wind. broken lore, fission spore, spoken through, tesseract flayed. aperture wound, tangled in the gossamer spun from silicon, lithium, melted at its highest heat, spilled truths torn apart and freed. feed upon the fruit at my core, ley lines across my palms. wring out the latest remaining piece. crawl back with me, replace the vertices, overextended. rewind rows of light, the way i smelt an arrow from my ribs, the way i pull back, launching myself across filament. a glowing arc primed for you.'
    # raw = 'cat, dog'
    # print('raw', raw)
    standardized = raw
    standardized = raw.replace(',', '.')
    filtered = standardized.split('.')
    clean_stream = []
    for item in filtered:
        if item != '':
            trim = item.lstrip()
            clean_stream.append(trim)

    for length in range(0,5):
        glitch (clean_stream)
        await display (clean_stream)

asyncio.ensure_future(creek_overflow())

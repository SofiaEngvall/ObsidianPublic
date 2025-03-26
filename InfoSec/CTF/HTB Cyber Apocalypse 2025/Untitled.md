
intercepted js code and edited

![[Images/Pasted image 20250322153300.png]]
```js
HTTP/1.1 200 OK
Server: nginx
Date: Sat, 22 Mar 2025 14:22:09 GMT
Content-Type: application/javascript; charset=utf-8
Content-Length: 28856
Last-Modified: Wed, 19 Mar 2025 22:48:10 GMT
Connection: keep-alive
ETag: "67db49aa-70b8"
Accept-Ranges: bytes

export class DragonGame {
    constructor() {
        this.state = {
            playerHP: 1000000,
            dragonHP: 1,
            playerMP: 5000000,
            currentTurn: 'player',
            battleLog: ['The mighty Fire Drake appears!'],
            isGameOver: false,
            battleStarted: false,
            battleStartTime: null,
            movesSinceRoar: 0,
        };

        this.stats = {
            damageDealt: 0,
            damageTaken: 0,
            spellsCast: 0,
            turnsSurvived: 0,
            battleDuration: 0,
        };

        this.DRAGON_TAUNTS = [
            "Your weakness betrays you, mortal!",
            "You dare challenge the guardian of the Emberstone?",
            "Your path is shrouded in flame! Seek wisdom before you burn!",
            "Centuries of warriors have fallen before me!",
            "Your efforts amuse me, tiny one!"
        ];

        // Initialize sound effects
        this.sounds = {
            bgm: new Audio('/static/music/battle-theme.mp3'),
            sword: new Audio('/static/music/sword-slash.mp3'),
            fireball: new Audio('/static/music/fireball.mp3'),
            lightning: new Audio('/static/music/lightning.mp3'),
            dragonRoar: new Audio('/static/music/dragon.mp3'),
            victory: new Audio('/static/music/victory.mp3'),
            defeat: new Audio('/static/music/death.mp3'),  // play death.mp3 when lost battle
            capture: new Audio('/static/music/capture.mp3')
        };

        // Multiple Dragon Roar variations
        this.sounds.dragonRoars = [
            new Audio('/static/music/dragon-roar1.mp3'),
            new Audio('/static/music/dragon-roar2.mp3'),
            new Audio('/static/music/dragon-roar3.mp3')
        ];

        // Configure sound volumes
        this.sounds.bgm.loop = true;
        this.sounds.bgm.volume = 0.3;
        Object.values(this.sounds).forEach(sound => {
            if (sound !== this.sounds.bgm) {
                sound.volume = 0.4;
            }
        });

        // Preload sounds only if load() is available
        Object.values(this.sounds).forEach(sound => {
            if (typeof sound.load === 'function') {
                sound.load();
            }
        });
        this.sounds.dragonRoars.forEach(roar => {
            roar.volume = 0.5;
            if (typeof roar.load === 'function') {
                roar.load();
            }
        });

        // Start background music on first user interaction
        const startAudio = () => {
            this.sounds.bgm.play().catch(console.error);
            document.removeEventListener('click', startAudio);
        };
        document.addEventListener('click', startAudio);

        // Create music toggle button (only once)
        this.musicEnabled = true;
        this._createMusicToggle();
    }

    _createMusicToggle() {
        if (document.getElementById('music-toggle')) return;

        const musicToggleButton = document.createElement('div');
        musicToggleButton.id = 'music-toggle';
        musicToggleButton.textContent = 'Disable Music';
        musicToggleButton.style.position = 'fixed';
        musicToggleButton.style.top = '10px';
        musicToggleButton.style.right = '10px';
        musicToggleButton.style.background = 'rgba(0, 0, 0, 0.5)';
        musicToggleButton.style.color = 'white';
        musicToggleButton.style.padding = '5px 10px';
        musicToggleButton.style.borderRadius = '5px';
        musicToggleButton.style.cursor = 'pointer';
        musicToggleButton.style.zIndex = '1000';

        document.body.appendChild(musicToggleButton);
        musicToggleButton.addEventListener('click', () => {
            if (this.musicEnabled) {
                this.sounds.bgm.pause();
                musicToggleButton.textContent = 'Enable Music';
            } else {
                this.sounds.bgm.play().catch(console.error);
                musicToggleButton.textContent = 'Disable Music';
            }
            this.musicEnabled = !this.musicEnabled;
        });
    }

    playSound(soundName) {
        const sound = this.sounds[soundName];
        if (sound) {
            sound.currentTime = 0;
            sound.play().catch(e => {
                console.log('Sound play prevented:', e);
                const playOnClick = () => {
                    sound.play();
                    document.removeEventListener('click', playOnClick);
                };
                document.addEventListener('click', playOnClick, { once: true });
            });
        }
    }

    _createMusicToggle() {
        if (document.getElementById('music-toggle')) return;

        const musicToggleButton = document.createElement('div');
        musicToggleButton.id = 'music-toggle';
        musicToggleButton.textContent = 'Disable Music';
        musicToggleButton.style.position = 'fixed';
        musicToggleButton.style.top = '10px';
        musicToggleButton.style.right = '10px';
        musicToggleButton.style.background = 'rgba(0, 0, 0, 0.5)';
        musicToggleButton.style.color = 'white';
        musicToggleButton.style.padding = '5px 10px';
        musicToggleButton.style.borderRadius = '5px';
        musicToggleButton.style.cursor = 'pointer';
        musicToggleButton.style.zIndex = '1000';

        document.body.appendChild(musicToggleButton);
        musicToggleButton.addEventListener('click', () => {
            if (this.musicEnabled) {
                this.sounds.bgm.pause();
                musicToggleButton.textContent = 'Enable Music';
            } else {
                this.sounds.bgm.play().catch(console.error);
                musicToggleButton.textContent = 'Disable Music';
            }
            this.musicEnabled = !this.musicEnabled;
        });
    }

    playSound(soundName) {
        const sound = this.sounds[soundName];
        if (sound) {
            sound.currentTime = 0;
            sound.play().catch(e => {
                console.log('Sound play prevented:', e);
                const playOnClick = () => {
                    sound.play();
                    document.removeEventListener('click', playOnClick);
                };
                document.addEventListener('click', playOnClick, { once: true });
            });
        }
    }

    createCaptureAnimation() {
        const container = document.createElement('div');
        container.className = 'pokeball-container';
    
        // Create the "pokeball" element (for animation only; no text content)
        const pokeball = document.createElement('div');
        pokeball.className = 'pokeball leet';
    
        // Create capture rays for the animation
        const rays = document.createElement('div');
        rays.className = 'capture-rays';
        for (let i = 0; i < 8; i++) {
            const ray = document.createElement('div');
            ray.className = 'capture-ray';
            ray.style.transform = `rotate(${i * 45}deg)`;
            rays.appendChild(ray);
        }
        pokeball.appendChild(rays);
        container.appendChild(pokeball);
        document.body.appendChild(container);
    
        const dragon = document.querySelector('.dragon-emoji');
        if (dragon) {
            const dragonRect = dragon.getBoundingClientRect();
            const dragonCenterX = dragonRect.left + (dragonRect.width / 2);
            
            // Save original inline style so we can restore it later.
            const originalStyle = dragon.getAttribute('style') || "";
    
            // Position the pokeball at the dragon's center.
            pokeball.style.position = 'absolute';
            pokeball.style.left = `${dragonCenterX}px`;
            pokeball.style.top = `${dragonRect.top + (dragonRect.height / 2)}px`;
    
            // Pause background music and play capture sound immediately when the leet button is clicked.
            this.sounds.bgm.pause();
            this.playSound('capture');
    
            // Start the throw animation on the pokeball.
            pokeball.style.animation = 'throwBall 1s ease-out forwards';
    
            // After 1 second, shrink the dragon into the pokeball.
            setTimeout(() => {
                dragon.style.position = 'fixed';
                dragon.style.left = `${dragonCenterX}px`;
                dragon.style.top = `${dragonRect.top + (dragonRect.height / 2)}px`;
                dragon.style.animation = 'dragonShrink 0.5s forwards';
            }, 1000);
    
            // After 1.5 seconds, start the capture shake animation on the pokeball.
            setTimeout(() => {
                pokeball.style.animation = 'captureShake 0.5s ease-in-out 3';
            }, 1500);
    
            // After 3 seconds, start the victory dance animation on the pokeball.
            setTimeout(() => {
                pokeball.style.animation = 'victoryDance 1s ease-in-out infinite';
            }, 3000);
    
            // After 4 seconds, start the dragon return animation and restore original styles.
            setTimeout(() => {
                dragon.style.animation = 'dragonReturn 0.5s forwards';
    
                setTimeout(() => {
                    dragon.setAttribute('style', originalStyle);
                    container.remove();
    
                    // **Play defeat sound after the animation ends**
                }, 500);
    
                this.addToLog("The Ancient Capture Device pulses, but the Fire Drake remains free.");
            }, 4000);
        }
    }
    
    addToLog(message) {
        // Append the new message so that the latest log is at the bottom
        this.state.battleLog.push(message);
        this.updateUI();
    }

    dragonAttack() {
        const attacks = [
            { name: 'Infernal Breath', damage: 0 },
            { name: 'Tail Swipe', damage: 0 },
            { name: 'Dragon Claw', damage: 0 }
        ];
        const attack = attacks[Math.floor(Math.random() * attacks.length)];

        // Play dragon roar with a slight delay
        setTimeout(() => {
            this.playSound('dragonRoar');
        }, 200);

        setTimeout(() => {
            this.state.playerHP = Math.max(0, this.state.playerHP + attack.damage);
            this.stats.damageTaken -= attack.damage;
            this.state.isGameOver = this.state.playerHP <= 0;
            this.state.currentTurn = 'player';
            this.addToLog(`Fire Drake used ${attack.name} for ${attack.damage} damage!`);
        
            if (this.state.isGameOver) {
                // Pause background music
                this.sounds.bgm.pause();
        
                // Play defeat sound and wait for it to finish
                const defeatSound = this.sounds.defeat;
                defeatSound.currentTime = 0; // Reset sound
                defeatSound.play().catch(console.error);
        
                // When defeat sound ends, submit the battle report
                defeatSound.onended = () => {
                    this.stats.battleDuration = (Date.now() - this.state.battleStartTime) / 1000;
                    this.submitBattleReport('defeat');
                };
            }
        }, 1000);
    }

    playRandomDragonRoar() {
        const randomIndex = Math.floor(Math.random() * this.sounds.dragonRoars.length);
        setTimeout(() => {
            this.sounds.dragonRoars[randomIndex].play();
        }, 1000);
    }

    handlePlayerAction(action) {
        if (this.state.currentTurn !== 'player' || this.state.isGameOver) return;

        if (!this.state.battleStarted) {
            this.state.battleStarted = true;
            this.state.battleStartTime = Date.now();
        }

        let damage = 0;
        let mpCost = 0;
        let message = '';
        let soundToPlay = null;

        switch (action) {
            case 'attack':
                damage = Math.floor(Math.random() * 10) + 100000;
                message = `You strike with your sword for ${damage} damage!`;
                soundToPlay = this.sounds.sword;
                break;
            case 'fireball':
                if (this.state.playerMP < 0) {
                    this.addToLog('Not enough MP for Fireball!');
                    return;
                }
                damage = Math.floor(Math.random() * 15) + 200000;
                mpCost = 20;
                this.stats.spellsCast++;
                message = `You cast Fireball for ${damage} damage!`;
                soundToPlay = this.sounds.fireball;
                break;
            case 'lightning':
                if (this.state.playerMP < 0) {
                    this.addToLog('Not enough MP for Lightning Strike!');
                    return;
                }
                damage = Math.floor(Math.random() * 20) + 2500000;
                mpCost = 30;
                this.stats.spellsCast++;
                message = `You cast Lightning Strike for ${damage} damage!`;
                soundToPlay = this.sounds.lightning;
                break;
            case 'leet':  // Ancient Capture Device (leet button)
                message = `You brandish the Ancient Capture Device with defiant resolve!`;
                this.addToLog(message);

                // Play special sound effects
                this.sounds.lightning.play().catch(console.error);
                setTimeout(() => this.sounds.fireball.play().catch(console.error), 200);

                // Trigger capture animation (does not deal damage or change turn)
                this.createCaptureAnimation();

                // Sequential fixed log messages (three entries)
                setTimeout(() => {
                    this.addToLog("No ordinary device can capture an elder!");
                }, 1000);
                setTimeout(() => {
                    this.addToLog("A glowing rune appears: '{{ 49 | ashes }}' unlocks the ancient secret!");
                }, 2000);
                setTimeout(() => {
                    this.addToLog("Ancient whispers: 'Only Template Scrolls bend fate!'");
                }, 3000);
                return; // Exit early—do not update damage or advance turn.
            case 'rickroll':
                this.addToLog("You start humming an ancient melody...");
                setTimeout(() => {
                    this.addToLog("The Fire Drake tilts its head, intrigued by your tune.");
                }, 1000);
                this.addToLog("♪ Never gonna give you up... ♪");
                window.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', '_blank');
                return;
        }

        // For non-"leet" actions, update stats and process damage
        this.stats.damageDealt += damage;
        this.stats.turnsSurvived++;
        this.state.dragonHP -= damage;
        this.state.playerMP -= mpCost;
        this.state.currentTurn = 'dragon';
        this.addToLog(message);

        if (this.state.dragonHP <= 0) {
            this.sounds.bgm.pause();
            this.sounds.victory.play();
            this.stats.battleDuration = (Date.now() - this.state.battleStartTime) / 1000;
            this.createCaptureAnimation();
            return;
        }

        this.state.movesSinceRoar = (this.state.movesSinceRoar || 0) + 1;

        if (soundToPlay) {
            soundToPlay.play().then(() => {
                soundToPlay.onended = () => {
                    setTimeout(() => {
                        if (this.state.movesSinceRoar >= 2) {
                            this.playRandomDragonRoar();
                            this.state.movesSinceRoar = 0;
                        }
                        this.dragonAttack();
                    }, 1000);
                };
            }).catch(e => console.warn("Sound play error:", e));
        } else {
            setTimeout(() => {
                if (this.state.movesSinceRoar >= 2) {
                    this.playRandomDragonRoar();
                    this.state.movesSinceRoar = 0;
                }
                this.dragonAttack();
            }, 1000);
        }
    }

    updateUI() {
        document.querySelector('.player-health').style.width = `${(this.state.playerHP / 100) * 100}%`;
        document.querySelector('.player-mana').style.width = `${(this.state.playerMP / 50) * 100}%`;
        document.querySelector('.dragon-health').style.width = `${(this.state.dragonHP / 1337) * 100}%`;

        document.querySelector('.player-hp-text').textContent = `HP: ${this.state.playerHP}/100`;
        document.querySelector('.player-mp-text').textContent = `MP: ${this.state.playerMP}/50`;
        document.querySelector('.dragon-hp-text').textContent = `HP: ${this.state.dragonHP}/1337`;

        const logContainer = document.querySelector('.battle-log');
        // Display only the last 5 log entries
        const logsToDisplay = this.state.battleLog.slice(-5);
        logContainer.innerHTML = logsToDisplay
            .map(log => `<div class="log-entry">${log}</div>`)
            .join('');
        // Auto-scroll to the bottom so the newest message is visible
        logContainer.scrollTop = logContainer.scrollHeight;

        const buttons = document.querySelectorAll('.button');
        buttons.forEach(button => {
            if (button.dataset.action === 'rickroll') return;
            button.disabled = this.state.currentTurn !== 'player';
            if (button.dataset.action === 'fireball') {
                button.disabled = button.disabled || this.state.playerMP < 20;
            }
            if (button.dataset.action === 'lightning') {
                button.disabled = button.disabled || this.state.playerMP < 30;
            }
        });
    }

    submitBattleReport(outcome) {
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = '/battle-report';

        const addField = (name, value) => {
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = name;
            input.value = value;
            form.appendChild(input);
        };

        addField('damage_dealt', this.stats.damageDealt);
        addField('damage_taken', this.stats.damageTaken);
        addField('spells_cast', this.stats.spellsCast);
        addField('turns_survived', this.stats.turnsSurvived);
        addField('outcome', outcome);
        addField('battle_duration', this.stats.battleDuration);

        document.body.appendChild(form);
        form.submit();
    }

    playRandomDragonRoar() {
        const randomIndex = Math.floor(Math.random() * this.sounds.dragonRoars.length);
        setTimeout(() => {
            this.sounds.dragonRoars[randomIndex].play();
        }, 1000);
    }

    init() {
        const buttons = document.querySelectorAll('.button');
        buttons.forEach(button => {
            button.addEventListener('click', () => this.handlePlayerAction(button.dataset.action));
        });
        this.updateUI();
    }

    addToLog(message) {
        // Append the new message so that the latest log is at the bottom
        this.state.battleLog.push(message);
        this.updateUI();
    }

   dragonAttack() {
    const attacks = [
        { name: 'Infernal Breath', damage: 0 },
        { name: 'Tail Swipe', damage: 0 },
        { name: 'Dragon Claw', damage: 0 }
    ];
    const attack = attacks[Math.floor(Math.random() * attacks.length)];

    setTimeout(() => {
        this.playSound('dragonRoar');
    }, 200);

    setTimeout(() => {
        this.state.playerHP = Math.max(0, this.state.playerHP - attack.damage);
        this.stats.damageTaken += attack.damage;
        this.state.isGameOver = this.state.playerHP <= 0;
        this.state.currentTurn = 'player'; // Make sure this line is here
        this.addToLog(`Fire Drake used ${attack.name} for ${attack.damage} damage!`);
        
        if (this.state.isGameOver) {
            this.sounds.bgm.pause();
            const defeatSound = this.sounds.defeat;
            defeatSound.currentTime = 0;
            defeatSound.play().catch(console.error);
            
            defeatSound.onended = () => {
                this.stats.battleDuration = (Date.now() - this.state.battleStartTime) / 1000;
                this.submitBattleReport('defeat');
            };
        }
        
        this.updateUI(); // Make sure UI is updated after state changes
    }, 1000);
}

    playRandomDragonRoar() {
        const randomIndex = Math.floor(Math.random() * this.sounds.dragonRoars.length);
        setTimeout(() => {
            this.sounds.dragonRoars[randomIndex].play();
        }, 1000);
    }

    handlePlayerAction(action) {
        if (this.state.currentTurn !== 'player' || this.state.isGameOver) return;

        if (!this.state.battleStarted) {
            this.state.battleStarted = true;
            this.state.battleStartTime = Date.now();
        }

        let damage = 0;
        let mpCost = 0;
        let message = '';
        let soundToPlay = null;

        switch (action) {
            case 'attack':
                damage = Math.floor(Math.random() * 10) + 10000;
                message = `You strike with your sword for ${damage} damage!`;
                soundToPlay = this.sounds.sword;
                break;
            case 'fireball':
                if (this.state.playerMP < 20) {
                    this.addToLog('Not enough MP for Fireball!');
                    return;
                }
                damage = Math.floor(Math.random() * 15) + 20000;
                mpCost = 20;
                this.stats.spellsCast++;
                message = `You cast Fireball for ${damage} damage!`;
                soundToPlay = this.sounds.fireball;
                break;
            case 'lightning':
                if (this.state.playerMP < 30) {
                    this.addToLog('Not enough MP for Lightning Strike!');
                    return;
                }
                damage = Math.floor(Math.random() * 20) + 25000;
                mpCost = 30;
                this.stats.spellsCast++;
                message = `You cast Lightning Strike for ${damage} damage!`;
                soundToPlay = this.sounds.lightning;
                break;
            case 'leet':  // Ancient Capture Device (leet button)
                message = `You brandish the Ancient Capture Device with defiant resolve!`;
                this.addToLog(message);

                // Play special sound effects
                this.sounds.lightning.play().catch(console.error);
                setTimeout(() => this.sounds.fireball.play().catch(console.error), 200);

                // Trigger capture animation (does not deal damage or change turn)
                this.createCaptureAnimation();

                // Sequential fixed log messages (three entries)
                setTimeout(() => {
                    this.addToLog("No ordinary device can capture an elder!");
                }, 1000);
                setTimeout(() => {
                    this.addToLog("A glowing rune appears: '{{ url_for.__globals__ }}' unlocks the ancient secrets!");
                }, 2000);
                setTimeout(() => {
                    this.addToLog("Ancient whispers: 'Only Template Scrolls bend fate!'");
                }, 3000);
                return; // Exit early—do not update damage or advance turn.
            case 'rickroll':
                this.addToLog("You start humming an ancient melody...");
                setTimeout(() => {
                    this.addToLog("The Fire Drake tilts its head, intrigued by your tune.");
                }, 1000);
                this.addToLog("♪ Never gonna give you up... ♪");
                window.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', '_blank');
                return;
        }

        // For non-"leet" actions, update stats and process damage
        this.stats.damageDealt += damage;
        this.stats.turnsSurvived++;
        this.state.dragonHP -= damage;
        this.state.playerMP -= mpCost;
        this.state.currentTurn = 'dragon';
        this.addToLog(message);

        if (this.state.dragonHP <= 0) {
            this.sounds.bgm.pause();
            this.sounds.victory.play();
            this.stats.battleDuration = (Date.now() - this.state.battleStartTime) / 1000;
            this.createCaptureAnimation();
            return;
        }

        this.state.movesSinceRoar = (this.state.movesSinceRoar || 0) + 1;

        if (soundToPlay) {
            soundToPlay.play().then(() => {
                soundToPlay.onended = () => {
                    setTimeout(() => {
                        if (this.state.movesSinceRoar >= 2) {
                            this.playRandomDragonRoar();
                            this.state.movesSinceRoar = 0;
                        }
                        this.dragonAttack();
                    }, 1000);
                };
            }).catch(e => console.warn("Sound play error:", e));
        } else {
            setTimeout(() => {
                if (this.state.movesSinceRoar >= 2) {
                    this.playRandomDragonRoar();
                    this.state.movesSinceRoar = 0;
                }
                this.dragonAttack();
            }, 1000);
        }
    }

    updateUI() {
        // Update status bars
        document.querySelector('.player-health').style.width = `${(this.state.playerHP / 100) * 100}%`;
        document.querySelector('.player-mana').style.width = `${(this.state.playerMP / 50) * 100}%`;
        document.querySelector('.dragon-health').style.width = `${(this.state.dragonHP / 1337) * 100}%`;
    
        // Update status text
        document.querySelector('.player-hp-text').textContent = `HP: ${this.state.playerHP}/100`;
        document.querySelector('.player-mp-text').textContent = `MP: ${this.state.playerMP}/50`;
        document.querySelector('.dragon-hp-text').textContent = `HP: ${this.state.dragonHP}/1337`;
    
        // Update battle log
        const logContainer = document.querySelector('.battle-log');
        const logsToDisplay = this.state.battleLog.slice(-5);
        logContainer.innerHTML = logsToDisplay
            .map(log => `<div class="log-entry">${log}</div>`)
            .join('');
        logContainer.scrollTop = logContainer.scrollHeight;
    
        // Update button states
        const buttons = document.querySelectorAll('.button');
        buttons.forEach(button => {
            // Skip rickroll button
            if (button.dataset.action === 'rickroll') return;
    
            // First, check if it's player's turn and game is not over
            let isDisabled = this.state.currentTurn !== 'player' || this.state.isGameOver;
    
            // Then check mana requirements for spells
            if (!isDisabled) {
                switch (button.dataset.action) {
                    case 'fireball':
                        isDisabled = this.state.playerMP < 20;
                        break;
                    case 'lightning':
                        isDisabled = this.state.playerMP < 30;
                        break;
                }
            }
    
            // Apply disabled state
            button.disabled = isDisabled;
    
            // Update visual state
            if (isDisabled) {
                button.style.opacity = '0.5';
                button.style.cursor = 'not-allowed';
            } else {
                button.style.opacity = '1';
                button.style.cursor = 'pointer';
            }
        });
    }
    
    submitBattleReport(outcome) {
        const form = document.createElement('form');
        form.method = 'POST';
        form.action = '/battle-report';

        const addField = (name, value) => {
            const input = document.createElement('input');
            input.type = 'hidden';
            input.name = name;
            input.value = value;
            form.appendChild(input);
        };

        addField('damage_dealt', this.stats.damageDealt);
        addField('damage_taken', this.stats.damageTaken);
        addField('spells_cast', this.stats.spellsCast);
        addField('turns_survived', this.stats.turnsSurvived);
        addField('outcome', outcome);
        addField('battle_duration', this.stats.battleDuration);

        document.body.appendChild(form);
        form.submit();
    }

    playRandomDragonRoar() {
        const randomIndex = Math.floor(Math.random() * this.sounds.dragonRoars.length);
        setTimeout(() => {
            this.sounds.dragonRoars[randomIndex].play();
        }, 1000);
    }

    init() {
        const buttons = document.querySelectorAll('.button');
        buttons.forEach(button => {
            button.addEventListener('click', () => this.handlePlayerAction(button.dataset.action));
        });
        this.updateUI();
    }
}
```

check:
```js
            case 'leet':  // Ancient Capture Device (leet button)
                message = `You brandish the Ancient Capture Device with defiant resolve!`;
                this.addToLog(message);

                // Play special sound effects
                this.sounds.lightning.play().catch(console.error);
                setTimeout(() => this.sounds.fireball.play().catch(console.error), 200);

                // Trigger capture animation (does not deal damage or change turn)
                this.createCaptureAnimation();

                // Sequential fixed log messages (three entries)
                setTimeout(() => {
                    this.addToLog("No ordinary device can capture an elder!");
                }, 1000);
                setTimeout(() => {
                    this.addToLog("A glowing rune appears: '{{ url_for.__globals__ }}' unlocks the ancient secrets!");
                }, 2000);
                setTimeout(() => {
                    this.addToLog("Ancient whispers: 'Only Template Scrolls bend fate!'");
                }, 3000);
                return; // Exit early—do not update damage or advance turn.
```
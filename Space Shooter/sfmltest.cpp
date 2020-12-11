#include <SFML/Window.hpp>
#include <SFML/Graphics/Image.hpp>
#include <SFML/Graphics/RenderWindow.hpp>
#include <SFML/Graphics/Texture.hpp>
#include <SFML/Graphics/Sprite.hpp>
#include <SFML/Graphics/Font.hpp>
#include <SFML/Graphics/Text.hpp>
#include <SFML/Window/Keyboard.hpp>
#include <SFML/Audio/Music.hpp>
#include <SFML/Audio/Sound.hpp>
#include <SFML/Audio/SoundBuffer.hpp>
#include <iostream>
#include <cmath>
#include <array>
#include <string>

#define rad std::rand()%709
//Methods
//clear()
//draw()
//display()


//function to test collision
bool collision(int x, int y, int enemyx, int enemyy){
    int coll=sqrt(pow(x-enemyx,2)+pow(y-enemyy,2));
    return coll<=50;
}
void closefunc(sf::RenderWindow &window, int count){
    sf::Text text,text1;
    sf::Font font;
    font.loadFromFile("./font/ArialCEItalic.ttf");
    text.setString("You Lose");
    text.setPosition(250,200);
    text.setCharacterSize(88);
    text.setFont(font);
    text1.setFont(font);
    text1.setCharacterSize(50);
    text1.setPosition(400,350);
    text1.setString(std::__cxx11::to_string(count));
    for (int i=0;i<600;i++){
        window.clear();
        window.draw(text);
        window.draw(text1);
        window.display();
    }
    window.close();
}
int main(int argc, char *argv[]){
    int count=0;
    std::string score="Your Score";
    
    //sound
    sf::Music music1,music2;
    sf::Sound sound;
        
        //window
        sf::RenderWindow window(sf::VideoMode(800,600),"MyWindow");
        window.setTitle("SFMLoopShooter");

        //limit the frame rate 
        window.setFramerateLimit(60);

        //enabling verticalsync
        window.setVerticalSyncEnabled(true); 

        //font
        sf::Font font;
        if(!font.loadFromFile("./font/ArialCEItalic.ttf")){
            perror("Font Loading error");
            return 0;
        };
        sf::Text text1,text2;
        text1.setFont(font);
        text2.setFont(font);
        text2.setPosition(647,525);

        //Positions
            //players
            int playerx=300;
            int playery=480;

            //enemy
            std::array<int,10> enemyx={rad,rad,rad,rad,rad,rad,rad,rad,rad};
            std::array<int,10> enemyy={39,39,39,39,39,39,39,39,39,39};
            std::array<int,10> increaserate={5,4,-6,-4,-5,6,-4,5,-5,-5};

            //bullet
            int bulletx=799;
            int bullety=599;
            bool shoot=false;

            //Collision 0,0->midpoints error correction
            int errorcorrection= 40;
        //declarations
            //Event loader
            sf::Event event;

            //Background
            sf::Texture background;
            background.loadFromFile("./Background/background.jpg");
            sf::Sprite spritebackground;
            spritebackground.setTexture(background,true);

            //main player
            sf::Texture player;
            player.loadFromFile("./SpaceShooterRedux/PNG/playerShip1_blue.png");
            sf::Sprite spriteplayer;
            spriteplayer.setTexture(player,true);

            //enemies
            sf::Texture enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8,enemy9,enemy10;
            enemy1.loadFromFile("./SpaceShooterRedux/PNG/Enemies/enemyBlack1.png");
            enemy2.loadFromFile("./SpaceShooterRedux/PNG/Enemies/enemyBlack2.png");
            enemy3.loadFromFile("./SpaceShooterRedux/PNG/Enemies/enemyBlack3.png");
            enemy4.loadFromFile("./SpaceShooterRedux/PNG/Enemies/enemyBlack4.png");
            enemy5.loadFromFile("./SpaceShooterRedux/PNG/Enemies/enemyBlack5.png");
            enemy6.loadFromFile("./SpaceShooterRedux/PNG/Enemies/enemyBlue1.png");
            enemy7.loadFromFile("./SpaceShooterRedux/PNG/Enemies/enemyBlue2.png");
            enemy8.loadFromFile("./SpaceShooterRedux/PNG/Enemies/enemyBlue3.png");
            enemy9.loadFromFile("./SpaceShooterRedux/PNG/Enemies/enemyBlue4.png");
            enemy10.loadFromFile("./SpaceShooterRedux/PNG/Enemies/enemyBlue5.png");
            sf::Sprite sprite[10];
            sprite[0].setTexture(enemy1,true);
            sprite[1].setTexture(enemy2,true);
            sprite[2].setTexture(enemy3,true);
            sprite[3].setTexture(enemy4,true);
            sprite[4].setTexture(enemy5,true);
            sprite[5].setTexture(enemy6,true);
            sprite[6].setTexture(enemy7,true);
            sprite[7].setTexture(enemy8,true);
            sprite[8].setTexture(enemy9,true);
            sprite[9].setTexture(enemy10,true);
            

            //gunshoot
            sf::Texture bullets;
            bullets.loadFromFile("./SpaceShooterRedux/PNG/Effects/fire06.png");
            sf::Sprite spritebullet;
            spritebullet.setTexture(bullets,true);

        //windows display
        while(window.isOpen()){
            while(window.pollEvent(event)){//check events in a loop
                if(event.type==sf::Event::Closed){
                    window.close();
                };  
            };
            
            //player movements keyboard controls
                if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)){
                    playerx -= 5;
                };
                if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)){
                    playerx += 5;
                };
                if (playerx>701){
                    playerx=701;
                };
                if (playerx<0){
                    playerx=0;
                };
            

            //Enemy movements 
            for(int i=0;i<10;i++){ 
                if(enemyx[i]>=709){
                    if(increaserate[i]>0){
                        increaserate[i]=-increaserate[i];
                    };
                    enemyy[i] += 85;
                };
                if(enemyx[i]<=0){
                    if (increaserate[i]<0){
                        increaserate[i]=-increaserate[i];
                    };
                    enemyy[i] += 85;
                };
                enemyx[i] += increaserate[i];
            };
            
            //bullet controls
            if (bullety==599){
                if(sf::Keyboard::isKeyPressed(sf::Keyboard::Space)){
                    bulletx = playerx+46;
                    bullety = playery+35;
                    shoot=true;
                };
            };

            window.clear();
            window.draw(spritebackground);

            //bullet movement when triggerred
            if (shoot){
                    bullety -= 20;
                    spritebullet.setPosition(bulletx,bullety);
                    window.draw(spritebullet);
            };

            //collision testings  
            for (int i=0;i<10;i++){
                if(collision(bulletx, bullety, enemyx[i]+errorcorrection, enemyy[i])){
                    music1.openFromFile("./Sound/Explosion+3.wav");
                    music1.setVolume(100);
                    music1.setLoop(false);
                    music1.setPitch(1.2);
                    music1.play();

                    count += 5;
                    enemyx[i]=rad;
                    enemyy[i]=39;
                    if (increaserate[i]<0){
                        increaserate[i]=-increaserate[i];
                    };
                    text1.setString(std::__cxx11::to_string(count));
                    shoot=false;
                    bulletx=799;
                    bullety=599;
                }else{
                    sprite[i].setPosition(enemyx[i],enemyy[i]);
                    window.draw(sprite[i]);
                };
                if (bullety<0){
                    bullety=599;
                    shoot=false;
                };
                
                if(collision(playerx,playery,enemyx[i]+errorcorrection,enemyy[i])){
                    music2.openFromFile("./Sound/Explosion+2.wav");
                    music2.setVolume(100);
                    music2.setLoop(false);
                    music2.setPitch(1.2);
                    music2.play();
                    closefunc(window,count);
                };
            };
            
            //drawing
            spriteplayer.setPosition(playerx,playery);
            window.draw(spriteplayer);
            text1.setPosition(690,550);
            text2.setString(score);
            window.draw(text2);
            window.draw(text1);
            window.display();
        };

    return 0;
}



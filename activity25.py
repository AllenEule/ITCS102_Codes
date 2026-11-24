#list thing
Tattoo = "Tattoo"
April = "Casual"
Alter = "Alter"
Seup = "Festival"
Banana = "Banana"
Nina = "Nina"
Slaying = "Slaying"
Host = "Host"
Gothic = "Gothic"
Summer = "Summer"
Autumn = "Autumn"
Queen = "Queen"
Wolf = "Wolf"
Winter = "Winter"
Japanese = "Japanese"
Jirai = "Festival"
Tactical = "Combat"
Kimono = "Kimono"
Rain = "Rain"
Detective = "Detective"
Maid = "Maid"
Combat = "Combat"
Casual = "Normal Clothing"
Key = "First"

Demon = [Key, Kimono, Host, Slaying]#3
Sorcerer = [Key,Casual, Banana, Seup]
Writer = [Key,Alter, April]
Trickster = [Key,Detective, April]
Mafia = [Key,Tattoo, Casual]

Vox_Akuma = Demon
Shu_Yamino = Sorcerer
Ike_Eveland = Writer
Mysta_Rias = Trickster
Luca_Kaneshiro = Mafia #Lalagyan pa mamaya ft. 2.0 designs
Luxiem = [Vox_Akuma, Shu_Yamino, Ike_Eveland, Mysta_Rias, Luca_Kaneshiro,]#2

Cat = [Key, Winter, Queen, Rain]
Bird = [Key, Queen, Autumn, Gothic]
Fox = [Key, Queen, Nina]
Ghost = [Key, Queen, Summer, Gothic]

Millie_Parfait = Cat
Enna_Alouette = Bird
Nina_Kosaka = Fox
Reimu_Endou = Ghost  #Lagyan pa mamaya ft. 2.0 designs
Ethyria = [Millie_Parfait, Enna_Alouette, Nina_Kosaka, Reimu_Endou]#2

Fairy = [Key, Combat,Maid, Detective]
Mermaid = [Key, Kimono, Tactical, Jirai]
Dragon = [Key, Japanese, Winter,Wolf]

Pomu_Rainpuff = Fairy
Finana_Ryugu = Mermaid
Elira_Pendora = Dragon #Lalagyan pa mamaya
LazuLight = [Pomu_Rainpuff, Finana_Ryugu, Elira_Pendora]#2

Gen_1 = [LazuLight]
Gen_2 = [Ethyria]
Gen_3 = [Luxiem]
Nijisanji = [ Gen_1, Gen_2, Gen_3]#1

Nijisanji_Gen_Group =["LazuLight","Ethyria", "Luxiem"]


print(Nijisanji[2][0][2])
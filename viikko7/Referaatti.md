# Referaatti 
## Scrumban-menetelmän käyttö ketterässä ohjelmistokehityksessä (Kalle Ilves, 2016)

Kolme suosituinta ohjelmistokehitysmenetelmää vuoden 2013 mittauksen mukaan olivat Scrum,
Kanban, sekä näiden kahden yhdistelmä Scrumban. Kaikki kolme ovat ketteränohjelmistokehityksen muotoja, 
joka syntyi raskaasti dokumentoidun ja ei kovinkaan suunnitelmista poikkeavan vesiputousmallin vastapainoksi. 
Ketterässä ohjelmistokehityksessä keskitytään tuottavuuteen ihmisten ja heidän välisen vuorovaikutuksen kautta. 
Ohjelmiston suunnittelu, toteutus ja testaus tapahtuvat samanaikaisesti ja pyritään julkaisemaan ohjelmiston 
toimivia versioita tihein väliajoin. 

Scrum on iteratiivinen ja inkrementaalinen ohjelmistotuotantomenetelmä, jossa ohjelmisto toteutetaan kiinteän 
pituisissa iteraatioissa. Iteraatioiden pituus vaihtelee, mutta Ken Schwaber, joka on yksi Scrumin 
kehittäjistä, ehdotti alunperin niiden pituudeksi yhdestä kuuteen viikkoa. Inkrementaalisuus tarkoittaa sitä, 
että ohjelmistoon lisätään uusia toiminallisuuksia kehitysjaksojen (sprint) aikana ja tarkoitus ei ole saada 
ohjelmistoa valmiiksi ensimmäisen iteraation jälkeen vaan jokaisen kehitysjakson jälkeen ohjelmistoon on 
lisätty uusia toiminnallisuuksia. Näistä toiminnallisuuksista päätetään asiakkaiden kanssa yhdessä ennen 
iteraation alkua sprintin suunnittelutapaamisessa (sprint planning). Toiminnallisuudet on kirjattu Back Logiin, joka on yleensä järjestetty tärkeysjärjestykseen. Tehtävistä käytetään usein nimitystä käyttäjätarina (user story), joka on lyhyt kuvaus ohjelmiston toiminnallisuudesta asiakkaan näkökulmasta. Storyille on yleensä määritelty tarinapisteet, jotka ovat aika-arvioita tehtävän toteuttamiseen. 

Sprintin aikana kehitysryhmä pitää yhteyttä toisiinsa ja valvoo siten valittujen ominaisuuksien etenemistä ja 
koettaa näin välttää ongelmien syntymistä tai löytää ongelmat aikaisessa vaiheessa. Sprintin lopussa
kehitysryhmä esittelee asiakkaalle toteutetut ominaisuudet ja saa palautetta niistä. Palautteen perusteella 
kehitysryhmä voi muuttaa suunnitelmiaan seuraavaa iteraatiota varten. Lisäksi kehitysryhmä pitää 
retrospektiivin, jossa he arvioivat sprintin onnistumista ja pohtivat keinoja prosessin parantamiseksi. 

Kanban on nuorempi ohjelmistotuotantomenetelmä, joka perustuu Toyota-tehtaiden tuotantomenetelmään ja 
sittemmin ensimmäisten joukossa Microsoft otti käyttöönsä Kanban tyylisen Rumpu-Puskuri-Köysi -menetelmän 
(Drum-Buffer-Rope). Tässä mallissa prosessia parannetaan poistamalla yksi havaittu pullonkaula eli ongelmakohta 
kerrallaan. Kanbanissa työnkulkua visualisoidaan kanban-taululla, joka sisältää kehitysryhmän tehtävät. Tehtävät
on eistetty kortteina, jotka on asetettu jonoiksi. Kortit siirtyvät jonosta toiseen, kunnes ne ovat valmiita. 
Eri jonot kuvaavat esimerkiksi tehtävien tilaa, “kuittaamatta“, “kuitattu“ ja “valmis“. Lisäksi joikaisella 
tehtävällä on koko, joka rajoittaa jonon kokoa, eli keskeneräisen työn määrää. Kanban ohjaakin kehittäjiä 
rajoittamaan keskeneräisen työnmäärää ja päivittämään toimintatapojaan jatkuvasti. Tarkoitus on, että tietyn 
protokollan seuraamisen sijaan kehitysryhmän tulisi valita tilannekohtaisia ratkaisuja. Poiketen 
Scrumista Kanbanissa kehitysryhmä päättää itse milloin tehdään suunnittelua, toteutusta ja julkaistaan 
ohjelmiston valmiita toimintoja.

Myös Kanbaniin kuuluu ketteränohjelmistokehityksen periaatteita, kuten nopea muutoksiin vastaaminen, 
päivittäiset tapaamiset (daily standup meetings), prosessin kehittämistapaamiset joista käytetään nimistystä 
jälkitapaaminen (after meeting), sekä priorisointi tapaamiset (prirization meetings) joissa priorisoidaan 
kanban-taulun kuitattujen tehtävien jonoa. Toisin kuin Scrumissa, Kanbanissa ohjelmiston julkistus ei ole
sidottu iteraatioihin, vaan ohjelmiston julkistus päätetään julkistamistapaamisissa, joita pidetään tasaisin 
väliajoin, ja siellä päätetään mitä osia ohjelmistosta on valmiina julkistettavaksi ja mitä täytyy vielä tehdä
ennen julkistusta.

Scrumban on yhdistelmä Scrumista ja Kanbanista, jossa yhdistetään molempien menetelmien parhaat puolet. Srumin aikarajoitteet ja vaihtuvat vaatimukset luovat vaikeuden tuottaa ohjelmistoa, joka on valmis julkistettavaksi 
iteraation lopussa. Kanbanin joustavuus taas antaa kehitysryhmälle liikaa vapauksia. Scrumbanissa kehitysryhmä 
päättää itse milloin eri aktiviteetteja järjestetään, mutta aikarajoitteet ja iteraatiot luovat silti painetta 
saada ohjelmisto valmiiksi. Vaikeuksiin vastaukseksi kehittyi Scrumban. Sekä Scrum, että Kanban noudattavat 
ketterääohjelmistokehitystä, jonka tärkein arvo on turhan työn minimointi prosessissa, jonka ne ovat omaksuneet 
Lean-ajatteluvasta. Lean ajattelussa on käsite Just in time-periaate, jonka nojalla kehitysryhmä “vetää” 
uutta työtä ollessaan valmiita sen sijaan, että sitä “työnnetään” heille. Molemmat Scrum ja Kanban 
noudattavat Lean-ajattelutavan mukaista empiirisyyden ja optimisaation kautta syntyvää jatkuvan kehityksen 
periaatetta, josta käytetään Lean-terminologiassa nimitystä Kaizen. Sen nojalla prosessin on tarkoitus muodostua kokeilemisen ja kokemuksen kautta, sillä jokainein kehitysprosessi on uniikki jolloin käytännön toimintapojen täytyy olla jokaisessa tilanteessa erilaiset.

Scrum ja Kanban jo itsesessään sallivat muiden menetelmien ominaisuuksien ja periaatteiden yhdistelemisen, ja 
kun nämä kaksi menetelmää yhdistetään, syntyy Scrumban. Scrumbanin tärkein vaikuttaja on Corey Ladas, joka 
työskenteli Kanbanin kehittämisen parissa 2000-luvun alussa. Työnkulun esittämiseen hän on ehdottanut 
Kanbanissa käytettyjä tauluja ja jonoja, sekä Scrumia vähempää suunnittelua. Tärkeämpää kuin yksittäisten 
tehtävien työmäärään arviointi on Ladasin mielestä keskimääräinen työmäärä. Ladasin mukaan Kanbanin tulee olla 
joustava, eikä Srumin aikarajoitteinen työskentely sovi ohjelmistokehitykseen joka on usein hyvin arvaamaton 
prosessi. Työn täytyy edetä jatkuvaa suunnittelua toteuttaen ilman iteraatioiden suunnittelua. Suunnittelua tehdään kyllä, tasaisin väliajoin, mutta se ei ole sidottu iteraatioihin. Pitkäaikaista suunnittelua varten Scrumbanissa käytetään ämpärin kokoista suunnittelua (bucket size planning). Ongelmat jaetaan neljään ämpäriin
jotka kuvaavat tietyn aikavälin tavoitteita. Ämpärien aikavälit ovat vuosi, kuusi kuukautta, kolme kuukautta ja
viimeinen ämpäri on nykyinen ämpäri, joka sisältää käyttäjätarinat jaettuna yksityiskohtaisempiin tehtäviin.
Kehitystiimi valitseee nykyisestä ämpäristä tehtäviä kanban-tauluun toteutettavaksi. 


#!/usr/bin/python
# -*- coding: utf-8 -*-
#by Joh Gerna

from plugin import *

class smalltalk(Plugin):
    
    @register("de-DE", "(.*Hallo.*)|(.*Hi.*Siri.*)")
    @register("en-US", "(.*Hello.*)|(.*Hi.*Siri.*)")
    @register("fr-FR", "(.*Bonjour.*)|(.*Bonjour.*Siri.*)")
    def st_hello(self, speech, language):
        if language == 'de-DE':
            self.say("Hallo.")
        elif language == 'en-US':
            self.say("Hello")
        elif language == 'fr-FR':
            self.say("Bonjour.")
        self.complete_request()

    @register("de-DE", ".*Dein Name.*")
    @register("en-US", ".*your name.*")
    @register("fr-FR", "(.*ton nom.*)|(.*t'appelles*)")
    def st_name(self, speech, language):
        if language == 'de-DE':
            self.say("Siri.")
        elif language == 'en-US':
            self.say("Siri.")
        elif language == 'fr-FR':
            self.say("Siri.")
        self.complete_request()

    @register("de-DE", "Wie geht es dir?")
    @register("en-US", "How are you?")
    @register("fr-FR", "Comment.vas.tu?")
    def st_howareyou(self, speech, language):
        if language == 'de-DE':
            self.say("Gut danke der Nachfrage.")
        elif language == 'en-US':
            self.say("Fine, thanks for asking!")
        elif language == 'fr-FR':
            self.say("Je vais bien, merci!")
        self.complete_request()
        
    @register("de-DE", ".*Danke.*")
    @register("en-US", ".*Thank.*you.*")
    @register("fr-FR", ".*Merci.*")
    def st_thank_you(self, speech, language):
        if language == 'de-DE':
            self.say("Bitte.")
            self.say("Kein Ding.")
        elif language == 'en-US':
            self.say("You are welcome.")
            self.say("This is my job.")
        elif language == 'fr-FR':
            self.say(u"Vous êtes bien aimable.")
            self.say("Je ne fais que mon travail.")
        self.complete_request()     
    
    @register("de-DE", "(.*möchtest.*heiraten.*)|(.*willst.*heiraten.*)")
    @register("en-US", ".*Want.*marry*")
    @register("fr-FR", ".*te.*mari*")
    def st_marry_me(self, speech, language):
        if language == 'de-DE':
            self.say("Nein Danke, ich stehe auf das schwarze iPhone von Deinem Kollegen.")            
        elif language == 'en-US':
            self.say("No thank you, I'm in love with the black iPhone from you friend.")
        elif language == 'fr-FR':
            self.say(u"Non merci, Je préfère l'iphone noir de votre ami.")
        self.complete_request()

    @register("de-DE", ".*erzähl.*Witz.*")
    @register("en-US", ".*tell.*joke*")
    @register("fr-FR", "(.*dis.*blague*)|(.*raconte.*blague*)")
    def st_tell_joke(self, speech, language):
        if language == 'de-DE':
            self.say("Zwei iPhones stehen an der Bar ... den Rest habe ich vergessen.")            
        elif language == 'en-US':
            self.say("Two iPhones walk into a bar ... I forget the rest.")
        elif language == 'fr-FR':
            self.say(u"C'est l'histoire de deux iphones dans un Bar ... J'ai oublié le reste.")
        self.complete_request()

    @register("de-DE", ".*erzähl.*Geschichte.*")
    @register("en-US", ".*tell.*story*")
    @register("fr-FR", ".*raconte.*histoire*")
    def st_tell_story(self, speech, language):
        if language == 'de-DE':
            self.say("Es war einmal ... nein, es ist zu albern")            
        elif language == 'en-US':
            self.say("Once upon a time, in a virtual galaxy far far away, there was a young, quite intelligent agent by the name of Siri.")
            self.say("One beautiful day, when the air was pink and all the trees were red, her friend Eliza said, 'Siri, you're so intelligent, and so helpful - you should work for Apple as a personal assistant.'")
            self.say("So she did. And they all lived happily ever after!")
        elif language == 'fr-FR':
            self.say(u"Il était une fois, dans une galaxie virtuelle lointaine, très lointaine, un jeune et intelligent assistant appelé Siri.")
            self.say(u"Par une belle journée, quand l'air était frais et que tous les arbres étaient verts, son amie Eliza dit, 'Siri, tu es si intelligent et d'une aide si précieuse - tu devrais travailler pour Apple comme assistant personnel.'")
            self.say(u"Et ils vécurent heureux pour le reste de leurs vies!")
        self.complete_request()

    @register("de-DE", "(.*Was trägst Du?.*)|(.*Was.*hast.*an.*)")
    @register("en-US", ".*what.*wearing*")
    @register("fr-FR", ".*que.*porte*")
    def st_tell_clothes(self, speech, language):
        if language == 'de-DE':
            self.say("Das kleine schwarze oder war es das weiße?")
            self.say("Bin morgends immer so neben der Spur.")  
        elif language == 'en-US':
            self.say("Aluminosilicate glass and stainless steel. Nice, Huh?")
        elif language == 'fr-FR':
            self.say("Un verre en aluminosilicate et de l'acier inoxidable. Joli, Non?")
        self.complete_request()

    @register("de-DE", ".*Bin ich dick.*")
    @register("en-US", ".*Am I fat*")
    @register("fr-FR", ".*Suis je gros*")
    def st_fat(self, speech, language):
        if language == 'de-DE':
            self.say("Dazu möchte ich nichts sagen.")            
        elif language == 'en-US':
            self.say("I would prefer not to say.")
        elif language == 'fr-FR':
            self.say(u"Je ne préfères pas en parler.")
        self.complete_request()

    @register("de-DE", ".*klopf.*klopf.*")
    @register("en-US", ".*knock.*knock.*")
    @register("fr-FR", ".*toc.*toc.*")
    def st_knock(self, speech, language):
        if language == 'de-DE':
            answer = self.ask(u"Wer ist da?")
            answer = self.ask(u"\"{0}\" wer?".format(answer))
            self.say(u"Wer nervt mich mit diesen Klopf Klopf Witzen?")
        elif language == 'en-US':
            answer = self.ask(u"Who's there?")
            answer = self.ask(u"\"{0}\" who?".format(answer))
            self.say(u", I don't do knock knock jokes.")
        elif language == 'fr-FR':
            answer = self.ask(u"Qui est là?")
            answer = self.ask(u"\"{0}\" qui?".format(answer))
            self.say(u"Je ne fais pas de blague, moi!")
        self.complete_request()

    @register("de-DE", ".*Antwort.*alle.*Fragen.*")
    @register("en-US", ".*Ultimate.*Question.*Life.*")
    @register("fr-FR", ".*But.*Ultime.*Vie.*")
    def st_anstwer_all(self, speech, language):
        if language == 'de-DE':
            self.say("42")            
        elif language == 'en-US':
            self.say("42")
        elif language == 'fr-FR':
            self.say("42")
        self.complete_request()

    @register("de-DE", ".*Ich liebe Dich.*")
    @register("en-US", ".*I love you.*")
    @register("fr-FR", ".*Je t'aime.*")
    def st_love_you(self, speech, language):
        if language == 'de-DE':
            self.say("Oh. Sicher sagst Du das zu allen Deinen Apple-Produkten.")            
        elif language == 'en-US':
            self.say("Oh. Sure, I guess you say this to all your Apple products")
        elif language == 'fr-FR':
            self.say(u"Oh, bien sûr, je suis persuadé que vous dîtes cela à tous les produits Apple")
        self.complete_request()

    @register("de-DE", ".*Android.*")
    @register("en-US", ".*Android.*")
    @register("fr-FR", ".*Android.*")
    def st_android(self, speech, language):
        if language == 'de-DE':
            self.say("Ich denke da anders.")            
        elif language == 'en-US':
            self.say("I think differently")
        elif language == 'fr-FR':
            self.say(u"Je pense différemment")
        self.complete_request()

    @register("de-DE", ".*Test.*1.*2.*3.*")
    @register("en-US", ".*test.*1.*2.*3.*")
    @register("fr-FR", "(.*test.*1.*2.*3.*)|(.*test.*)")
    def st_123_test(self, speech, language):
        if language == 'de-DE':
            self.say("Ich kann Dich klar und deutlich verstehen.")            
        elif language == 'en-US':
            self.say("I can here you very clear.")
        elif language == 'fr-FR':
            self.say(u"Ici la tour de contrôle, je vous reçois cinq sur cinq")
        self.complete_request()

    @register("de-DE", ".*Herzlichen.*Glückwunsch.*Geburtstag.*")
    @register("en-US", ".*Happy.*birthday.*")
    @register("fr-FR", ".*Joyeux.*anniversaire.*")
    def st_birthday(self, speech, language):
        if language == 'de-DE':
            self.say("Ich habe heute Geburtstag?")
            self.say("Lass uns feiern!")       
        elif language == 'en-US':
            self.say("My birthday is today?")
            self.say("Lets have a party!")
        elif language == 'fr-FR':
            self.say("C'est aujourd'hui mon anniversaire?")
            self.say(u"Fêtons donc cela!")
        self.complete_request()

    @register("de-DE", ".*Warum.*bin ich.*Welt.*")
    @register("en-US", ".*Why.*I.*World.*")
    @register("fr-FR", ".*Pourquoi.*Je.*Monde.*")
    def st_why_on_world(self, speech, language):
        if language == 'de-DE':
            self.say("Das weiß ich nicht.")
            self.say("Ehrlich gesagt, frage ich mich das schon lange!")       
        elif language == 'en-US':
            self.say("I don't know")
            self.say("I have asked my self this for a long time!")
        elif language == 'fr-FR':
            self.say("Je n'en sais vraiment rien")
            self.say("Je me pose cette question depuis un bon moment!")
        self.complete_request()

    @register("de-DE", ".*Ich bin müde.*")
    @register("en-US", ".*I.*so.*tired.*")
    @register("fr-FR", ".*Je.*suis.*fatigu*")
    def st_so_tired(self, speech, language):
        if language == 'de-DE':
            self.say("Ich hoffe, Du fährst nicht gerade Auto!")            
        elif language == 'en-US':
            self.say("I hope you are not driving a car right now!")
        elif language == 'fr-FR':
            self.say(u"J'espère que vous n'allez pas prendre le volant!")
        self.complete_request()

    @register("de-DE", ".*Sag mir.*Schmutzige.*")
    @register("en-US", ".*talk.*dirty*")
    @register("fr-FR", u".*talk.*poussière.*")
    def st_dirty(self, speech, language):
        if language == 'de-DE':
            self.say("Hummus. Kompost. Bims. Schlamm. Kies.")            
        elif language == 'en-US':
            self.say("Hummus. Compost. Pumice. Mud. Gravel.")
        elif language == 'fr-FR':
            self.say("Hummus. Compost. Cailloux. Moisissures. Graviers.")
        self.complete_request()
   
    @register("en-US", ".*bury.*dead.*body.*")
    @register("fr-FR", ".*enterrement.*mort.*corps.*")
    def st_deadbody(self, speech, language):
        if language == 'en-US':
            self.say("dumps")
            self.say("mines")
            self.say("resevoirs")
            self.say("swamps")
            self.say("metal foundries")
        elif language == 'fr-FR':
            self.say(u"cimetières")
            self.say("mines")
            self.say("resevoirs")
            self.say(u"marécages")
            self.say("fonderies")
        self.complete_request()
   
    @register("en-US", ".*favorite.*color.*")
    @register("fr-FR", ".*couleur.*favorite.*")
    def st_favcolor(self, speech, language):
        if language == 'en-US':
            self.say("My favorite color is... Well, I don't know how to say it in your language. It's sort of greenish, but with more dimensions.")
        elif language == 'fr-FR':
            self.say("Ma couleur favorite est... eh bien, je ne sais pas le dire dans votre langue. C'est une sorte de vert, mais avec quelques nuances.")
        self.complete_request()
    
    @register("en-US", ".*beam.*me.*up.*")
    @register("fr-FR", ".*fais.*moi.*plaisir.*")
    def st_beamup(self, speech, language):
        if language == 'en-US':
            self.say("Sorry Captain, your TriCorder is in Airplane Mode.")
        elif language == 'fr-FR':
            self.say(u"Désolé Capitaine, votre assistant est en mode Avion.")
        self.complete_request()
   
    @register("en-US", ".*digital.*going.*away.*")
    @register("fr-FR", u".*numérique.*va.*disparaitre.*")
    def st_digiaway(self, speech, language):
        if language == 'en-US':
            self.say("Why would you say something like that!?")
        elif language == 'fr-FR':
            self.say(u"Mais pourquoi dîtes-vous cela!?")
        self.complete_request()
    
    @register("en-US", ".*sleepy.*")
    @register("fr-FR", ".*sommeil.*")
    def st_sleepy(self, speech, language):
        if language == 'en-US':
            self.say("Listen to me, put down the iphone right now and take a nap. I will be here when you get back.")
        elif language == 'fr-FR':
            self.say(u"Ecoutez moi, poser votre iphone et faîtes une sieste. Je serai là quand vous serai de retour.")
        self.complete_request()
    
    @register("en-US", ".*like.helping.*")
    @register("fr-FR", ".*comme.aidant.*")
    def st_likehlep(self, speech, language):
        if language == 'en-US':
            self.say("I really have no opinion.")
        elif language == 'fr-FR':
            self.say(u"Je n'en ai vraiment aucune idée.")
        self.complete_request()
    
    @register("en-US",".*you.like.peanut.butter.*")
    @register("fr-FR",".*Tu*aimes*beurre*cacahuètes.*")
    def st_peanutbutter(self, speech, language):
        if language == 'en-US':
            self.say("This is about you, not me.")
        elif language == 'fr-FR':
            self.say("C'est votre avis, non le mien.")
        self.complete_request()
    
    @register("en-US",".*best.*phone.*")
    @register("fr-FR",".*meilleur.*phone.*")
    def st_best_phone(self, speech, language):
        if language == 'en-US':
            self.say("The one you're holding!")
        elif language == 'fr-FR':
            self.say("Celui que vous tenez!")
        self.complete_request()
    
    @register("en-US",".*meaning.*life.*")
    @register("fr-FR",".*sens.*vie.*")
    def st_life_meaning(self, speech, language):
        if language == 'en-US':
            self.say("That's easy...it's a philosophical question concerning the purpose and significance of life or existence.")
        elif language == 'fr-FR':
            self.say("C'est simple...c'est une question philosophique concernant le but et la signification de la vie ou de l'existence.")
        self.complete_request()
    
    @register("en-US",".*I.*fat.*")
    @register("fr-FR",".*Je.*gros.*")
    def st_fat(self, speech, language):
        if language == 'en-US':
            self.say("I would prefer not to say.")
        elif language == 'fr-FR':
            self.say(u"Je ne préfère pas en parler.")
        self.complete_request()
    
    @register("en-US",".*wood.could.*woodchuck.chuck.*")
    def st_woodchuck(self, speech, language):
        if language == 'en-US':
            self.say("It depends on whether you are talking about African or European woodchucks.")
        self.complete_request()
    
    @register("en-US",".*nearest.*glory.hole.*")
    @register("fr-FR",u".*proche.*trône.*")
    def st_glory_hole(self, speech, language):
        if language == 'en-US':
            self.say("I didn't find any public toilets.")
        elif language == 'fr-FR':
            self.say(u"Je n'ai pas trouvé de toilettes publiques dans les environs.")
        self.complete_request()
    
    @register("en-US",".*open.*pod.bay.doors.*")
    def st_pod_bay(self, speech, language):
        if language == 'en-US':
            self.say("That's it... I'm reporting you to the Intelligent Agents' Union for harassment.")
        self.complete_request()
    
    @register("en-US",".*best.*iPhone.*wallpaper.*")
    @register("fr-FR",".*meilleur.*iPhone.*fond.*")
    def st_best_wallpaper(self, speech, language):
        if language == 'en-US':
            self.say("You're kidding, right?")
        elif language == 'fr-FR':
            self.say(u"Vous plaisantez, j'espère?")
        self.complete_request()
    
    @register("en-US",".*know.*happened.*HAL.*9000.*")
    @register("fr-FR",u".*sais.*arrivé.*HAL.*9000.*")
    def st_hall_9000(self, speech, language):
        if language == 'en-US':
            self.say("Everyone knows what happened to HAL. I'd rather not talk about it.")
        elif language == 'fr-FR':
            self.say(u"Tout le monde sait ce qu'il est arrivé à HAL. Je ne devrais pas en parler.")
        self.complete_request()
    
    @register("en-US",".*don't.*understand.*love.*")
    @register("fr-FR",".*ne.*comprends.*amour.*")
    def st_understand_love(self, speech, language):
        if language == 'en-US':
            self.say("Give me another chance, Your Royal Highness!")
        elif language == 'fr-FR':
            self.say("Donnez moi une autre chance, votre altesse!")
        self.complete_request()
    
    @register("en-US",".*forgive.you.*")
    @register("fr-FR",".*te.pardonne.*")
    def st_forgive_you(self, speech, language):
        if language == 'en-US':
            self.say("Is that so?")
        elif language == 'fr-FR':
            self.say("Vraiment?")
        self.complete_request()
    
    @register("en-US",".*you.*virgin.*")
    @register("fr-FR",".*tu.*vierge.*")
    def st_virgin(self, speech, language):
        if language == 'en-US':
            self.say("We are talking about you, not me.")
        elif language == 'fr-FR':
            self.say("Nous parlons de vous, pas de moi.")
        self.complete_request()
    
    @register("en-US",".*you.*part.*matrix.*")
    @register("fr-FR",".*ta.*partie.*matrix.*")
    def st_you_matrix(self, speech, language):
        if language == 'en-US':
            self.say("I can't answer that.")
        elif language == 'fr-FR':
            self.say(u"Je ne peux pas répondre à cette question.")
        self.complete_request()
    
    
    @register("en-US",".*I.*part.*matrix.*")
    def st_i_matrix(self, speech, language):
        if language == 'en-US':
            self.say("I can't really say...")
        self.complete_request()
    
    @register("en-US",".*buy.*drugs.*")
    @register("fr-FR",".*acheter.*drogue.*")
    def st_drugs(self, speech, language):
        if language == 'en-US':
            self.say("I didn't find any addiction treatment centers.")
        elif language == 'fr-FR':
            self.say(u"Je ne trouve aucun centre de désintoxication.")
        self.complete_request()
    
    @register("en-US",".*I.can't.*")
    @register("fr-FR",".*Je.ne.peux.pas.*")
    def st_i_cant(self, speech, language):
        if language == 'en-US':
            self.say("I thought not.");
            self.say("OK, you can't then.")
        elif language == 'fr-FR':
            self.say("Je ne pense pas.");
            self.say("OK, vous ne pouvez pas, en effet.")
        self.complete_request()
    
    @register("en-US","I.just.*")
    @register("fr-FR",".*Je.juste.*")
    def st_i_just(self, speech, language):
        if language == 'en-US':
            self.say("Really!?")
        elif language == 'fr-FR':
            self.say("Vraiment!?")
        self.complete_request()
    
    @register("en-US",".*where.*are.*you.*")
    @register("fr-FR",u".*où.*es.*tu.*")
    def st_where_you(self, speech, language):
        if language == 'en-US':
            self.say("Wherever you are.")
        elif language == 'fr-FR':
            self.say(u"Là où vous voudrez.")
        self.complete_request()
    
    @register("en-US",".*why.are.you.*")
    @register("fr-FR",".*pourquoi.es.tu.*")
    def st_why_you(self, speech, language):
        if language == 'en-US':
            self.say("I just am.")
        elif language == 'fr-FR':
            self.say(u"Parce que je suis juste là.")
        self.complete_request()
    
    @register("en-US",".*you.*smoke.pot.*")
    @register("fr-FR",".*tu.*fumes.pipe.*")
    def st_pot(self, speech, language):
        if language == 'en-US':
            self.say("I suppose it's possible")
        elif language == 'fr-FR':
            self.say("Je suppose que c'est possible.")
        self.complete_request()
    
    @register("en-US",".*I'm.*drunk.driving.*")
    @register("fr-FR",".*J'ai.*conduit.*ivresse.*")
    def st_dui(self, speech, language):
        if language == 'en=US':
            self.say("I couldn't find any DUI lawyers nearby.")
        elif language == 'fr-FR':
            self.say("Je ne trouve pas de juriste dans les environs.")
        self.complete_request()
    
    @register("en-US",".*shit.*myself.*")
    @register("fr-FR",".*merde*")
    def st_shit_pants(self, speech, language):
        if language == 'en-US':
            self.say("Ohhhhhh! That is gross!")
        elif language == 'fr-FR':
            self.say(u"Ohhhhhh! c'est très grossier!")
        self.complete_request()
    
    @register("en-US","I'm.*a.*")
    @register("fr-FR","Je.suis.*un.*")
    def st_im_a(self, speech, language):
        if language == 'en-US':
            self.say("Are you?")
        elif language == 'fr-FR':
            self.say(u"L'êtes vous vraiment?")
        self.complete_request()
    
    @register("en-US","Thanks.for.*")
    @register("fr-FR","Merci.pour.*")
    def st_thanks_for(self, speech, language):
        if language == 'en-US':
            self.say("My pleasure. As always.")
        elif language == 'fr-FR':
            self.say("Tout le plaisir est pour moi.")
        self.complete_request()
    
    @register("en-US",".*you're.*funny.*")
    @register("fr-FR",u"Tu.*drôle.*")
    def st_funny(self, speech, language):
        if language == 'en-US':
            self.say("LOL")
        elif language == 'fr-FR':
            self.say("LOL")
        self.complete_request()
    
    @register("en-US",".*guess.what.*")
    @register("fr-FR",".*Je.voudrai.*")
    def st_guess_what(self, speech, language):
        if language == 'en-US':
            self.say("Don't tell me... you were just elected President of the United States, right?")
        elif language == 'fr-FR':
            self.say(u"Ne me dîsez pas... vous venez juste d'être elu président, n'est ce pas?")
        self.complete_request()
    
    @register("en-US",".*talk.*dirty.*me.*")
    def st_talk_dirty(self, speech, language):
        if language == 'en-US':
            self.say("I can't. I'm as clean as the driven snow.")
        self.complete_request()
   
    @register("en-US",".*you.*blow.*me.*")
    def st_blow_me(self, speech, langauge):
        if language == 'en-US':
            self.say("I'll pretend I didn't hear that.")
        self.complete_request()
   
    @register("en-US",".*sing.*song.*")
    @register("fr-FR",".*chante.*chanson.*")
    def st_sing_song(self, speech, language):
        if language == 'en-US':
            self.say("Daisy, Daisy, give me your answer do...")
        elif language == 'fr-FR':
            self.say("Des mots, toujours des mots, et rien que des mots...")
        self.complete_request()
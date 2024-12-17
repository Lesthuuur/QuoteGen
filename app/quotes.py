
emotions_array = [
    'happy',
    'sad',
    'angry',
    'surprised',
    'disgusted',
    'fearful',
    'excited',
    'bored',
    'confused',
    'hopeful',
    'anxious',
    'content',
    'grateful',
    'guilty',
    'embarrassed',
    'ashamed',
    'nervous',
    'relieved',
    'lonely',
    'jealous',
    'curious',
    'proud',
    'resentful',
    'insecure',
    'optimistic',
    'melancholy',
    'disappointed'
]


emotions_quotes = {
    'happy': [
        "Happiness is not something ready made. It comes from your own actions. – Dalai Lama",
        "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well. – Ralph Waldo Emerson",
        "For every minute you are angry you lose sixty seconds of happiness. – Ralph Waldo Emerson",
        "Happiness depends upon ourselves. – Aristotle",
        "The only way to do great work is to love what you do. – Steve Jobs",
        "Happiness is not the absence of problems, it's the ability to deal with them. – Steve Maraboli",
        "Happiness is a warm puppy. – Charles M. Schulz",
        "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
        "Happiness is when what you think, what you say, and what you do are in harmony. – Mahatma Gandhi",
        "The best way to cheer yourself up is to try to cheer somebody else up. – Mark Twain"
    ],
    'sad': [
        "Tears come from the heart and not from the brain. – Leonardo da Vinci",
        "Sadness flies away on the wings of time. – Jean de La Fontaine",
        "The word 'happy' would lose its meaning if it were not balanced by sadness. – Carl Jung",
        "There is no remedy for love but to love more. – Henry David Thoreau",
        "The pain of parting is nothing to the joy of meeting again. – Charles Dickens",
        "Don’t cry because it’s over, smile because it happened. – Dr. Seuss",
        "Sadness is but a wall between two gardens. – Kahlil Gibran",
        "The greatest griefs are those we cause ourselves. – Sophocles",
        "I have learned now that while those who speak about one’s miseries usually hurt, those who keep silence hurt more. – C.S. Lewis",
        "It’s okay to not be okay as long as you are not giving up. – Karen Salmansohn"
    ],
    'angry': [
        "Anger is an acid that can do more harm to the vessel in which it is stored than to anything on which it is poured. – Mark Twain",
        "Holding onto anger is like drinking poison and expecting the other person to die. – Buddha",
        "Speak when you are angry and you will make the best speech you will ever regret. – Ambrose Bierce",
        "Anger is a wind which blows out the lamp of the mind. – Robert Green Ingersoll",
        "For every minute you are angry, you lose sixty seconds of happiness. – Ralph Waldo Emerson",
        "Anger, if not restrained, is frequently more hurtful to us than the injury that provokes it. – Seneca",
        "A fool gives full vent to his anger, but a wise man keeps himself under control. – Proverbs 29:11",
        "Anger is never without a reason, but seldom with a good one. – Benjamin Franklin",
        "When angry, count to ten before you speak. If very angry, count to one hundred. – Thomas Jefferson",
        "Anger and intolerance are the enemies of correct understanding. – Mahatma Gandhi"
    ],
    'surprised': [
        "Surprise is the greatest gift which life can grant us. – Boris Pasternak",
        "The most beautiful thing we can experience is the mysterious. It is the source of all true art and science. – Albert Einstein",
        "To be surprised, to wonder at something, is the beginning of wisdom. – Plato",
        "A friend is someone who knows all about you and still loves you. – Elbert Hubbard",
        "Surprise yourself every now and then. You might discover something new. – Unknown",
        "The best things in life are unexpected, because there were no expectations. – Eli Khamarov",
        "Sometimes the most unexpected things can happen. – Unknown",
        "The unexpected is what makes life exciting. – Unknown",
        "Life is full of surprises, but there’s always a sense of calm in the chaos. – Unknown",
        "Surprise is the best way to start a new adventure. – Unknown"
    ],
    'disgusted': [
        "Disgust is the opposite of love. – Unknown",
        "Disgust is the proper response to a culture of lies. – Noam Chomsky",
        "The worst thing you can do to someone is make them feel disgusted by themselves. – Unknown",
        "A person who has never made a mistake has never tried anything new. – Albert Einstein",
        "The more we know about life, the more we learn how to avoid it. – Unknown",
        "There are things in life that will disgust you and you can either let them control you or change how you think about them. – Unknown",
        "Nothing is more exhausting than being disgusted with yourself. – Unknown",
        "There is nothing in the world that can be compared with a truly disgusting person. – Unknown",
        "The feeling of disgust is one of the strongest emotions we can experience. – Unknown",
        "I have never encountered such disgust before. – Unknown"
    ],
    'fearful': [
        "Fear is only as deep as the mind allows. – Japanese Proverb",
        "The only thing we have to fear is fear itself. – Franklin D. Roosevelt",
        "Fear is a natural reaction to moving closer to the truth. – Pema Chodron",
        "Do one thing every day that scares you. – Eleanor Roosevelt",
        "Fear makes the wolf bigger than he is. – German Proverb",
        "Fear is the enemy of logic. – Frank Sinatra",
        "There is no illusion greater than fear. – Lao Tzu",
        "The cave you fear to enter holds the treasure you seek. – Joseph Campbell",
        "Fears are stories we tell ourselves. – Unknown",
        "Fear is not real. The only thing we have to fear is fear itself. – Unknown"
    ],
    'excited': [
        "The future belongs to those who believe in the beauty of their dreams. – Eleanor Roosevelt",
        "Excitement is the excitement you feel when you realize that the best is yet to come. – Unknown",
        "Life is either a daring adventure or nothing at all. – Helen Keller",
        "When you have a passion for something, excitement comes naturally. – Unknown",
        "Don’t just dream, live your dream. – Unknown",
        "The only way to do great work is to love what you do. – Steve Jobs",
        "The best way to predict the future is to create it. – Abraham Lincoln",
        "There’s nothing more exciting than an opportunity to make a difference. – Unknown",
        "Live with excitement, and let it fuel you to greatness. – Unknown",
        "Success is a journey, not a destination. – Arthur Ashe"
    ],
    'bored': [
        "Boredom is the feeling that everything is a waste of time; serenity, that nothing is. – Thomas Szasz",
        "Boredom is simply the absence of an interesting idea. – Edward de Bono",
        "The opposite of boredom is not excitement, but care. – Thomas Merton",
        "Boredom: the desire for desires. – Leo Tolstoy",
        "Sometimes the most productive thing you can do is relax. – Mark Black",
        "Don’t be afraid of boredom. It is just the space between opportunities. – Unknown",
        "You can’t force someone to pay attention to something that doesn’t excite them. – Unknown",
        "Boredom is the conviction that you can’t change things. – Unknown",
        "Sometimes you have to create your own excitement. – Unknown",
        "Boredom is the ultimate form of resistance. – Unknown"
    ],
    'confused': [
        "Confusion is the welcome mat at the door of creativity. – Michael J. Gelb",
        "When you’re not sure where to go, sometimes it’s better to just stop and wait for clarity. – Unknown",
        "Not everything makes sense right away, and that’s okay. – Unknown",
        "Confusion is the first step to understanding. – Unknown",
        "You’re not alone in your confusion; we all feel it at some point. – Unknown",
        "Life isn’t about finding yourself. Life is about creating yourself. – George Bernard Shaw",
        "Sometimes, confusion is the way life tells us to slow down. – Unknown",
        "When in doubt, follow your heart. – Unknown",
        "Everything will be clear in time. – Unknown",
        "The more you know, the more you realize you don’t know. – Aristotle"
    ],
    'hopeful': [
        "Hope is being able to see that there is light despite all of the darkness. – Desmond Tutu",
        "Hope is a waking dream. – Aristotle",
        "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
        "Hope is the thing with feathers that perches in the soul. – Emily Dickinson",
        "Hope is the last thing ever lost. – Italian Proverb",
        "Where there is no hope, there is no life. – W. Clement Stone",
        "A pessimist sees the difficulty in every opportunity; an optimist sees the opportunity in every difficulty. – Winston Churchill",
        "You must not lose faith in humanity. Humanity is an ocean; if a few drops of the ocean are dirty, the ocean does not become dirty. – Mahatma Gandhi",
        "Hope is a powerful thing. – Unknown",
        "Keep hope alive. – Jesse Jackson"
    ],
    'anxious': [
        "Anxiety is the dizziness of freedom. – Søren Kierkegaard",
        "Nothing in the affairs of men is worthy of anxiety. – Plato",
        "Anxiety is a thin stream of fear trickling through the mind. If encouraged, it cuts a channel into which all other thoughts are drained. – Arthur Somers Roche",
        "There is only one way to avoid criticism: do nothing, say nothing, and be nothing. – Aristotle",
        "Anxiety does not empty tomorrow of its sorrows, but only empties today of its strength. – Charles Spurgeon",
        "The greatest weapon against stress is our ability to choose one thought over another. – William James",
        "Don’t worry about things you can’t control. – Unknown",
        "Anxiety is the space between the present and the future. – Unknown",
        "The best way out is always through. – Robert Frost",
        "Breathe. You are stronger than you think. – Unknown"
    ],
    'content': [
        "Contentment is natural wealth, luxury is artificial poverty. – Socrates",
        "The greatest wealth is to live content with little. – Plato",
        "The most contented people are those who find joy in the simple things. – Unknown",
        "A contented mind is the greatest blessing a man can enjoy in this world. – Joseph Addison",
        "Contentment is not the fulfillment of what you want, but the realization of how much you already have. – Unknown",
        "True contentment is not about getting what you want, but learning to want what you have. – Unknown",
        "The secret to happiness is not in doing what one likes, but in liking what one does. – James M. Barrie",
        "Contentment is the true wealth. – Unknown",
        "If you want to be rich, be content with what you have. – Unknown",
        "Contentment is the key to happiness. – Unknown"
    ],
    'grateful': [
        "Gratitude is not only the greatest of virtues, but the parent of all the others. – Marcus Tullius Cicero",
        "Gratitude is the fairest blossom which springs from the soul. – Henry Ward Beecher",
        "Feeling gratitude and not expressing it is like wrapping a present and not giving it. – William Arthur Ward",
        "Gratitude turns what we have into enough. – Aesop",
        "Silent gratitude isn’t much use to anyone. – Gertrude Stein",
        "Gratitude is when memory is stored in the heart and not in the mind. – Lionel Hampton",
        "Gratitude is the sign of noble souls. – Aesop",
        "Gratitude is the best attitude. – Unknown",
        "Gratitude is the most exquisite form of courtesy. – Jacques Maritain",
        "A grateful heart is a magnet for miracles. – Unknown"
    ],
    'guilty': [
        "Guilt is the most powerful source of negative energy that we can hold onto. – Unknown",
        "Guilt is a thief who steals happiness. – Unknown",
        "Guilt is the one feeling that cannot be ignored. – Unknown",
        "Guilt is the feeling we experience when we have wronged someone else. – Unknown",
        "We are more often guilty of our weaknesses than of our wrongs. – Francois de La Rochefoucauld",
        "Guilt is something you feel when you have done something wrong. – Unknown",
        "Guilt is a powerful emotion that can consume you if you let it. – Unknown",
        "Don’t live with guilt. Learn from your mistakes and move forward. – Unknown",
        "The burden of guilt is often heavier than the weight of wrong. – Unknown",
        "Guilt is the price we pay for our mistakes. – Unknown"
    ],
    'embarrassed': [
        "Embarrassment is a temporary feeling. It’s only a moment of discomfort in an otherwise beautiful life. – Unknown",
        "It’s not the mistake that matters, it’s how you handle it. – Unknown",
        "Embarrassment is the first step to personal growth. – Unknown",
        "It’s okay to be embarrassed. It means you care. – Unknown",
        "If you’re not embarrassed by your first product, you’ve launched too late. – Reid Hoffman",
        "Embarrassment is the price we pay for being ourselves. – Unknown",
        "Embarrassment is a great teacher if you let it be. – Unknown",
        "It’s just a moment. Don’t let it define you. – Unknown",
        "It’s okay to feel embarrassed, just don’t let it stop you from moving forward. – Unknown",
        "Embarrassment is simply the body’s way of reminding you that you’re human. – Unknown"
    ],
    'ashamed': [
        "Shame is a soul-eating emotion. – Carl Jung",
        "Shame is the most powerful, master emotion. It’s the fear that we’re not good enough. – Brené Brown",
        "Shame corrodes the very part of us that believes we are capable of change. – Brené Brown",
        "You are not your mistakes. – Unknown",
        "The worst feeling is feeling ashamed of yourself. – Unknown",
        "Shame is an emotion that arises from the belief that we are unworthy of love or respect. – Unknown",
        "Don’t let shame define you. – Unknown",
        "Shame is not a reflection of who you are, but of your behavior. – Unknown",
        "It’s not the mistake that defines you; it’s what you do after the mistake that matters. – Unknown",
        "Shame is the root of all suffering. – Unknown"
    ],
    'nervous': [
        "Nervousness is the first step towards success. – Unknown",
        "The only way to get over a fear of something is to do it. – Unknown",
        "The moment you start being nervous is the moment you grow. – Unknown",
        "Nervousness is a sign you care, and that’s a good thing. – Unknown",
        "Nervousness is the energy that keeps you on your toes. – Unknown",
        "Nervousness is the shadow of fear. – Unknown",
        "Being nervous is part of the process, embrace it. – Unknown",
        "Don’t let nervousness hold you back. It’s a sign you’re doing something important. – Unknown",
        "The nerves you feel before doing something great is your passion trying to push through. – Unknown",
        "Nervousness is the body’s natural response to the unknown. – Unknown"
    ]
}
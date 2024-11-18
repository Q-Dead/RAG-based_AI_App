from typing import Final

TITLE: Final[str] = "Own Info Retriever: :violet[A RAG Chatbot] :robot_face:"
HEADER_1: Final[str] = "About"
HEADER_2: Final[str] = "Hi, I'm Jasper John! 🙋🏼‍♂️"
LAYOUT: Final[str] = "wide"
COLOR_VIOLET: Final[str] = "violet"

HEADER_1_MARKDOWN: Final[str] = """ :violet[A personalized] chatbot powered by Retrieval-Augmented Generation (RAG) technology. 
                    It efficiently retrieves and generates responses based on a document containing 
                    personal information"""

HEADER_2_MARKDOWN: Final[str] = """ :violet[Feel free] to ask the bot any questions to learn more about me and my background."""

CCS_MARKDOWN: Final[str] =  """
                            <style>
                                .st-emotion-cache-1c7y2kd {
                                    flex-direction: row-reverse;
                                    text-align: right;
                                }
                                .stApp[data-teststate=running] .stChatInput textarea,
                                .stApp[data-test-script-state=running] .stChatInput textarea {
                                    display: none;
                                }
                                .st-emotion-cache-16nc0hx{
                                    overflow-y: auto;
                                    overflow-x: hidden;
                                    height: 600px;
                                    max-height: 600px;
                                    border: 1px solid #ccc;
                                    display: flex;
                                    flex-direction: column-reverse;
                                }
                                .st-emotion-cache-16nc0hx::-webkit-scrollbar {
                                    width: 8px;
                                }
                                .st-emotion-cache-16nc0hx::-webkit-scrollbar-thumb {
                                    background: #888;
                                    border-radius: 4px;
                                }
                            </style>
                            """

JQUERY_1_MARKDOWN: Final[str] =   """
                                <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
                                <script>
                                function scrollToBottom() {
                                    $(".st-emotion-cache-1wmy9hl ").animate({ scrollTop: $('.st-emotion-cache-1wmy9hl').prop("scrollHeight")}, 1000);
                                }
                                </script>
                                """

LOADING_JQUERY_1: Final[str] = '<script>scrollToBottom();</script>'


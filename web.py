<style>
html,
body {
  min-width: 290px;
  color: #4d4e53;
  background-color: #ffffff;
  font-family: "Open Sans", Arial, sans-serif;
  line-height: 1.5;
}

#sidebar {
  position: fixed;
  min-width: 290px;
  top: 0px;
  left: 0px;
  width: 300px;
  height: 100%;
  border-right: solid;
  border-color: rgba(0, 22, 22, 0.4);
}

h2 {
  color: black;
  margin: 10px;
  text-align: center;
  font-size: 1.8em;
  font-weight: thin;
}

#documentation h2 {
  text-align: left;
  margin: 0px;
}

#sidebar ul {
  height: 88%;
  padding: 0;
  overflow-y: auto;
  overflow-x: hidden;
}

#sidebar li {
  color: #4d4e53;
  border-top: 1px solid;
  list-style: none;
  position: relative;
  width: 100%;
}

#sidebar .nav-item {
  display: block;
  padding: 10px 30px;
  color: #4d4e53;
  text-decoration: none;
  cursor: pointer;
}

#documentation {
  position: absolute;
  margin-left: 310px;
  padding: 20px;
  margin-bottom: 110px;
}

section article {
  color: #4d4e53;
  margin: 15px;
  font-size: 0.96em;
}

section li {
  margin: 15px 0px 0px 20px;
}

pre {
  display: block;
  text-align: left;
  white-space: pre-line;
  position: relative;
  word-break: normal;
  word-wrap: normal;
  line-height: 2;
  background-color: #f7f7f7;
  padding: 15px;
  margin: 10px;
  border-radius: 5px;
}

.hscroll {
  overflow-x: auto;
}

table {
  caption-side: bottom;
  border-collapse: collapse;
}

@media only screen and (max-width: 815px) {
  /* For mobile phones: */
  #sidebar ul {
    border: 1px solid;
    height: 207px;
  }

  #sidebar {
    background-color: white;
    position: absolute;
    top: 0;
    padding: 0;
    margin: 0;
    width: 100%;
    max-height: 275px;
    border: none;
    z-index: 1;
    border-bottom: 2px solid;
  }

  #documentation {
    position: relative;
    margin-left: 0px;
    margin-top: 270px;
  }
}

@media only screen and (max-width: 400px) {
  #documentation {
    margin-left: -10px;
  }
}

<style/>
<body>
  <nav id="sidebar">
    <h2>HTML</h2>
    <ul>
      <li><a class="nav-item" href="#Introduction">Introduction</a></li>
      <li>
        <a class="nav-item" href="#html_editors">HTML Editors</a>
      </li>
      <li>
        <a class="nav-item" href="#html_elements">HTML Elements</a>
      </li>
      <li><a class="nav-item" href="#html_attributes">HTML Attributes</a></li>
      <li><a class="nav-item" href="#html_heading">HTML Heading</a></li>
      <li>
        <a class="nav-item" href="#html_paragraph">HTML Paragraph</a>
      </li>
      <li><a class="nav-item" href="#html_style">HTML Style</a></li>
      <li><a class="nav-item" href="#html_formatting">HTML Formatting</a></li>
      <li><a class="nav-item" href="#reference">Reference</a></li>
    </ul>
  </nav>
  <main id="documentation">
    <section id="Introduction">
      <h2>Introduction</h2>
      <article>
        <p>
          HTML is an acronym for HyperText Markup Language, and it is the
          standard language for creating web-pages. Every web page you surf on
          your browser is built using HTML. The primary use of HTML to provide
          a proper structure to the web-page so all the content or data of the
          page could represent adequately. A stand-alone HTML can create only
          static and skeleton looking black and white pages, but with the help
          of CSS and JavaScript , we can create a more interactive and
          intuitive web-page. When we try to visit a website or click on the
          link, we basically request the server to show us the page, then the
          server acts on our request and sends us an appropriate HTML document
          as a response. Then this HTML document parsed by browse, and we able
          to see the content.
        </p>
        <h3>HTML Document</h3>
        <pre>
&lt;!DOCTYPE html&gt;
                &lt;html&gt;
                &lt;head&gt;
                &lt;title&gt;Page Title&lt;/title&gt;
                &lt;/head&gt;
                &lt;body&gt;

                &lt;h1&gt;This is a Heading&lt;/h1&gt;
                &lt;p&gt;This is a paragraph.&lt;/p&gt;

                &lt;/body&gt;
                &lt;/html&gt;</pre>
      </article>
    </section>
    <section id="html_editors">
      <h2>HTML Editors</h2>
      <article>
        <p>
          However, you can use notepad to create and edit HTML documents, but
          we recommend to install an open-source editor. There are many free
          to use text-editor software present on the internet, which provides
          a better interactive User interface and some add-on functionality
          which you miss on a notepad.
        </p>
        <p>Here is the list of top 4 HTML text editors you can pick:</p>

        <ul>
          <li>Sublime Text Editor</li>
          <li>Notepad++</li>
          <li>Visual Studio Code</li>
          <li>Atom</li>
        </ul>
      </article>
    </section>
    <section id="html_elements">
      <h2>HTML Elements</h2>
      <article>
        <p>
          The HTML elements provide the semantic meaning to the web-page
          content. We usually interchangeably use the term HTML elements and
          tags, but technically both are different. An HTML tag is just a
          character inside the angle bracket<>, whereas the HTML element is a
            collection of starting tag, its attribute, content and end tag. For
            example:
        </p>
        <pre>&lt;p class= "para"&gt; Hello World &lt;/p&gt;</pre>
      </article>
    </section>
    <section id="html_attributes">
      <h2>HTML Attributes</h2>
      <article>
        <p>
          In HTML, the attributes are used to provide additional information
          about the elements. For most of the HTML elements, attributes are
          optional, but there are some elements where we have to deliver the
          attributes. Attributes always specified within the opening tag of
          the HTML element and they specified in a name and value pair.
          <strong> Example </strong>
        </p>
        <pre>&lt;image src= "cat.jpg" alt ="cat image"&gt;</pre>
        <p>
          In this example src ="cat.jpg" and alt="cat image" are two
          attributes where src and alt are attributes name and "cat.jpg" and
          "cat image" are attributes values. Here alt attribute is optional,
          but src is mandatory because src specify which image to show. There
          should be at least one space gap between two attributes, and the
          value of the attributes must have resided in the double inverted
          comma. Some most important HTML
        </p>
      </article>
    </section>
    <section id="html_heading">
      <h2>HTML Heading</h2>
      <p>
        To display the section heading, title or subtitle we can use the HTML
        heading tags. In HTML 5 we have 6 heading tags start from &lt;h1&gt;
        up to &lt;h6&gt;, where &lt;h1&gt; specify the largest heading and
        &lt;h6&gt; represent the smallest or sub heading. If the content is
        specified by heading tags, then it would be displayed large and bold
        as compared to other text content present on the web-page.
        <strong> Example </strong>
      </p>
      <pre>
&lt;h1&gt;First Heading &lt;/h1&gt;
            &lt;h2&gt;Second Heading &lt;/h2&gt;
            &lt;h3&gt;Third Heading &lt;/h3&gt;
            &lt;h4&gt;Forth Heading &lt;/h4&gt;
            &lt;h5&gt;Fifth Heading &lt;/h5&gt;
            &lt;h6&gt;Sixth Heading &lt;/h6&gt;</pre>
    </section>
    <section id="html_paragraph">
      <h2>HTML Paragraph</h2>
      <article>
        <p>
          In HTML paragraphs can be defined using &lt;p&gt; element. Paragraph
          text always starts from a new line, the browser parsed the &lt;p&gt;
          tag and automatically add some margin and white space after the end
          &lt;/p&gt; tag.
        </p>
        <pre>
&lt;p&gt; Hello! and Welcome to TechGeekBuzz &lt;/p&gt;
                &lt;p&gt; Here you get to know all about the latest technology. &lt;/p&gt;</pre>
      </article>
    </section>
    <section id="html_style">
      <h2>HTML Style</h2>
      <article>
        <p>
          Every browser has a specific engine that parses the HTML document and displays a default style of the page content.
        </p>
        <pre>&lt;body style="background-color:yellow;"&gt;

                &lt;h1&gt;TechGeekBuzz&lt;/h1&gt;
                &lt;p&gt;Welcome to TechGeekBuzz.&lt;/p&gt;
                
                &lt;/body&gt;</pre>
      </article>
    </section>
    <section id="html_formatting">
      <h2>HTML Formatting</h2>
      <article>
        <p>
          In HTML, we have many special elements that can provide special meaning to text content.
        </p>
        <div class="hscroll">
          <table>
            <tbody>
              <tr>
                <td>
                  <a href="https://www.techgeekbuzz.com/html-elements/">
                    HTML Elements
                  </a>
                </td>
                <td>
                  Description
                </td>
              </tr>
              <tr>
                <td>
                  &lt;b&gt;
                </td>
                <td>
                  Bold the text
                </td>
              </tr>
              <tr>
                <td>
                  &lt;strong&gt;
                </td>
                <td>
                  An alternative for &lt;b&gt;, which tell that this text is essential.
                </td>
              </tr>
              <tr>
                <td>
                  &lt;i&gt;
                </td>
                <td>
                  Italic the text
                </td>
              </tr>
              <tr>
                <td>
                  &lt;em&gt;
                </td>
                <td>
                  Similar to italic but used when we want to emphasize the text.
                </td>
              </tr>
              <tr>
                <td>
                  &lt;mark&gt;
                </td>
                <td>
                  It marks the text with a default "yellow" background colour
                </td>
              </tr>
              <tr>
                <td>
                  &lt;small&gt;
                </td>
                <td>
                  Decrease the text size
                </td>
              </tr>
              <tr>
                <td>
                  &lt;del&gt;
                </td>
                <td>
                  It prints a cross line over the text.
                </td>
              </tr>
              <tr>
                <td>
                  &lt;ins&gt;
                </td>
                <td>
                  Represents the inserted text by putting an underline.
                </td>
              </tr>
              <tr>
                <td>
                  &lt;sub&gt;
                </td>
                <td>
                  This element is used to display the subscript.
                </td>
              </tr>
              <tr>
                <td>
                  &lt;sup&gt;
                </td>
                <td>
                  It can make a text superscript.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </article>
    </section>

    <section id="reference">
      <h2>Reference</h2>
      <article>
        <ul>
          <li>
            All the documentation in this page is taken from
            <a href="https://www.techgeekbuzz.com/tutorial/html/" target="_blank">HTML Tutorial</a>
          </li>
        </ul>
      </article>
    </section>
  </main>
</body>

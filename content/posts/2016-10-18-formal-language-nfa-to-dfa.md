title: Formal language 作業：nfa 轉 dfa
slug: formal-language-nfa-to-dfa
date: 2016-10-18T12:39:14T+0800
category: graduate school
tags: formal language, dfa, nfa

## NFA

{% graphviz
    dot {
        digraph nfa {
            rankdir = "LR";
            init [shape=none label=""];
            end [shape=none label=""];
            q1 [shape=doublecircle];
            init -> q0;
            q0 -> q1 [label="0,1"];
            q1 -> q0 [label="0"];
            q1 -> q1 [label="1"];
            q1 -> q2 [label="0,λ"];
            q2 -> q1 [label="1"];
            q2 -> end [label="" penwidth=0 arrowhead=none];
        }
    }
%}

## DFA

{% graphviz
    dot {
        digraph dfa {
            rankdir = "LR";
            init [shape=none label=""];
            end [shape=none label=""];
            q0 [label="{q0}"];
            q1 [shape=doublecircle, label="{q1,q2}"];
            q2 [label="{q0,q2}"];
            init -> q0;
            q0 -> q1 [label="0,1"];
            q1 -> q1 [label="1"];
            q1 -> q2 [label="0"];
            q2 -> q1 [label="0,1"];
            q2 -> end [label="" penwidth=0 arrowhead=none];
        }
    }
%}


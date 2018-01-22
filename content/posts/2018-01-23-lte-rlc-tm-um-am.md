title: LTE RLC AM/UM/TM
slug: lte-rlc-tm-um-am
date: 2018-01-23 02:36:55
category: 3gpp
tags: lte, rlc, spec

這是讀 3GPP LTE spec. 的筆記，不保證完全正確。有錯請指教，謝謝。

LTE 的 RLC (radio link control) 定義了三個模式：TM/UM/AM (3GPP TS 36.322)

* TM: Transparent Mode
* UM: Unacknowledged Mode
* AM: Acknowledged Mode

在 4.2 RLC architecture 中定義了這三個 RLC entity 對應傳送的 logical channels

* TM: BCCH, BR-BCCH, DL/UL CCCH, PCCH and SBCCH.
* UM: DL/UL DTCH, MCCH, MTCH, SC-MCCH, SC-MTCH or STCH.
* AM: DL/UL DCCH or DL/UL DTCH.

```
BCCH: Broadcast Control CHannel
BR-BCCH: Bandwidth Reduced Broadcast Control CHannel
CCCH: Common Control CHannel
PCCH: Paging Control CHannel
SBCCH: Sidelink Broadcast Control Channel
DTCH: Dedicated Traffic CHannel
MCCH: Multicast Control Channel
SC-MCCH: Single Cell Multicast Control Channel
SC-MTCH: Single Cell Multicast Transport Channel
STCH: Sidelink Traffic Channel
DCCH: Dedicated Control CHannel
DTCH: Dedicated Traffic CHannel
```

TM 對應的動作最單純，從上層收到 SDU(Service Data Unit) 之後，便往下層送 TMD PDU(TM Data Protocol Data Unit)。不對 RLC SDU 做分割也不串接，收到什麼資料就轉成 TMD PDU 往下層送，也不加任何 RLC 的 header。若是往下層收到 TMD PDU，則直接往上層送(因為這就直接是 RLC SDU了)。

UM 則是會依著下層給的資訊把 SDU 分割或是串接成 UMD PDU(UM Data Protocol Data Unit) 來符合可用的 RLC PDU 大小。所以傳送前要加上 RLC 的 header。當UM 收到 UMD PDU 的時候，要能夠偵測 duplication 並丟棄 duplicated RLC data PDU；還要依序號重排；重組 SDU 並依序號的順序往上層送；無法重組的 SDU 就丟棄。

AM 傳送時同樣會依著下層給的資訊把 SDU 分割或是串接成 AMD PDU(AM Data Protocol Data Unit) 來符合可用的 RLC PDU 大小。但是 AM 支援重送 RLC data PDU (ARQ Automatic Repeat reQuest)。AM 可以在下層給的 RLC PDU 大小不符的時候重新分割。另外，AM 還會傳送與接收 RLC control PDU - STATUS PDU。所以在接收的時候，AM 也要能偵測 duplication 並丟棄 duplicated RLC data PDU；也要依序重排；偵測下層是否掉封包並要求傳送端的 AM 重新傳送；重組 SDU 並依序往上層送；無法重組的 SDU 就丟棄。

從上面的描述及 4.3.1 Services provided to upper layers 中提到的，
> The following services are provided by RLC to upper layer:
>
> * TM data transfer;
> * UM data transfer;
> * AM data transfer, including indication of successful delivery of upper layers PDUs.

可以知道，AM 提供最高可靠度的傳送管道。


底下附上 OpenAirInterface 的實作的相關函式呼叫：

* `rlc_data_ind` RLC 接收端與 TM/UM/AM

{% graphviz
    dot {
        strict digraph  {
            "2bd22491feb1deaea2f70a831b1646e3" [label="openair2/LAYER2/RLC/TM_v9.3.0\nrlc_tm.c:35\nrlc_tm_send_sdu"];
            dc2034e22564a01ca44f4ed6229db1c5 [label="openair2/LAYER2/RLC/TM_v9.3.0\nrlc_tm.c:127\nrlc_tm_rx"];
            "4a5e7b9ec9d2888b3d3befaf67e17c27" [label="openair2/LAYER2/RLC/UM_v9.3.0\nrlc_um_reassembly.c:110\nrlc_um_send_sdu"];
            "3e592ab11cc5901b79754d4cc8a2b8e2" [label="openair2/LAYER2/PDCP_v10.1.0\npdcp.c:413\npdcp_data_ind"];
            "1754de08a5103434660852917ff9a8af" [label="openair2/LAYER2/RLC\nrlc.c:551\nrlc_data_ind"];
            "54cbeb597ee91dd4eb08058889e3620a" [label="openair2/LAYER2/RLC/UM_v9.3.0\nrlc_um_dar.c:204\nrlc_um_try_reassembly"];
            "0fb0a9be7be729feea024a41aff0278e" [label="openair2/LAYER2/RLC/AM_v9.3.0\nrlc_am_reassembly.c:90\nrlc_am_send_sdu"];
            c426a75fb82cfcd0aba965adba68abaa [label="openair2/LAYER2/RLC/AM_v9.3.0\nrlc_am_reassembly.c:212\nrlc_am_reassemble_pdu"];
            "2bd22491feb1deaea2f70a831b1646e3" -> "1754de08a5103434660852917ff9a8af";
            dc2034e22564a01ca44f4ed6229db1c5 -> "2bd22491feb1deaea2f70a831b1646e3";
            "4a5e7b9ec9d2888b3d3befaf67e17c27" -> "1754de08a5103434660852917ff9a8af";
            "1754de08a5103434660852917ff9a8af" -> "3e592ab11cc5901b79754d4cc8a2b8e2";
            "54cbeb597ee91dd4eb08058889e3620a" -> "4a5e7b9ec9d2888b3d3befaf67e17c27";
            "0fb0a9be7be729feea024a41aff0278e" -> "1754de08a5103434660852917ff9a8af";
            c426a75fb82cfcd0aba965adba68abaa -> "0fb0a9be7be729feea024a41aff0278e";
        }
    }
%}

* `rlc_data_req` RLC 傳送端與 TM/UM/AM

{% graphviz
    dot {
        strict digraph  {
            d2a6cd427fb72850aa271f78b8e2a777 [label="openair2/LAYER2/RLC\nrlc_rrc.c:777\nrrc_rlc_data_req"];
            "59a6b4d3800eaaf145bd322f9d96a937" [label="openair2/LAYER2/RLC\nrlc.c:315\nrlc_data_req"];
            "4d97d2f46f875cecf5419a6115156e49" [label="openair2/LAYER2/RLC/AM_v9.3.0\nrlc_am.c:1133\nrlc_am_data_req"];
            a65c968e21c42e4f249a1abf6db253ed [label="openair2/LAYER2/RLC/TM_v9.3.0\nrlc_tm.c:212\nrlc_tm_data_req"];
            "0e0d912743f320498f7d32ca931aff05" [label="openair2/LAYER2/RLC\nrlc_mpls.c:35\nmpls_rlc_data_req"];
            a87f381af66fd68e68c8c596b1ce4b9a [label="openair2/LAYER2/PDCP_v10.1.0\npdcp.c:80\npdcp_data_req"];
            "8ad73b4da2d1746c7bf03f54e750fc03" [label="openair2/LAYER2/RLC/UM_v9.3.0\nrlc_um.c:681\nrlc_um_data_req"];
            d2a6cd427fb72850aa271f78b8e2a777 -> "59a6b4d3800eaaf145bd322f9d96a937";
            "59a6b4d3800eaaf145bd322f9d96a937" -> "4d97d2f46f875cecf5419a6115156e49";
            "59a6b4d3800eaaf145bd322f9d96a937" -> a65c968e21c42e4f249a1abf6db253ed;
            "59a6b4d3800eaaf145bd322f9d96a937" -> "8ad73b4da2d1746c7bf03f54e750fc03";
            "0e0d912743f320498f7d32ca931aff05" -> "59a6b4d3800eaaf145bd322f9d96a937";
            a87f381af66fd68e68c8c596b1ce4b9a -> "59a6b4d3800eaaf145bd322f9d96a937";
        }
    }
%}

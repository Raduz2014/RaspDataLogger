$.cookie.json = true;
//MainApp object
var MainApp = {};

var zzCookie = {
    createLoginCookie: function () {
        var c = $.cookie('login', '1', { expires: 31, path: '/' });
        return c;
    },
    isLogIn: function () {
        var clogin = $.cookie('login');
        if (clogin && clogin === "1") {
            //if exists and logged in
            return 1;
        }
        else if (clogin && clogin === "0") {
            //if exists and logged out
            return 0;
        }
        //if doesn't exists
        return -1;
    },
    setLogState: function (s) {
        var clogin = $.cookie('login');
        if (clogin) {
            s ? $.cookie('login', "1") : $.cookie('login', "0");
        }
    },

    getLoginCookie: function () {
        return $.cookie('login', Number);
    },
    removeLoginCookie: function () {
        return $.removeCookie('login');
    }
};
var userSettings = {};
var currentView;

(function (app, zzCookie) {
    var MainMobileApp; //KendoMobieApplication

    var currentView; // Current view selected
    var selectProfile;

    var ServiceModel = kendo.data.Model.define({
        id: "service_name", // the identifier of the model
        fields: {
            "service_name": {
                type: "string"
            },
            "service_code": {
                type: "number"
            }
        }
    });
   
    var
        modelHome = kendo.observable({
            onInit: function (e) {
                console.log("Home Model:", e);
                var logState = zzCookie.isLogIn();
                if (logState != 1) {
                    window.location.replace("login.html");
                }                
            }
        }),
        modelLogout = kendo.observable({
            onLogOut: function (e) {
                console.log("onLogOut:", e);
                if (zzCookie.isLogIn()) {
                    zzCookie.setLogState(false);
                    window.location.replace("login.html");
                }

            },
            onInit: function (e) {
                console.log("Logout Model:", e);
            }
        }),
        modelAbout = kendo.observable({
            onInit: function (e) {
                console.log("About Model:", e);
            },
            onLogOut: function (e) {
                var logState = zzCookie.isLogIn();
                if (logState == 1) {
                    e.button.text("Log In");
                    zzCookie.setLogState(false);
                    app.navigate("#login");
                }
                else if (logState == 0) {
                    zzCookie.setLogState(true);
                    e.button.text("Log Out");
                    app.navigate("#home");
                }
            },
        }),
        modelWificard = kendo.observable({
            modeState: "wifi",//wifi or ap
            onInit: function (e) {
                console.log("Wifi model onInit", e);

            },
            saveSettings: function (e) {
                console.log("saveSettings", e);
                console.log("Model wificard", this);
            },
            resetSettings: function (e) {
                console.log("resetSettings", e);
                console.log("Model wificard", this);

            },
        }),
        modelLanInterface = kendo.observable({}),
        modelSettingsFtp = kendo.observable({}),
        modelCfgModbus = kendo.observable({

            onInit: function (e) {
                console.log("model ConfigModbus",e);
            },
            saveCfg: function (e) {
                console.log("Save modbus config:", e);

            },
        }),
        modelDeviceDrivers = kendo.observable({}),
        modelDevices = kendo.observable({}),
        modelReadProfiles = kendo.observable({
            profiles: new kendo.data.DataSource({
                data: [
                        {
                            NameProfile: "Low",
                            MeterServices: [
                                { service_name: "Temperatue 1", service_code: 430 },
                                { service_name: "Voltage 4", service_code: 204 },
                                { service_name: "Measure 1", service_code: 403 },
                            ]
                        },
                        {
                            NameProfile: "Medium",
                            MeterServices: [
                                { service_name: "Temperatue 1", service_code: 430 },
                                { service_name: "Temperatue 2", service_code: 431 },
                                { service_name: "Voltage 6", service_code: 206 },
                                { service_name: "Voltage 7", service_code: 207 },
                                { service_name: "Measure 1", service_code: 403 },
                                { service_name: "Measure 2", service_code: 404 },

                            ]
                        },
                        {
                            NameProfile: "High",
                            MeterServices: [
                                { service_name: "Temperatue 1", service_code: 401 },
                                { service_name: "Voltage 2", service_code: 204 },
                                { service_name: "Debit", service_code: 403 },
                                { service_name: "Debit", service_code: 403 },
                                { service_name: "Debit", service_code: 403 },
                                { service_name: "Debit 5", service_code: 505 },
                                { service_name: "TTur 1", service_code: 601 },
                                { service_name: "TRetur 3", service_code: 606 },
                                { service_name: "Energy index 1", service_code: 607 },
                                { service_name: "Energy index 3", service_code: 609 },
                                { service_name: "Volum 1", service_code: 611 },
                                { service_name: "Volum Aux 1", service_code: 612 },
                                { service_name: "Volum Aux 2", service_code: 613 },
                            ]
                        },
                        {
                            NameProfile: "Custom 1",
                            MeterServices: [
                                   { service_name: "Measure 1", service_code: 403 },
                                   { service_name: "Debit 1", service_code: 501 },
                                   { service_name: "TRetur 1", service_code: 604 },
                                   { service_name: "Energy index 1", service_code: 607 },
                            ]
                        },
                        {
                            NameProfile: "Custom 2",
                            MeterServices: [
                                { service_name: "Volum 1", service_code: 611 },
                                { service_name: "Volum Aux 1", service_code: 612 },
                                { service_name: "Volum Aux 2", service_code: 613 },
                            ]
                        },
                ],
                batch: true,
                schema: {
                    model: {
                        id: "NameProfile",
                        fields: {
                            NameProfile: "NameProfile",
                            MeterServices: { ServiceModel }
                        }
                    }
                },
                sync: function (e) { console.log("profile ds sync complete", e);}
            }),

            //[
            //    {
            //        nameProfile: "Low",
            //        meterServices: [
            //            { service_name: "Temperatue 1", service_code: 401 },
            //            { service_name: "Voltage 2", service_code: 204 },
            //            { service_name: "Debit", service_code: 403 },
            //        ]
            //    },
            //    {
            //        nameProfile: "Medium",
            //        meterServices: [
            //            { service_name: "Temperatue 1", service_code: 401 },
            //            { service_name: "Voltage 2", service_code: 204 },
            //            { service_name: "Voltage 2", service_code: 204 },
            //            { service_name: "Voltage 2", service_code: 204 },
            //            { service_name: "Debit", service_code: 403 },
            //        ]
            //    },
            //    {
            //        nameProfile: "High",
            //        meterServices: [
            //            { service_name: "Temperatue 1", service_code: 401 },
            //            { service_name: "Voltage 2", service_code: 204 },
            //            { service_name: "Debit", service_code: 403 },
            //            { service_name: "Debit", service_code: 403 },
            //            { service_name: "Debit", service_code: 403 },
            //        ]
            //    },
            //    {
            //        nameProfile: "Custom 1",
            //        meterServices: [
            //            { service_name: "Temperatue 1", service_code: 401 },
            //            { service_name: "Voltage 2", service_code: 204 },
            //            { service_name: "Debit", service_code: 403 },
            //            { service_name: "Debit", service_code: 403 },
            //            { service_name: "Debit", service_code: 403 },
            //        ]
            //    },
            //    {
            //        nameProfile: "Custom 2",
            //        meterServices: [
            //            { service_name: "Temperatue 1", service_code: 401 },
            //            { service_name: "Voltage 2", service_code: 204 },
            //            { service_name: "Debit", service_code: 403 },
            //            { service_name: "Debit", service_code: 403 },
            //            { service_name: "Debit", service_code: 403 },
            //        ]
            //    },
            //],
            onInit: function (e) {
                console.log("onInit>>model read profiles", e);

            },
            onSave: function (e) {
                console.log("save values",e)
            },
            onAddNewProfile: function (e) {
                console.log("add new read profile", e);

                var $txtProfileNameCtrl = $("#txtProfileNameInput");
                var ctrlVal = $txtProfileNameCtrl.val();
                var profileName = ctrlVal == "" ? "Custom " : ctrlVal;

                var p =
                    {
                        NameProfile: profileName,
                        MeterServices: []
                    };
                this.profiles.add(p);
                e.preventDefault();
            }
        }), 
        modelDeviceServices = kendo.observable({
            deviceServices: new kendo.data.DataSource({
                data: [
                    { serviceID: 1, service_name: "Temperatue 1", service_code: 430 },
                    { serviceID: 2, service_name: "Temperatue 2", service_code: 431 },
                    { serviceID: 3, service_name: "Temperatue 3", service_code: 432 },
                    { serviceID: 4, service_name: "Temperatue 4", service_code: 433 },

                    { serviceID: 5, service_name: "Voltage 1", service_code: 201 },
                    { serviceID: 6, service_name: "Voltage 2", service_code: 202 },
                    { serviceID: 7, service_name: "Voltage 3", service_code: 203 },
                    { serviceID: 8, service_name: "Voltage 4", service_code: 204 },
                    { serviceID: 9, service_name: "Voltage 5", service_code: 205 },
                    { serviceID: 10, service_name: "Voltage 6", service_code: 206 },
                    { serviceID: 11, service_name: "Voltage 7", service_code: 207 },

                    { serviceID: 12, service_name: "Measure 1", service_code: 403 },
                    { serviceID: 13, service_name: "Measure 2", service_code: 404 },
                    { serviceID: 14, service_name: "Measure 3", service_code: 405 },
                    { serviceID: 15, service_name: "Measure 4", service_code: 406 },
                    { serviceID: 16, service_name: "Measure 5", service_code: 407 },
                    { serviceID: 17, service_name: "Measure 6", service_code: 408 },
                    { serviceID: 18, service_name: "Measure 7", service_code: 409 },
                    { serviceID: 19, service_name: "Measure 8", service_code: 410 },
                    { serviceID: 20, service_name: "Measure 9", service_code: 411 },
                    { serviceID: 21, service_name: "Measure 10", service_code: 412 },

                    { serviceID: 22, service_name: "Debit 1", service_code: 501 },
                    { serviceID: 23, service_name: "Debit 2", service_code: 502 },
                    { serviceID: 24, service_name: "Debit 3", service_code: 503 },
                    { serviceID: 25, service_name: "Debit 4", service_code: 504 },
                    { serviceID: 26, service_name: "Debit 5", service_code: 505 },
                    { serviceID: 27, service_name: "TTur 1", service_code: 601 },
                    { serviceID: 28, service_name: "TTur 2", service_code: 602 },
                    { serviceID: 29, service_name: "TTur 3", service_code: 603 },
                    { serviceID: 30, service_name: "TRetur 1", service_code: 604 },
                    { serviceID: 31, service_name: "TRetur 2", service_code: 605 },
                    { serviceID: 33, service_name: "TRetur 3", service_code: 606 },
                    { serviceID: 34, service_name: "Energy index 1", service_code: 607 },
                    { serviceID: 35, service_name: "Energy index 2", service_code: 608 },
                    { serviceID: 36, service_name: "Energy index 3", service_code: 609 },
                    { serviceID: 37, service_name: "Volum 1", service_code: 611 },
                    { serviceID: 38, service_name: "Volum Aux 1", service_code: 612 },
                    { serviceID: 39, service_name: "Volum Aux 2", service_code: 613 },
                ],
                batch: true,
                schema: {
                    model: {
                        id: "serviceID",
                        fields: {
                            serviceID: { editable: false, nullable: true },
                            serviceID: { type: "number" },
                        }
                    }
                },
            }),
            onAddNewService: function (e) {
                console.log("onAddNewService", e);
                var s = { service_name: "", service_code: 0 };
                this.deviceServices.add(s);
                e.preventDefault();
            },
            onSave: function (e) {
                console.log("save values", e)
            },
        }),
        modelTaskScheduled = kendo.observable({});


    function closeProfileServEditModalView(e) {
        console.log("CLOSE profile serv edit ModalView", e);        

    }

    var initProfileServiceCount = 0;

    function onOpenModelView(e) {
        console.log("onOpenModelView", e);
        var container = e.sender.element;
        var MVId = e.sender.id;
        switch (MVId) {
            case "#modalViewAddDelProfileServices": {
                var params = e.sender.element.data('profileInfo');
                console.log("Params:", params);
                var $title = container.find("[data-id='mvtitle']");
                $title.text(params.profile.NameProfile);
                initProfileServiceCount = params.profile.MeterServices.length;
                
                var allServsList = container
                        .find("[id='allDeviceServiceList']")
                        .data("kendoListBox"),
                    allProfileSelServsList = container
                        .find("[id='allProfileServiceList']")
                        .data("kendoListBox");

                if (allServsList)
                    allServsList.setDataSource(modelDeviceServices.deviceServices);

                setTimeout(function () {
                    allProfileSelServsList.dataSource.data(params.profile.MeterServices);
                    var selIds = params.profile.MeterServices.map(function (d) { return d.service_code });

                    var allServsArr = allServsList.dataSource.data();
                    var filteredArr = allServsArr.filter(function (d) {
                        return selIds.indexOf(d.service_code) === -1;
                    });
                    allServsList.dataSource.data(filteredArr);
                }, 1000);
                break;
            }
        }
    }

    function onModalViewInit(e) {
        console.log("modalViewInit", e);
        var container = e.sender.element;
        var modalViewId = e.sender.id;

        switch (modalViewId) {
            case "#modalViewAddDelProfileServices": {
                var $allListDevServices = container.find("#allDeviceServiceList"),
                    $profileListServices = container.find("#allProfileServiceList"),
                    $tmplServItem = container.find("#tmplServiceItem");                        

                $allListDevServices.kendoListBox({
                    dataSource: {
                        data: [],
                    },
                    connectWith: "allProfileServiceList",
                    toolbar: {
                        tools: ["transferTo", "transferFrom", "transferAllTo", "transferAllFrom", "remove"]
                    },
                    template: kendo.template($tmplServItem.html()),
                });

                $profileListServices.kendoListBox({
                    dataSource: { data: []},
                    template: kendo.template($tmplServItem.html()),
                    add: function (e) { console.log("add", e); },
                    remove: function (e) { console.log("remove", e); },
                    change: function (e) { console.log("change", e); },
                });

                var submitBtn = container.find('a[class*="SubmitChangesBtn"]');
                submitBtn.on('click', function (e) {
                    var profileServsLV = $("#read-profiles").find("#profilesListView").data("kendoListView");

                    var d = container.data("profileInfo");
                    if (initProfileServiceCount != d.profile.MeterServices.length)
                        profileServsLV.dataSource.pushUpdate({ NameProfile: d.profile.NameProfile, MeterServices: d.profile.MeterServices });
                    else
                        console.log("no update is necessary");

                    container.data("kendoMobileModalView").close();
                });
                var cancelBtn = container.find('a[class*="cancelChangesBtn"]');
                cancelBtn.on('click', function (e) {
                    container.data("kendoMobileModalView").close();
                });

                
                break;
            }
            case "": { break; }
            case "": { break; }
            default:
                break;
        }
    }

    var $profileLV;

    // Private methods:
    function viewInit(e) {
        var view = e.view;

        switch (view.id) {
            case "#wifi-network": {
                var $wifiModeSwitch = view.container.find("#wifimode-switch"),
                    $wifiApMode = view.container.find("#wifiApMode"),
                    $wifiNetworksMode = view.container.find("#wifiNetworksMode");

                var wifeModeSwitch = $wifiModeSwitch.data("kendoMobileSwitch");

                if (!wifeModeSwitch) {
                    wifeModeSwitch = $wifiModeSwitch.kendoMobileSwitch({
                        onLabel: "YES",
                        offLabel: "NO",
                        change: function (e) {
                            console.log("Wifi mode change", e);
                            if (e.sender.check() == true) {
                                //ap mode
                                view.model.set('modeState', "ap");
                                $wifiApMode.show()
                                $wifiNetworksMode.hide();
                            }
                            else {
                                view.model.set('modeState', "wifi");
                                $wifiApMode.hide();
                                $wifiNetworksMode.show();
                            }

                        },
                    }).data("kendoMobileSwitch");
                }

                var wifiMode = view.model.modeState;
                switch (wifiMode) {
                    case "ap":
                        wifeModeSwitch.check(true);
                        break;
                    case "wifi":
                        wifeModeSwitch.check(false);
                        break;
                    default:
                        wifeModeSwitch.check(true);
                        break;
                }

                wifeModeSwitch.trigger("change");
                return;
            }
            case "#modbus-config": {
                var $ddlModbusProtocol = view.container.find("#inputModbusProtocol"),
                  $ddlSerialPort = view.container.find("#inputSerialPort"),
                  $ddlSerialSpeed = view.container.find("#inputSerialSpeed");

                var ddlModbusProtocol = $ddlModbusProtocol.data("kendoDropDownList"),
                    ddlSerialPort = $ddlSerialPort.data("kendoDropDownList"),
                    ddlSerialSpeed = $ddlSerialSpeed.data("kendoDropDownList")
                
                if (!ddlModbusProtocol)
                    ddlModbusProtocol = $ddlModbusProtocol.kendoDropDownList({
                        dataSource: { data: ["RTU", "TCP"] }
                    }).data("kendoDropDownList");
                if (!ddlSerialPort)
                    ddlSerialPort = $ddlSerialPort.kendoDropDownList({
                        dataSource: { data: ["Port1", "Port2"] }
                    }).data("kendoDropDownList");
                if (!ddlSerialSpeed)
                    ddlSerialPort = $ddlSerialSpeed.kendoDropDownList({
                        dataSource: { data: [9660, 1200, 84500] }
                    }).data("kendoDropDownList");
                break;
            }
            case "#device-services": {
                var $deviceServiceLV = view.container.find("#deviceServicesList"),
                    $tmplItem = view.container.find("#tmplService"),
                    $tmplEditItem = view.container.find("#tmplEditService");                
                
                var deviceServicesListView =
                    $deviceServiceLV.kendoListView({
                    dataSource: modelDeviceServices.deviceServices,
                    template: kendo.template($tmplItem.html()),
                    editTemplate: kendo.template($tmplEditItem.html()),
                    selectable: false,
                    
                }).data("kendoListView");

                break;
            }
            case "#read-profiles": {
                $profileLV = view.container.find("#profilesListView");
                var $profilesPager = view.container.find("#profilesPager"),
                    $tmplItem = view.container.find("#tmplProfile"),
                    $tmplEditItem = view.container.find("#tmplEditProfile");
                     //$editServices = view.container.find("#editMeterServiceLayout");
              
                var $mvProfAddServices = view.container.find("#modalViewAddDelProfileServices");
                 var mv = $mvProfAddServices.data("kendoMobileModalView");

                    var profileListView = $profileLV.kendoListView({
                        dataSource: modelReadProfiles.profiles,
                        template: kendo.template($tmplItem.html()),
                        //editTemplate: kendo.template($tmplEditItem.html()),
                        selectable: true,
                        change: function (e) {
                            var lv = this.element.data("kendoListView");
                            var dataItemSel = lv.dataItem(this.select());

                           

                            //console.log("Selected Item 1:", dataItemSel);
                            console.log("Selected Item 2:", lv.dataItem(e.sender.select()));
                            $mvProfAddServices.data("profileInfo", { profile: dataItemSel })

                            mv.open();
                            mv.trigger("open");
                            //$editProfileServModalView.data("profileInfo", { modelServices: dataItemSel });
                            //var modalView = $editProfileServModalView.data("kendoMobileModalView");
                            //modalView.open();
                            //modalView.trigger("open");
                            //console.log("Selected Item open", $editProfileServModalView.data("profileInfo").modelServices);

                            //$editServices.show();
                            //$editServices.text(dataItemSel.NameProfile);
                        
                        },
                    }).data("kendoListView");
                break;
            }
            default:
                break;
        }
    }

    function viewShow(e) {
        var view = e.view;
        currentView = view;

        //Check if is login or cookie has expire
        var logState = zzCookie.isLogIn();
        if (logState != 1) {
            window.location.replace("login.html");
        }

        switch (view.id) {
            default:
                break;
        }
    }

    function logOutHandle_click(e) {
        console.log("Log out of app", e, currentView);
        zzCookie.setLogState(false);
        viewShow(currentView);
    }

    function navigateToSettings(e) {
        if (MainMobileApp.view().footer.length > 0) {
            MainMobileApp.navigate("#home"); // the id of the local view
            var tabstrip = MainMobileApp.view().footer.find(".km-tabstrip").data("kendoMobileTabStrip");
            tabstrip.switchTo("#home");
        }
    }

    MainMobileApp = new kendo.mobile.Application(
        $(document.body),
        {
            initial: "#home",
            layout: "default-layout",
            skin: "flat",
            init: function () {
                console.log("KenoMobileApp is ready");
                var logState = zzCookie.isLogIn();
            }
        });

    // Public methods:
    app.data = {
        modelHome: modelHome,
        modelLogout: modelLogout,
        modelAbout: modelAbout,
        modelWificard: modelWificard,
        modelLanInterface: modelLanInterface,
        modelSettingsFtp: modelSettingsFtp,
        modelCfgModbus: modelCfgModbus,
        modelDeviceDrivers: modelDeviceDrivers,
        modelDevices: modelDevices,
        modelReadProfiles: modelReadProfiles,
        modelDeviceServices: modelDeviceServices,
        modelTaskScheduled: modelTaskScheduled,

        //openProfileServEditModalView: openProfileServEditModalView,
        //closeProfileServEditModalView: closeProfileServEditModalView,

        //logTarget:logTarget,
        onOpenModelView: onOpenModelView,
        onModalViewInit: onModalViewInit,
        viewInit: viewInit,
        viewShow: viewShow,
        logOutFromApp: logOutHandle_click,
        navigateToSettings: navigateToSettings,
    };

}(MainApp, zzCookie));

//function clearMobileTabStrip() {
//    if (MainMobileApp.view().footer.length > 0) {
//        var tabstrip = MainMobileApp.view().footer.find(".km-tabstrip").data("kendoMobileTabStrip");
//        tabstrip.clear();
//    }  
//}


//$(function () {
//    //MainMobileApp = new kendo.mobile.Application(
//    //        $(document.body),
//    //        {
//    //            initial: "#home",
//    //            layout: "default-layout",
//    //            skin: "flat",
//    //            init: function () {
//    //                console.log("KenoMobileApp is ready");
//    //                var logState = zzCookie.isLogIn();
//    //                //switch (logState) {
//    //                //    case 1:
//    //                //        app.navigate("#home");
//    //                //        break;
//    //                //    case -1:
//    //                //    case 0:
//    //                //        app.navigate("../views/login.html");
//    //                //        break;
//    //                //}
//    //            }
//    //        });
//});


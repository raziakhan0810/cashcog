import {AgGridReact} from 'ag-grid-react';
import 'ag-grid/dist/styles/ag-grid.css';
import 'ag-grid/dist/styles/ag-theme-balham.css';
import React, {Component} from 'react';
import moment from 'moment';
import './App.css'

// eslint-disable-next-line no-undef
class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            columnDefs: [
                {
                    headerName: "UUID",
                    field: "uuid",
                    resizable: true
                },
                {
                    headerName: "CURRENCY",
                    field: "currency",
                    sortable: true,
                    resizable: true,
                    editable: true,
                    filter: 'agTextColumnFilter',
                    filterParams: {
                        filterOptions: ["contains", "notContains"],
                        debounceMs: 0,
                        caseSensitive: true,
                        suppressAndOrCondition: true
                    }
                },
                {
                    headerName: "AMOUNT",
                    field: "amount",
                    sortable: true,
                    resizable: true,
                    editable: false,
                    filter: 'agNumberColumnFilter'
                },
                {
                    headerName: "DESCRIPTION",
                    field: "description",
                    resizable: true,
                },
                {
                    headerName: "CREATED AT",
                    field: "created_at",
                    sortable: true,
                    resizable: true,
                    filter: 'agDateColumnFilter',
                    cellRenderer: (data) => {
                      return moment(data.created_at).format('MM/DD/YYYY')
                    },
                    filterParams:{
                        comparator: function (filterLocalDateAtMidnight, cellValue) {
                            let dateAsString = cellValue;
                            if (dateAsString == null) return 0;
                            let dateParts = dateAsString.split("/");
                            let day = Number(dateParts[2]);
                            let month = Number(dateParts[1]) - 1;
                            let year = Number(dateParts[0]);
                            let cellDate = new Date(day, month, year);
                            if (cellDate < filterLocalDateAtMidnight) {
                                return -1;
                            } else if (cellDate > filterLocalDateAtMidnight) {
                                return 1;
                            } else {
                                return 0;
                            }
                        }
                    }
                },
                {
                    headerName: "EMPLOYEE",
                    field: "employee.first_name",
                    width: 120,
                    height: 20,
                    sortable: true,
                    resizable: true,
                    editable: true,
                    filter: 'agTextColumnFilter',
                    filterParams: {
                        filterOptions: ["contains", "notContains"],
                        debounceMs: 0,
                        caseSensitive: true,
                        suppressAndOrCondition: true
                    },
                }
            ],
            rowData: [],
            defaultColDef: {
                sortable: true,
                resizable: true,
                autoSizeColumns: true
            },
            autoGroupColumnDef: {
                headerName: "CURRENCY",
                width: 200,
                field: "currency",
                valueGetter: function (params) {
                    if (params.node.group) {
                        return params.node.key;
                    } else {
                        return params.data[params.colDef.field];
                    }
                },
                cellRenderer: "agGroupCellRenderer",
            },
        };
        this.onGridReady = params => {
            this.gridApi = params.api;
            this.columnApi = params.columnApi;
            this.gridApi.sizeColumnsToFit();
            window.onresize = () => {
                this.gridApi.sizeColumnsToFit();
            };
            const httpRequest = new XMLHttpRequest();
            const updateData = data => {
                this.setState({rowData: data});
            };
            httpRequest.open(
                "GET",
                "http://localhost:8000/expense",
            );
            httpRequest.setRequestHeader("Authorization", "Token 6427d1edc42488a297608a063550fea5766a91b4");
            httpRequest.send();
            httpRequest.onreadystatechange = () => {
                if (httpRequest.readyState === 4 && httpRequest.status === 200) {
                    updateData(JSON.parse(httpRequest.responseText).res);
                }
            };
        };
    }

    render() {
        return (
            <div
                className="ag-theme-balham"
                style={{
                    height: `500px`,
                    margin: `20px`
                }}
            >
                <AgGridReact
                    columnDefs={this.state.columnDefs}
                    rowData={this.state.rowData}
                    onGridReady={this.onGridReady}
                    defaultColDef={this.state.defaultColDef}
                    autoGroupColumnDef={this.state.autoGroupColumnDef}
                    autoSizeColumns="True"
                    rowHeight="30"
                    headerHeight="30"
                >
                </AgGridReact>
            </div>
        );
    }
}

export default App;
